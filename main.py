# This is the beginning of the project where data is read in and data is alter visualised

import requests
import json

response = requests.get('https://data.bs.ch/api/v2/catalog/datasets/100079/exports/json')

# Check Server Status

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


#print(response.json())


def jprint(obj):
    text = json.dumps(obj, sort_keys=True,indent = 5)
    print(text)

jprint(response.json())

