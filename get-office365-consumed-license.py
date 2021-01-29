#!/usr/bin/env python3
import requests
import json
payload = {'grant_type': 'client_credentials', 'client_id': '{APP-ID}', 'client_secret': '{APP-SECRET}', 'scope': 'https://graph.microsoft.com/.default'}
tokenurl = 'https://login.microsoftonline.com/{TENANT-GUID}/oauth2/v2.0/token'
enterprisepackskuurl = 'https://graph.microsoft.com/v1.0/subscribedSkus/{SKU-ID}'
tokenrequest = requests.post(tokenurl, data=payload)
token = tokenrequest.json().get('access_token')
tokenheader = {'Authorization' : 'Bearer {}'.format(token)}
enterprisepackskurequest = requests.get(enterprisepackskuurl, headers=tokenheader)
enterprisepackconsumed = enterprisepackskurequest.json().get('consumedUnits')
print(enterprisepackconsumed)
