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

    print(context.registerMerchant_response.text)


@then(u'status code is returned')
def step_impl(context):
    assert_that(context.generated_response_code).is_equal_to("0")
