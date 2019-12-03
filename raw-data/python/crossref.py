#!/usr/bin/env python
# coding: utf-8

import requests

def getInfo(ref):
    url = "https://doi.crossref.org/servlet/query"

    querystring = {"usr":"halloweenwx@163.com","pwd":"halloween","format":"json","qdata":"""<?xml version = "1.0" encoding="UTF-8"?>
    <query_batch version="2.0" xmlns = "http://www.crossref.org/qschema/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <head>
          <email_address>hisham@atypon.com</email_address>
          <doi_batch_id>Sample multi resolve</doi_batch_id>
      </head>
      <body>
           <query key="mykey" enable-multiple-hits="true">
      <unstructured_citation>Girvan M, Newman MEJ (2002) Community structure in social and biological networks. Proceedings of the National Academy of Sciences 99: 7821–7826.
      </unstructured_citation>
    </query>
         </body>
    </query_batch>"""}

    headers = {
        'User-Agent': "PostmanRuntime/7.20.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "123bedd6-8fb9-43e5-980a-54336e7aa684,6312f073-8e24-4222-abb2-789899bbc01f",
        'Host': "doi.crossref.org",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    return response.text




