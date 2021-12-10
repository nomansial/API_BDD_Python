import json

import requests

from payLoads.payLoad import *
from utilities.configurations import *

config = getConfig()

url = config['API']['endpoint']

headers = {"Content-Type": "application/json",
           "Accept": "application/json"
           }

registerMerchant_response = requests.post(url, data=json.dumps(registerMerchant("AED", "Test Java", "test", "http://demo-ipg.comtrust.ae/test", "TEST{Y}{m}{d}", "I am in ExtraData", "Web", "10", "CPT:N", "Demo Merchant", "Imtiaz", "ProgramProgram99"), indent=4), headers=headers)
# import pdb
# pdb.set_trace()


print(registerMerchant_response.json())
print(registerMerchant_response.json()["Transaction"]["ResponseCode"])


