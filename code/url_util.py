import http.client
import os
import urllib.error
import urllib.request

from bs4 import BeautifulSoup

from get_state_urls import get_state_url
from log_util import log


def ignore_urls(link):
    link = link['href'].lower()
    if "mailto" in link:
        return True
    if "png" in link:
        return True
    if "jpg" in link:
        return True
    if "xlsx" in link:
        return True
    if "zip" in link:
        return True
    if "twitter" in link:
        return True
    if "facebook" in link:
        return True
    if "pdf" in link:
        return True
    return False


def get_all_url_utils(url):
    # log("Requested url is: " + url['url'])
    home_page_url = url['url'].split('/')
    if len(home_page_url) > 1:
        home_page_url = home_page_url[0] + '//' + home_page_url[2]
    url_list = []
    try:
        resp = urllib.request.urlopen(url['url'])
        soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'), features="html.parser")
        for link in soup.find_all('a', href=True):
            if "corona" in link['href'].lower() or "covid" in link['href'].lower():
                if ignore_urls(link):
                    continue
                url_dict = {}
                if link['href'].startswith('http'):
                    url_dict = {'url': link['href'], 'county': url['county'], 'contentType': url['contentType'],
                                'channel': url['channel']}
                else:
                    url_dict = {'url': home_page_url + link['href'], 'county': url['county'],
                                'contentType': url['contentType'],
                                'channel': url['channel']}
                url_list.append(url_dict)
    except urllib.error.HTTPError:
        log("urllib error http error for " + url['url'])
        pass
    except urllib.error.URLError:
        log("url error for " + url['url'])
        pass
    except ValueError:
        log("value error for " + url['url'])
        pass
    except ConnectionResetError:
        log("connection reset error " + url['url'])
        pass
    except http.client.InvalidURL:
        log("http client invalid url for " + url['url'])
        pass
    except UnboundLocalError:
        log("unbound local error for " + url['url'])
        pass
    except http.client.IncompleteRead:
        log("http client incomplete read " + url['url'])
        pass
    except TypeError:
        log("Type error for " + url['url'])
        pass
    return url_list


def get_all_url():
    full_list = []
    state_names = os.getenv('state')
    state_names = state_names.split(' ')

    for state in state_names:
        base_urls = get_state_url(state)
        pdf_urls = []

        rec_urls = []
        for start_url in base_urls:
            if "pdf" in start_url['url'].lower():
                pdf_urls.append(start_url)
            elif "corona" in start_url['url'].lower() or "covid" in start_url['url'].lower():
                if "cdc" in start_url['url'].lower():
                    full_list.append(start_url)
                else:
                    rec_urls.append(start_url)
            else:
                full_list.append(start_url)

        # log(len(rec_urls))
        for rec_url in rec_urls:
            urls = get_all_url_utils(rec_url)
            for url in urls:
                list_urls = get_all_url_utils(url)
                try:
                    for i in list_urls:
                        if i not in full_list:
                            # log("adding to list: " + i['url'])
                            full_list.append(i)
                except TypeError:
                    log('Whoops wrong content passed ' + TypeError.with_traceback())
            # log(rec_url + " " + str(len(full_list)))
        for pdf_url in pdf_urls:
            full_list.append(pdf_url)
        log("Pdf count " + str(len(pdf_urls)))
        log(state + " " + str(len(full_list)))
    return full_list


if __name__ == "__main__":
    urls = get_all_url()
    # url = {
    #     "url": "www.coronavirus.kdheks.gov",
    #     "county": "hennepin",
    #     "contentType": "provider",
    #     "channel": "url"
    # }
    # urls = get_all_url_utils(url)
    for url in urls:
        log(url)
