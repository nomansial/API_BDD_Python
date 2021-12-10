from utilities.configurations import *


def registerMerchant(currency, orderName, orderInfo, returnPath, orderID, extraData, channel, amount,
                     transactionHint, customer, userName, Password):
    body = {
        "Registration": {
            "Currency": currency,
            "OrderName": orderName,
            "OrderInfo": orderInfo,
            "ReturnPath": returnPath,
            "OrderID": orderID,
            "ExtraData": {
                "HelloWorld": extraData
            },
            "Channel": channel,
            "Amount": amount,
            "TransactionHint": transactionHint,
            "Customer": customer,
            "UserName": userName,
            "Password": Password
        }
    }
    return body
