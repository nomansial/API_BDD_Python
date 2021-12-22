import json

import requests
import pdb

from payLoads.payLoad import *
from utilities.configurations import *

config = getConfig()

url = config['API']['endpoint']

headers = {"Content-Type": "application/json",
           "Accept": "application/json"
           }
# pdb.set_trace()
# registerMerchant_response = requests.post(url, data=json.dumps(paymentQuery("2.0", "en", "28742", "86.96.250.27",
#                                                                             "195.229.84.28", "443", "EPG-MS-SET-I",
#                                                                             "Web", "238738648673", "Imtiaz",
#                                                                             "ProgramProgram99"), indent=4),
#                                           headers=headers)


registerMerchant_response = requests.post(url, data=json.dumps(preAuthenticate("60204", "92.97.46.218",
                                                                               "BBC51CD1-8DB7-4DC3-A285-A3DC428A73C0",
                                                                               "195.229.84.28", "443", "EPG-MS-SET-I",
                                                                               "/DevPaymentEx/MerchantPay"
                                                                               "/GetPreAuthData", "En", "Web",
                                                                               "273607407838", "10", "Imtiaz",
                                                                               "ProgramProgram99", "AED", "C",
                                                                               "4111111111111111",
                                                                               "2022", "02", "123", "10", "2",
                                                                               "20211214125651", "Demo Merchant New"),
                                                               indent=4), headers=headers)

# registerMerchant_response = requests.post(url, data=json.dumps(finalize("Demo Merchant", "en", "216063158375",
# "Imtiaz", "ProgramProgram99"), indent=4), headers=headers)

# registerMerchant_response = requests.post(url, data=json.dumps(motoTransAutoCapture("Imtiaz","ProgramProgram99",
# "2022","AED","Pinger-NBAD","en","123","990000227113719","W","11","10","4111111111111111","CPT:Y;","Demo Merchant"),
# indent=4), headers=headers)

# registerMerchant_response = requests.post(url, data=json.dumps(
#     track2("Imtiaz", "ProgramProgram99", "AED", "Pinger-NBAD", "en", "990000227113719", "T", "10",
#            "CPT:Y","Demo Merchant", ";4111111111111111=16112011000089600000?"),
#     indent=4), headers=headers)

print("Description: " + registerMerchant_response.json()["Transaction"]["ResponseDescription"])
print("Response Code:  " + registerMerchant_response.json()["Transaction"]["ResponseCode"])
