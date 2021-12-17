import json

import requests

from payLoads.payLoad import *
from utilities.configurations import *

config = getConfig()

url = config['API']['endpoint']

headers = {"Content-Type": "application/json",
           "Accept": "application/json"
           }

# registerMerchant_response = requests.post(url, data=json.dumps(paymentQuery("2.0", "en", "28742", "86.96.250.27",
#                                                                             "195.229.84.28", "443", "EPG-MS-SET-I",
#                                                                             "Web", "284304470226", "Imtiaz",
#                                                                             "ProgramProgram99"), indent=4),
#                                           headers=headers)

# import pdb pdb.set_trace()

registerMerchant_response = requests.post(url, data=json.dumps(preAuthenticate("60204", "92.97.46.218",
                                                                               "BBC51CD1-8DB7-4DC3-A285-A3DC428A73C0",
                                                                               "195.229.84.28", "443", "EPG-MS-SET-I",
                                                                               "/DevPaymentEx/MerchantPay"
                                                                               "/GetPreAuthData",
                                                                               "En", "Web", "250384623618", "10",
                                                                               "Imtiaz", "ProgramProgram99", "AED", "C",
                                                                               "4111111111111111", "2022", "02", "123",
                                                                               "10", "2", "20211214125651",
                                                                               "Demo Merchant New"), indent=4), headers=headers)

print(registerMerchant_response.json())
print("Response Code is " + registerMerchant_response.json()["Transaction"]["ResponseCode"])
