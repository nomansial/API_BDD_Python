from utilities.configurations import *


def registerMerchantPayload(amount):
    body = {
        "Registration": {
            "Currency": "AED",
            "OrderName": "Test Java",
            "OrderInfo": "OrderInfo",
            "ReturnPath": "http://demo-ipg.comtrust.ae/test",
            "OrderID": "TEST{Y}{m}{d}",
            "ExtraData": {
                "HelloWorld": "I am in ExtraData"
            },
            "Channel": "Web",
            "Amount": amount,
            "TransactionHint": "CPT:N",
            "Customer": "Demo Merchant",
            "UserName": "Imtiaz",
            "Password": "ProgramProgram99"
        }
    }
    return body


def registerMerchantExtraData(extraData):
    body = {
        "Registration": {
            "Currency": "AED",
            "OrderName": "Test Java",
            "OrderInfo": "OrderInfo",
            "ReturnPath": "http://demo-ipg.comtrust.ae/test",
            "OrderID": "TEST{Y}{m}{d}",
            "ExtraData": {
                "HelloWorld": extraData
            },
            "Channel": "Web",
            "Amount": "10",
            "TransactionHint": "CPT:N",
            "Customer": "Demo Merchant",
            "UserName": "Imtiaz",
            "Password": "ProgramProgram99"
        }
    }
    return body


def registerWithChannel(channel):
    body = {
        "Registration": {
            "Currency": "AED",
            "OrderName": "Test Java",
            "OrderInfo": "OrderInfo",
            "ReturnPath": "http://demo-ipg.comtrust.ae/test",
            "OrderID": "TEST{Y}{m}{d}",
            "ExtraData": {
                "HelloWorld": "I am in ExtraData"
            },
            "Channel": channel,
            "Amount": "10",
            "TransactionHint": "CPT:N",
            "Customer": "Demo Merchant",
            "UserName": "Imtiaz",
            "Password": "ProgramProgram99"
        }
    }
    return body


def currencyProvided(currency):
    body = {
        "Registration": {
            "Currency": currency,
            "OrderName": "Test Java",
            "OrderInfo": "OrderInfo",
            "ReturnPath": "http://demo-ipg.comtrust.ae/test",
            "OrderID": "TEST{Y}{m}{d}",
            "ExtraData": {
                "HelloWorld": "I am in ExtraData"
            },
            "Channel": "Web",
            "Amount": "10",
            "TransactionHint": "CPT:N",
            "Customer": "Demo Merchant",
            "UserName": "Imtiaz",
            "Password": "ProgramProgram99"
        }
    }
    return body


def returnPath(path):
    body = {
        "Registration": {
            "Currency": "AED",
            "OrderName": "Test Java",
            "OrderInfo": "OrderInfo",
            "ReturnPath": path,
            "OrderID": "TEST{Y}{m}{d}",
            "ExtraData": {
                "HelloWorld": "I am in ExtraData"
            },
            "Channel": "Web",
            "Amount": "10",
            "TransactionHint": "CPT:N",
            "Customer": "Demo Merchant",
            "UserName": "Imtiaz",
            "Password": "ProgramProgram99"
        }
    }
    return body


def orderName(order):
    body = {
        "Registration": {
            "Currency": "AED",
            "OrderName": order,
            "OrderInfo": "OrderInfo",
            "ReturnPath": "http://demo-ipg.comtrust.ae/test",
            "OrderID": "TEST{Y}{m}{d}",
            "ExtraData": {
                "HelloWorld": "I am in ExtraData"
            },
            "Channel": "Web",
            "Amount": "10",
            "TransactionHint": "CPT:N",
            "Customer": "Demo Merchant",
            "UserName": "Imtiaz",
            "Password": "ProgramProgram99"
        }
    }
    return body


def customerName(customer_name):
    body = {
        "Registration": {
            "Currency": "AED",
            "OrderName": "Test Java",
            "OrderInfo": "OrderInfo",
            "ReturnPath": "http://demo-ipg.comtrust.ae/test",
            "OrderID": "TEST{Y}{m}{d}",
            "ExtraData": {
                "HelloWorld": "I am in ExtraData"
            },
            "Channel": "Web",
            "Amount": "10",
            "TransactionHint": "CPT:N",
            "Customer": customer_name,
            "UserName": "Imtiaz",
            "Password": "ProgramProgram99"
        }
    }
    return body


def registerPassword(password):
    body = {
        "Registration": {
            "Currency": "AED",
            "OrderName": "Test Java",
            "OrderInfo": "OrderInfo",
            "ReturnPath": "http://demo-ipg.comtrust.ae/test",
            "OrderID": "TEST{Y}{m}{d}",
            "ExtraData": {
                "HelloWorld": "I am in ExtraData"
            },
            "Channel": "Web",
            "Amount": "10",
            "TransactionHint": "CPT:N",
            "Customer": "Demo Merchant",
            "UserName": "Imtiaz",
            "Password": password
        }
    }
    return body
