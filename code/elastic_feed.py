from elasticsearch import Elasticsearch
from log_util import log
import os

# import states

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


log(es.info())


def create_index_util(index):
    request_body = {
        "settings": {
            "index": {
                "analysis": {
                    "analyzer": {
                        "analyzer_shingle": {
                            "tokenizer": "standard",
                            "filter": [
                                "lowercase",
                                "filter_shingle"
                            ]
                        }
                    },
                    "filter": {
                        "filter_shingle": {
                            "type": "shingle",
                            "max_shingle_size": 4,
                            "min_shingle_size": 2,
                            "output_unigrams": "true"
                        }
                    }
                }
            }
        }, "mappings": {
            "properties": {
                "channel": {
                    "type": "keyword"
                },
                "contentType": {
                    "type": "keyword"
                },
                "contentdiff": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "county": {
                    "type": "keyword"
                },
                "createdatetime": {
                    "type": "text"
                },
                "htmldiff": {
                    "type": "text"
                },
                "state": {
                    "type": "keyword"
                },
                "url": {
                    "type": "text"
                },
                "title": {
                    "type": "keyword"
                },
                "previewText": {
                    "type": "nested",
                    "properties": {
                        "title": {"type": "text"},
                        "description": {"type": "text"},
                        "image": {"type": "text"},
                        "website": {"type": "text"}
                    }
                }
            }
        },
    }

    log("Creating Index")
    es.indices.create(index=index, body=request_body)
    log("Index Created")


# res = es.bulk(index = 'example_index', body = bulk_data)
def get_index_mapping(index):
    log(es.indices.get_mapping(index=index))


def check_index(index_hash):
    status = False
    if es.indices.exists(index=index_hash):
        status = True

    return status


def create_index(index):
    status = check_index(index)

    if not status:
        create_index_util(index)
        log("Index Created in main")
    get_index_mapping(index)


def delete_index(index):
    es.indices.delete(index=index, ignore=[400, 404])
    log("Deleted")


def feed_documents(index, json_data):
    es.index(index=index, doc_type="_doc", body=json_data)
    # log("Inserted !!")


def feed_nlp_document(index, diff_json):
    es.index(index=index, doc_type="_doc", body=diff_json)
    # log("json Inserted")


def search_index(index):
    results = es.search(body={"query": {"match_all": {}}}, index=index)
    for each in results['hits']['hits']:
        each = each['_source']['Url']
        log(each)

#
# log(es.indices.get_alias("*"))

# states = states.states
# count = 0
# for state in states:
#     log(state)
#     delete_index(index)
#     create_index(index)
#     count+=1
#
# log(count)
