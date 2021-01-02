# This is the beginning of the project where data is read in and data is alter visualised

import requests
import json

response = requests.get('https://www.pxweb.bfs.admin.ch/api/v1/en/px-x-0102020000_401/px-x-0102020000_401.px')

# Check Server Status
"""
if response.status_code == 200:
    print('Ok')
elif response.status_code == 301:
    print('Different endpoint')
elif response.status_code == 400:
    print('Bad request')
elif response.status_code == 401: 
    print('Not authenticated')
elif response.status_code == 403:
    print('Forbidden')
elif response.status_code == 404:
    print('Not found')
else: 
    print('Server not ready')                            
"""

#print(response.json())



def jprint(obj):
    text = json.dumps(obj, sort_keys=True,indent = 5)
    print(text)

jprint(response.json())

