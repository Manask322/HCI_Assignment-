
from django.shortcuts import render
from django.http import HttpResponse

import requests
import urllib.request
import urllib.response
import sys
import os, glob

import http.client, urllib
import json
import re
import os
import ast

from NLP.audio2text import *


accessKey = '1a970c6aee584bd2aa0e2e535c84d6e4'
url = 'westcentralus.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/keyPhrases'
result = []

def get_details(result):
    res = {}
    res['Address'] = str(result['documents'][0]['keyPhrases'][0])
    res['Intensity'] = 2
    res['Remark'] = str(result['documents'][0]['keyPhrases'][1])
    return res

def get_info(converted_text):
    # 1.
    print("Extracting Text")
    documents = extractText(converted_text)
    # 2. Perform Text Analysis
    print("Getting Authentication for Text Analytics")
    result = TextAnalytics(documents)
    print("Authenticated")
    result = result.decode("ascii")
    print("Extractinf literal value")
    result = ast.literal_eval(result)
    print("Values extracted successfully")
    print(result)
    print("results printed successfully")
    print(result, ",,,.... " , type(result['documents'][0]['keyPhrases']))
    print(result['documents'][0]['keyPhrases'][0])
    res = get_details(result)
    return res
    # 3. Print Results
    #print (json.dumps(json.loads(result), indent=4))

def extractText(converted_text):
    documents = { 'documents': []}
    count = 1
    text =converted_text
    #text = text.strip('\n')
    text = text.encode('ascii','ignore').decode('ascii')
    documents.setdefault('documents').append({"language":"en","id":str(count),"text":text})
    #count+= 1
    return documents


def TextAnalytics(documents):
    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = http.client.HTTPSConnection(url)
    body = json.dumps (documents)
    conn.request ("POST", path, body, headers)
    response = conn.getresponse ()
    return response.read ()
