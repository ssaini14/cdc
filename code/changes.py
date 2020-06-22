import hashlib
import http.client
import os
import time
import urllib.error
from datetime import datetime

import requests
import schedule
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch
from link_preview import link_preview

import difffile
from elastic_feed import feed_documents, feed_nlp_document
from log_util import log
from nlp_data_writer import get_diff_json
from read_images import read_from_url
from url_util import get_all_url

# For server
es = Elasticsearch(
    [os.getenv('elastic_server_host')],
    http_auth=(os.getenv('elastic_username'), os.getenv('elastic_password')),
    scheme="https",
    port=os.getenv('elastic_port'),
    verify_certs=False
)

# For Azure Cloud
# es = Elasticsearch(os.getenv('elastic_azure_host') + os.getenv('elastic_azure_port'),
#                    http_auth=(os.getenv('elastic_azure_username'), os.getenv('elastic_azure_password')))

content = {}


# creating dictionary from list of urls of the format : old={"url1": content_of_url1,"url2": content_of_url2}
def find_change(content):
    log("job started")
    # urls = [{"url":"https://www.denvergov.org/content/dam/denvergov/Portals/771/documents/covid-19/FaceCoveringRequired_site_11x17.pdf"}]
    urls = get_all_url()
    log("total urls to be crawled " + str(len(urls)))

    html_diff = difffile.HtmlDiff(tabsize=4, wrapcolumn=80)

    connection_error_urls = []
    could_not_retrive_urls = []
    stop_iteration_urls = []
    new_urls = []

    for url in urls:
        pdf_content = False
        # log("going to " + url['url'])

        requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
        try:
            requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
        except AttributeError:
            # no pyopenssl support used / needed / available
            pass

        try:
            req = requests.get(url['url'])
        except requests.exceptions.ConnectionError:
            connection_error_urls.append(url)
            continue
        except requests.exceptions.TooManyRedirects:
            log("Too many redirects for: " + url['url'])
            continue
        except requests.exceptions.ChunkedEncodingError:
            log("Chunked encoding error " + url['url'])
            continue
        except requests.exceptions.InvalidURL:
            log("requests exception invalid url" + url['url'])
            continue
        except requests.exceptions.MissingSchema:
            log("request exception missing schema: " + url['url'])
            continue
        except UnicodeError:
            log("unicode error for " + url['url'])
            continue
        except requests.exceptions.InvalidSchema:
            log("requests exceptions invalid schema " + url['url'])
            continue

        if req.status_code in [200]:
            try:
                if req.headers['Content-Type'].split(';')[0] == 'application/pdf':
                    pdf_content = True
                    html = read_from_url(url['url'])  # still keeping the variable name as html
                    if html== "failed":
                        log("pdf ocr failed for url - " + url['url'])
                        continue
                else:
                    html = req.text
            except KeyError:
                log("Key error for " + url['url'])

        else:
            could_not_retrive_urls.append(url)
            html = None
            continue

        if url['url'] not in content.keys():
            content[url['url']] = html
            new_urls.append(url)
        else:
            old_html = content[url['url']]
            current_html = html
            content[url['url']] = current_html

            old_html_body = old_html
            current_html_body = current_html

            if not pdf_content:
                try:
                    current_html = BeautifulSoup(current_html.encode('utf-8').decode('ascii', 'ignore'), "html.parser")
                except UnboundLocalError:
                    log("unbound local error for " + url['url'])
                    continue
                except TypeError:
                    log("type error for " + url['url'])
                    continue
                [s.extract() for s in current_html.findAll(['script', 'style'])]
                try:
                    current_html_body = current_html.find('body').text
                except AttributeError:
                    log("attribute error for " + url['url'])
                    continue

                old_html = BeautifulSoup(old_html.encode('utf-8').decode('ascii', 'ignore'), "html.parser")
                [s.extract() for s in old_html.findAll(['script', 'style'])]
                if not old_html.find('body'):
                    continue
                old_html_body = old_html.find('body').text

            md5_1 = hashlib.md5()

            try:
                md5_1.update(old_html_body.encode('utf-8'))
            except AttributeError:
                log("Attribute error " + url['url'])
                continue
            hash_1 = md5_1.hexdigest()

            md5_2 = hashlib.md5()
            md5_2.update(current_html_body.encode('utf-8'))
            hash_2 = md5_2.hexdigest()

            if hash_1 == hash_2:
                pass
            else:
                if not pdf_content:
                    parsed_curr_html = BeautifulSoup(html.encode('utf-8').decode('ascii', 'ignore'), "html.parser")

                    title = ''
                    if parsed_curr_html.find('head'):
                        if parsed_curr_html.head.find('title'):
                            title = parsed_curr_html.head.find('title').text
                    try:
                        html_diffs = html_diff.make_file(old_html_body.splitlines(), current_html_body.splitlines(),
                                                         '<h2><a href= %s>%s</a></h2>' % (
                                                             "\"" + url['url'] + "\"", title),
                                                         "",
                                                         context=True, numlines=3)
                    except StopIteration:
                        log("stop iteration for " + url['url'])
                        stop_iteration_urls.append(url)
                        continue
                    except RecursionError:
                        log("recursion error for " + url['url'])
                        continue

                else:

                    title = url['url']

                    try:
                        html_diffs = html_diff.make_file(old_html.splitlines(), current_html.splitlines(),
                                                         '<h2><a href= %s>%s</a></h2>' % (
                                                             "\"" + url['url'] + "\"", title), "",
                                                         context=True, numlines=3)
                    except StopIteration:
                        stop_iteration_urls.append(url)
                        continue

                diff_json = get_diff_json(html_diffs, url['url'])

                if len(diff_json) > 0:
                    title = ""
                    description = ""
                    image = ""
                    website = ""

                    if not pdf_content:
                        try:
                            dict_elem = link_preview.generate_dict(url['url'])
                        except urllib.error.HTTPError:
                            log("urllib error http error " + url['url'])
                            continue
                        except UnicodeEncodeError:
                            log("unicode encode error " + url['url'])
                            continue
                        except IndexError:
                            log("index error for " + url['url'])
                            continue
                        except http.client.InvalidURL:
                            log("http client invalid url " + url['url'])
                            continue
                        except UnicodeDecodeError:
                            log("unicode decode error " + url['url'])
                            continue
                        except urllib.error.URLError:
                            log("urllib error url error " + url['url'])
                            continue
                        except ConnectionResetError:
                            log("connection reset error " + url['url'])
                            continue
                        title = dict_elem['title']
                        description = dict_elem['description']
                        image = dict_elem['image']
                        website = dict_elem['website']

                    html_diffs += ('<br><br>')  # ADD These
                    html_diffs += ('page link - <a href= %s>%s</a></h2>' % ("\"" + url['url'] + "\"", url['url']))
                    html_diffs += ('<br><br>')
                    # log(html_diffs)
                    index = "state_" + os.getenv('state').lower().replace(' ', '_')
                    state = os.getenv('state')
                    page_url = url['url']
                    htmldiff = html_diffs
                    createdatetime = datetime.now()
                    county = url['county']
                    contentType = url['contentType']
                    channel = url['channel']
                    contentdiff = ""
                    preview = {"title": title, "description": description, "image": image, "website": website}
                    # log(preview)

                    document = {"state": state, "channel": channel, "contentType": contentType,
                                "contentdiff": contentdiff,
                                "county": county, "createdatetime": createdatetime, "htmldiff": htmldiff,
                                "state": state,
                                "url": page_url, "title": title, "previewText": preview}
                    feed_documents(index, document)
                    for json in diff_json:
                        feed_nlp_document("nlp_data", json)
    log("job finished")


log("crawler started")
first_run = False
find_change(content)
first_run = True

schedule.every().day.at("13:00").do(find_change, content)
schedule.every().day.at("01:00").do(find_change, content)
log("schedule started")
while True:
    schedule.run_pending()
    time.sleep(1)

# find_change(content)
# find_change(content)
