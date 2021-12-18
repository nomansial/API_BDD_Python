
  Feature: Manual Merchant Registration

    @Dunedin
    Scenario Outline: Register merchant API
      Given API headers are provided
      When User executed API with <Currency> <OrderName> <order_info> and <return_Path> <orderID> <extraData> with <Channel> <Amount> <transactionHint> <Customer>
      Then Status code is returned
      Examples:
      | Currency |  OrderName | order_info    | return_Path                       | orderID       | extraData          |  Channel |  Amount | transactionHint | Customer       |
      | AED      |  Test Java | test          | http://demo-ipg.comtrust.ae/test  | TEST{Y}{m}{d} | I  am in ExtraData |  Web     |  10     | CPT:N           | Demo Merchant  |

    @Dunedin
    Scenario Outline: Payment Page Query API
      Given API headers are provided
      When <Version> provided <Language> selected <Port> number <AddressIP> selected <ServerIP> with <ServerPort> and <Machine> for <Channel> and <TransactionID>
      Then Status code is returned
      Examples:
      | Version | Language  | Port  | AddressIP     | ServerIP      | ServerPort  | Machine       | Channel | TransactionID |
      | 2.0     | en        | 28742 | 86.96.250.27  | 195.229.84.28 | 443         | EPG-MS-SET-I  | Web     | 284304470226  |

    @Dunedin
    Scenario Outline: Pre Authenticate API
      Given API headers are provided
      When <Port> and <clientIp> along <Identifier> with <ServerIP> and <ServerPort> and <machine> with <url> when <lang> is <channel> then <transactionId> can be <amount> and <currency> so that <instrument> some with <cardnumber> year <year> month <month> code <code> and the <purchaseAmount> along <purchaseExponent> and <purchaseDate> with <merchantName>
      Then Status code is returned
      Examples:
      | Port  | clientIp    | Identifier                            | ServerIP      |  ServerPort  | machine       | url                                      | lang  | channel | transactionId | amount | currency | instrument  | cardnumber        | year | month  | code | purchaseAmount  | purchaseExponent | purchaseDate   | merchantName      |
      | 60204 |92.97.46.218 | BBC51CD1-8DB7-4DC3-A285-A3DC428A73C0  | 195.229.84.28 | 443          | EPG-MS-SET-I  | /DevPaymentEx/MerchantPay/GetPreAuthData | En    | Web     |250384623618   | 10     | AED      | C           | 4111111111111111  | 2022 | 02     |123   | 10              | 2                | 20211214125651 | Demo Merchant New |


    @Dunedin
    Scenario Outline: Finalize call API
      Given API headers are provided
      When <customerName> and <lang> are provided with <transactionID>
      Then Status code is returned
      Examples:
      | customerName  | lang  | transactionID  |
      | Demo Merchant | en    | 216063158375   |
