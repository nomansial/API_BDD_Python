import json

import requests
from assertpy import assert_that
from behave import *

from payLoads.payLoad import *
from utilities.configurations import *

config = getConfig()


@given(u'user basic information is provided')
def step_impl(context):
    context.url = config['API']['endpoint']
    context.headers = {"Content-Type": "application/json",
                       "Accept": "application/json"
                       }


@when(u'user executed API with {amount}')
def step_impl(context, amount):
    context.registerMerchant_response = requests.post(context.url,
                                                      data=json.dumps(registerMerchantPayload(amount), indent=4),
                                                      headers=context.headers)
    context.status_code = context.registerMerchant_response.json()["Transaction"]["ResponseCode"]


@then(u'status code is returned')
def step_impl(context):
    assert_that(context.status_code).is_equal_to("0")


@when(u'run API with {extraData}')
def step_impl(context, extraData):
    context.registerMerchant_response = requests.post(context.url,
                                                      data=json.dumps(registerMerchantExtraData(extraData), indent=4),
                                                      headers=context.headers)
    context.status_code = context.registerMerchant_response.json()["Transaction"]["ResponseCode"]


@when(u'when {channel} is provided')
def step_impl(context, channel):
    context.registerMerchant_response = requests.post(context.url,
                                                      data=json.dumps(registerWithChannel(channel), indent=4),
                                                      headers=context.headers)
    context.status_code = context.registerMerchant_response.json()["Transaction"]["ResponseCode"]


@when(u'{currency} type is provided')
def step_impl(context, currency):
    context.registerMerchant_response = requests.post(context.url,
                                                      data=json.dumps(currencyProvided(currency), indent=4),
                                                      headers=context.headers)
    context.status_code = context.registerMerchant_response.json()["Transaction"]["ResponseCode"]


@when(u'return {path} is give to the request')
def step_impl(context, path):
    context.registerMerchant_response = requests.post(context.url,
                                                      data=json.dumps(returnPath(path), indent=4),
                                                      headers=context.headers)
    context.status_code = context.registerMerchant_response.json()["Transaction"]["ResponseCode"]


@when(u'{customer} is added for the order')
def step_impl(context, customer):
    context.registerMerchant_response = requests.post(context.url,
                                                      data=json.dumps(customerName(customer), indent=4),
                                                      headers=context.headers)
    context.status_code = context.registerMerchant_response.json()["Transaction"]["ResponseCode"]


@when(u'{order} is provided')
def step_impl(context, order):
    context.registerMerchant_response = requests.post(context.url,
                                                      data=json.dumps(orderName(order), indent=4),
                                                      headers=context.headers)
    context.status_code = context.registerMerchant_response.json()["Transaction"]["ResponseCode"]


@when(u'certificate {password} is entered')
def step_impl(context, password):
    context.registerMerchant_response = requests.post(context.url,
                                                      data=json.dumps(registerPassword(password), indent=4),
                                                      headers=context.headers)
    context.status_code = context.registerMerchant_response.json()["Transaction"]["ResponseCode"]
