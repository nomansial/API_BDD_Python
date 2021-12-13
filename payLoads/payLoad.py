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


def paymentQuery(Version, Language, Port, AddressIP, ServerIP, ServerPort, Machine, Channel, TransactionID, UserName,
                 Password):
    body = {
        "PaymentData": {
            "@version": Version,
            "Language": Language,
            "Client": {
                "Port": Port,
                "AddressIP": AddressIP,
                "Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/96.0.4664.93 Safari/537.36",
                "Identifier": "35D9831D-B51D-486B-B368-8A5AA55C1F0A"
            },
            "Server": {
                "AddressIP": ServerIP,
                "Port": ServerPort,
                "Machine": Machine,
                "Url": "/DevPaymentEx/MerchantPay/GetPaymentData"
            },
            "Channel": Channel,
            "TransactionID": TransactionID,
            "UserName": UserName,
            "Password": Password
        }
    }

    return body
