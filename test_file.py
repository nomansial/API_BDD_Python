import json

import requests

from payLoads.payLoad import *
from utilities.configurations import *

config = getConfig()

url = config['API']['endpoint']
headers = {"Content-Type": "application/json",
           "Accept": "application/json"
           }

registerMerchant_response = requests.post(url, data=json.dumps(registerMerchantPayload(10), indent=4), headers=headers)
# import pdb
# pdb.set_trace()


print(registerMerchant_response.json())
print(registerMerchant_response.json()["Transaction"]["ResponseCode"])


