import os
import sys
import requests
import time


def read_from_url(url):
    subscription_key = os.getenv('ocr_subscription_key')

    endpoint = os.getenv('ocr_endpoint')

    text_recognition_url = endpoint + "vision/v2.1/read/core/asyncBatchAnalyze"
    # image_url= "https://onlinepngtools.com/images/preview-image-onlinepngtools.png"
    image_url = url
    headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    data = {'url': image_url}
    response = requests.post(text_recognition_url, headers=headers, json=data)

    if response.status_code not in [202]:
        print("could not process for url : " + url + " with response " + str(response.status_code))

    else:
        response.raise_for_status()
        operation_url = response.headers["Operation-Location"]

        result = {}
        poll = True
        while (poll):
            response_final = requests.get(
                response.headers["Operation-Location"], headers=headers)
            result = response_final.json()
            # print(result)
            time.sleep(1)
            if ("recognitionResults" in result):
                poll = False
            if ("status" in result and result['status'] == 'Failed'):
                poll = False

        if(poll==False):
            return "failed"

        text = ""
        for rec in result['recognitionResults']:
            for lines in rec['lines']:
                text = text + str(lines['text'])
        return text
#
# lines = read_from_url("https://www.cdc.gov/coronavirus/2019-ncov/downloads/DIY-cloth-face-covering-instructions.pdf")
#
# print(lines)
