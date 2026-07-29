import json
import os
import pprint
from base64 import b64encode
from datetime import datetime, timezone
from time import localtime, strftime

import requests
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
datacenter_url = os.getenv('datacenter_url')
customer_tenant_id = "4ca4a787-74f8-48ba-aa3f-15720ff695a0"

#Test without api client
base_url = f'{datacenter_url}/api/2'

response = requests.post(
    f'{base_url}/idp/token',
    headers={'Content-Type': 'application/x-www-form-urlencoded',
             'Authorization': 'Basic ' + b64encode(f'{client_id}:{client_secret}'.encode('ascii')).decode('ascii')},
    data={'grant_type': 'client_credentials'},
)

token_info = response.json()
expiry = datetime.fromtimestamp(timestamp=token_info["expires_on"])  # noqa: DTZ006
expiry = expiry.replace(tzinfo=timezone.utc) if expiry.tzinfo is None else expiry.astimezone(timezone.utc)
print(expiry)

auth = {'Authorization': 'Bearer ' + token_info['access_token']}
clientid_response = requests.get(f'{base_url}/clients/{client_id}', headers=auth)
tenant_id = clientid_response.json()['tenant_id']

datastuff = requests.get(f'{base_url}/tenants/{tenant_id}/usages', headers=auth)

print(datastuff.json())
