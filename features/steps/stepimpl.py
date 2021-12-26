import json

import requests
import pdb
from assertpy import assert_that
from behave import *

from payLoads.payLoad import *
from utilities.configurations import *

config = getConfig()


@given(u'API headers are provided')
def step_impl(context):
    context.url = config['API']['endpoint']
    context.userName = config['Credentials']['userName']
    context.passWord = config['Credentials']['passWord']
    context.headers = {"Content-Type": "application/json",
                       "Accept": "application/json"
                       }


@when(u'User executed API with {Currency} {OrderName} {order_info} and {return_Path} {orderID} {extraData} with {'
      u'Channel} {Amount} {transactionHint} {Customer}')
def step_impl(context, Currency, OrderName, order_info, return_Path, orderID, extraData, Channel, Amount,
              transactionHint, Customer):
    global transaction_id
    user_name = context.userName
    password = context.passWord

    context.registerMerchant_response = requests.post(context.url,
                                                      data=json.dumps(
                                                          registerMerchant(Currency, OrderName, order_info, return_Path,
                                                                           orderID, extraData, Channel, Amount,
                                                                           transactionHint, Customer, user_name,
                                                                           password), indent=4),
                                                      headers=context.headers)

    context.generated_response_code = context.registerMerchant_response.json()["Transaction"]["ResponseCode"]
    context.generated_description = context.registerMerchant_response.json()["Transaction"]["ResponseDescription"]
    if len(context.generated_response_code) == 1:
        transaction_id = context.registerMerchant_response.json()["Transaction"]["TransactionID"]
        print("Registration ID: " + transaction_id)
    else:
        print("Transaction ID not generated")

    print("Register API Description:" + context.generated_description)
    print("Register API Response Code:" + context.generated_response_code)
    print("\n")


@then(u'status code is returned')
def step_impl(context):
    assert_that(context.generated_description).is_equal_to("Request Processed Successfully")
    assert_that(context.generated_response_code).is_equal_to("0")


@when(u'for {Version} provided {Language} selected {Port} number {AddressIP} selected {ServerIP} with {ServerPort} '
      u'and {Machine} for {Channel}')
def step_impl(context, Version, Language, Port, AddressIP, ServerIP, ServerPort, Machine, Channel):
    user_name = context.userName
    password = context.passWord

    context.paymentQueryResponse = requests.post(context.url, data=json.dumps(
        paymentQuery(Version, Language, Port, AddressIP, ServerIP, ServerPort, Machine, Channel, transaction_id,
                     user_name, password), indent=4), headers=context.headers)

    context.generated_response_code = context.paymentQueryResponse.json()["PaymentData"]["ResponseCode"]
    context.generated_description = context.paymentQueryResponse.json()["PaymentData"]["ResponseDescription"]

    print("Payment Page Query API Description: " + context.paymentQueryResponse.json()["PaymentData"]["Response"
                                                                                                      "Description"])
    print("Payment Page Query API Response Code:  " + context.paymentQueryResponse.json()["PaymentData"]["Response"
                                                                                                         "Code"])
    print("\n")


@when(u'{port_num} and {clientIp} along {Identifier} with {ServerIP} and {ServerPort} and {machine} with {url} when {'
      u'lang} is {channel} for {amount} and {currency} so that {instrument} some with {cardnumber} year {year} month '
      u'{month} code {code} and the {purchaseAmount} along {purchaseExponent} and {purchaseDate} with {merchantName}')
def step_impl(context, port_num, clientIp, Identifier, ServerIP, ServerPort, machine, url, lang, channel,
              amount, currency, instrument, cardnumber, year, month, code, purchaseAmount,
              purchaseExponent, purchaseDate, merchantName):
    userName = context.userName
    password = context.passWord

    context.preAuthenticateResponse = requests.post(context.url, data=json.dumps(
        preAuthenticate(port_num, clientIp, Identifier, ServerIP, ServerPort, machine, url, lang, channel,
                        transaction_id, amount, userName, password, currency, instrument, cardnumber, year,
                        month, code,
                        purchaseAmount, purchaseExponent, purchaseDate, merchantName), indent=4),
                                                    headers=context.headers)

    context.generated_response_code = context.preAuthenticateResponse.json()["Transaction"]["ResponseCode"]
    context.generated_description = context.preAuthenticateResponse.json()["Transaction"]["ResponseDescription"]

    print(
        "Pre Authenticate Description: " + context.preAuthenticateResponse.json()["Transaction"]["ResponseDescription"])
    print("Pre Authenticate Response Code:  " + context.preAuthenticateResponse.json()["Transaction"]["ResponseCode"])
    print("\n")


@when(u'so when {customerName} and {lang} are provided')
def step_impl(context, customerName, lang):
    user_name = context.userName
    password = context.passWord

    context.finalize_response = requests.post(context.url,
                                              data=json.dumps(finalize(
                                                  customerName, lang, transaction_id, user_name, password),
                                                  indent=4),
                                              headers=context.headers)

    context.generated_response_code = context.finalize_response.json()["Transaction"]["ResponseCode"]
    context.generated_description = context.finalize_response.json()["Transaction"]["ResponseDescription"]

    print("Finalize API Description: " + context.finalize_response.json()["Transaction"]["ResponseDescription"])
    print("Finalize API Response Code:  " + context.finalize_response.json()["Transaction"]["ResponseCode"])
    print("\n")


@when(u'{year} and {currency} along {orderName} and {lang} combined {code} and {orderId} is {channel} and {month} '
      u'along {amount} also {cardNumber} for {hint} the {customer}')
def step_impl(context, year, currency, orderName, lang, code, orderId, channel, month, amount, cardNumber, hint,
              customer):
    user_name = context.userName
    password = context.passWord

    context.motoAutoCapture = requests.post(context.url,
                                            data=json.dumps(
                                                motoTransAutoCapture(user_name, password, year, currency, orderName,
                                                                     lang, code, orderId, channel, month, amount,
                                                                     cardNumber, hint, customer), indent=4),
                                            headers=context.headers)

    context.generated_response_code = context.motoAutoCapture.json()["Transaction"]["ResponseCode"]
    context.generated_description = context.motoAutoCapture.json()["Transaction"]["ResponseDescription"]

    print("Moto Transaction Auto Capture API Description: " + context.motoAutoCapture.json()["Transaction"]
    ["ResponseDescription"])
    print("Moto Transaction Auto Capture:  " + context.motoAutoCapture.json()["Transaction"]["ResponseCode"])
    print("\n")


@when(u'{currency} and {orderName} with {lang} for {orderId} along {channel} for {amount} and {hint} the {customer} '
      u'for {cardTrack2}')
def step_impl(context, currency, orderName, lang, orderId, channel, amount, hint, customer, cardTrack2):
    user_name = context.userName
    password = context.passWord

    context.track2 = requests.post(context.url,
                                   data=json.dumps(
                                       track2(user_name, password, currency, orderName, lang,
                                              orderId, channel, amount, hint, customer,
                                              cardTrack2), indent=4),
                                   headers=context.headers)

    context.generated_response_code = context.track2.json()["Transaction"]["ResponseCode"]
    context.generated_description = context.track2.json()["Transaction"]["ResponseDescription"]

    print("Track 2 API Description: " + context.track2.json()["Transaction"]["ResponseDescription"])
    print("Track 2 Auto Capture:  " + context.track2.json()["Transaction"]["ResponseCode"])
