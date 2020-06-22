import requests
import urllib3
from log_util import log
import os


def get_state_url(state_name):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # for server
    url = "https://" + os.getenv('elastic_server_host') + ":" + os.getenv('elastic_port') + "/crawler_urls/_search"
    # for azure
    # url = os.getenv('elastic_azure_host') + os.getenv('elastic_azure_port') + "/crawler_urls/_search"

    payload = "{\n\t\"query\": {\n    \"term\" : { \"state\" : \"" + state_name + "\" } \n  }\n}"

    # for server
    response = requests.post(url,
                             data=payload,
                             headers={'Content-Type': 'application/json'},
                             auth=(os.getenv('elastic_username'), os.getenv('elastic_password')),
                             verify=False).json()

    # for azure
    # response = requests.post(url,
    #                          data=payload,
    #                          headers={'Content-Type': 'application/json'},
    #                          auth=(os.getenv('elastic_azure_username'), os.getenv('elastic_azure_password')),
    #                          verify=False).json()

    # log(json.dumps(response, indent=2, sort_keys=True))
    hits = response["hits"]["hits"]
    source = hits[0]["_source"]
    state_urls = source["state_urls"]
    urls = []
    for state_url in state_urls:
        # urls.append(state_url["url"])
        if "facebook" in state_url["url"] or "twitter" in state_url["url"]:
            continue
        urls.append(state_url)
    # log(len(urls))
    return urls


if __name__ == "__main__":
    state_urls = get_state_url("pennsylvania")
    for state_url in state_urls:
        log(state_url)
