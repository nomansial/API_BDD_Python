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


def preAuthenticate(clientPort, clientIp, Identifier, ServerIP, ServerPort, machine, url, language, channel,
                    transactionId, amount, userName, password, currency, instrument, cardnumber, year, month, code,
                    purchaseAmount, purchaseExponent, purchaseDate, merchantName):
    body = {
        "PreAuthData": {
            "Client": {
                "Port": clientPort,
                "AddressIP": clientIp,
                "Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/96.0.4664.110 Safari/537.36",
                "Identifier": Identifier
            },
            "Server": {
                "AddressIP": ServerIP,
                "Port": ServerPort,
                "Machine": machine,
                "Url": url
            },
            "Language": language,
            "Channel": channel,
            "TransactionID": transactionId,
            "Amount": amount,
            "UserName": userName,
            "Password": password,
            "Currency": currency,
            "Instrument": instrument,
            "CardNumber": cardnumber,
            "ExpiryYear": year,
            "ExpiryMonth": month,
            "VerifyCode": code,
            "ExtraData": {
                "ThreeDSTwoElements": {
                    "messageType": "AReq",
                    "deviceChannel": "03",
                    "messageVersion": "2.2.0",
                    "messageCategory": "01",
                    "threeDSRequestorID": "null",
                    "threeDSRequestorName": "null",
                    "threeDSRequestorURL": "null",
                    "acctNumber": "null",
                    "cardExpiryDate": "null",
                    "threeDSRequestorAuthenticationInd": "01",
                    "acquirerMerchantID": "null",
                    "merchantCountryCode": "null",
                    "acquirerBIN": "null",
                    "purchaseCurrency": "null",
                    "threeDSCompInd": "Y",
                    "threeDSServerRefNumber": "null",
                    "threeDSServerTransID": "2fe88cbd-edd1-458e-9535-b7652f10ddfa",
                    "threeDSServerURL": "null",
                    "recurringExpiry": "null",
                    "recurringFrequency": "null",
                    "browserAcceptHeader": "application/json, text/plain, */*",
                    "browserJavascriptEnabled": "true",
                    "browserLanguage": "En",
                    "browserUserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                        "like Gecko) Chrome/96.0.4664.110 Safari/537.36",
                    "notificationURL": "https://demo-ipg.ctdev.comtrust.ae/DevPaymentEx/MerchantPay/VerifyAuth?TID"
                                       "=250384623618",
                    "browserTZ": "-240",
                    "browserScreenHeight": "720",
                    "browserJavaEnabled": "true",
                    "browserColorDepth": "24",
                    "browserScreenWidth": "1280",
                    "mcc": "null",
                    "purchaseAmount": purchaseAmount,
                    "purchaseExponent": purchaseExponent,
                    "purchaseDate": purchaseDate,
                    "merchantName": merchantName,
                    "threeDSRequestorDecReqInd": "null"
                },
                "AutoFill": "false"
            },
            "AuthMethods": {
                "Redirection": {
                    "ReturnPath": "https%3a%2f%2fdemo-ipg.ctdev.comtrust.ae%2fdev_deploymenttest%2fPreFinalization"
                                  ".aspx%3fcapture%3dfalse",
                    "Browser": {
                        "UserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                     "like Gecko) Chrome/96.0.4664.110 Safari/537.36",
                        "AcceptHeaders": "application/json, text/plain, */*"
                    }
                }
            }
        }
    }

    return body


def finalize(customerName, lang, transactionID, username, password):
    body = {
        "Finalization": {
            "Customer": customerName,
            "Language": lang,
            "TransactionID": transactionID,
            "Password": password,
            "UserName": username
        }
    }

    return body
