import json

import requests
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


@when(
    u'User executed API with {Currency} {OrderName} {order_info} and {return_Path} {orderID} {extraData} with {'
    u'Channel} {Amount} {transactionHint} {Customer}')
def step_impl(context, Currency, OrderName, order_info, return_Path, orderID, extraData, Channel, Amount,
              transactionHint, Customer):
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
    context.generated_response_class = context.registerMerchant_response.json()["Transaction"]["ResponseClass"]

    print(context.registerMerchant_response.text)


@then(u'status code is returned')
def step_impl(context):
    assert_that(context.generated_response_code).is_equal_to("0")


@when(u'{Version} provided {Language} selected {Port} number {AddressIP} selected {ServerIP} with {ServerPort} and {'
      u'Machine} for {Channel} and {TransactionID}')
def step_impl(context, Version, Language, Port, AddressIP, ServerIP, ServerPort, Machine, Channel, TransactionID):
    user_name = context.userName
    password = context.passWord

    context.paymentQueryResponse = requests.post(context.url, data=json.dumps(
        paymentQuery(Version, Language, Port, AddressIP, ServerIP, ServerPort, Machine, Channel, TransactionID,
                     user_name, password), indent=4), headers=context.headers)

    context.generated_response_code = context.paymentQueryResponse.json()["PaymentData"]["ResponseCode"]
    print(context.paymentQueryResponse.text)


@when(u'{Port} and {clientIp} along {Identifier} with {ServerIP} and {ServerPort} and {machine} with {url} when {'
      u'lang} is {channel} then {transactionId} can be {amount} and {currency} so that {instrument} some with {'
      u'cardnumber} year {year} month {month} code {code} and the {purchaseAmount} along {purchaseExponent} and {'
      u'purchaseDate} with {merchantName}')
def step_impl(context, clientPort, clientIp, Identifier, ServerIP, ServerPort, machine, url, language, channel,
              transactionId, amount, currency, instrument, cardnumber, year, month, code,
              purchaseAmount, purchaseExponent, purchaseDate, merchantName):
    userName = context.userName
    password = context.passWord

    context.preAuthenticateResponse = requests.post(context.url, data=json.dumps(
        preAuthenticate(clientPort, clientIp, Identifier, ServerIP, ServerPort, machine, url, language, channel,
                        transactionId, amount, userName, password, currency, instrument, cardnumber, year, month, code,
                        purchaseAmount, purchaseExponent, purchaseDate, merchantName), indent=4),
                                                    headers=context.headers)

    context.generated_response_code = context.preAuthenticateResponse.json()["Transaction"]["ResponseCode"]
    print(context.paymentQueryResponse.text)
