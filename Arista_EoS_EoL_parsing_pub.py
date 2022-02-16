#!/usr/bin/env/python3.8
# Get the portal access token from https://www.arista.com/en/users/profile

import requests
import json
import base64

token = '<your token>' # insert from the URL provided above
url = 'https://www.arista.com/custom_data/bug-alert/alertBaseDownloadApi.php'

creds = (base64.b64encode(token.encode())).decode("utf-8")

jsonpost = {'token_auth': creds,'file_version':'2'}

result = requests.post(url, data=json.dumps(jsonpost))

data = json.loads(result.text)

with open('./EoL_result_hw.txt', "w") as EoL_result:
    EoL_result.write(json.dumps((data.get('hardwareLifecycles')), indent=4, sort_keys=True))
