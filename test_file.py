import json

import requests

from payLoads.payLoad import *
from utilities.configurations import *

config = getConfig()

url = config['API']['endpoint']

headers = {"Content-Type": "application/json",
           "Accept": "application/json"
           }

registerMerchant_response = requests.post(url, data=json.dumps(
        paymentQuery("2.0", "en", "28742", "86.96.250.27", "195.229.84.28", "443", "EPG-MS-SET-I", "Web", "284304470226",
                     "Imtiaz", "ProgramProgram99"), indent=4), headers=headers)
# import pdb
# pdb.set_trace()


print(registerMerchant_response.json())
print(registerMerchant_response.json()["PaymentData"]["ResponseCode"])


