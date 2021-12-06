from behave import *
import requests
from assertpy import assert_that

from payLoads.payLoad import *
from utilities.resources import *
import json

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



