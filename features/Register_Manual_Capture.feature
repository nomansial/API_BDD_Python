
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
      When for <Version> provided <Language> selected <Port> number <AddressIP> selected <ServerIP> with <ServerPort> and <Machine> for <Channel>
      Then Status code is returned
      Examples:
      | Version | Language  | Port  | AddressIP     | ServerIP      | ServerPort  | Machine       | Channel |
      | 2.0     | en        | 28742 | 86.96.250.27  | 195.229.84.28 | 443         | EPG-MS-SET-I  | Web     |

    @Dunedin
    Scenario Outline: Pre Authenticate API
      Given API headers are provided
      When <port_num> and <clientIp> along <Identifier> with <ServerIP> and <ServerPort> and <machine> with <url> when <lang> is <channel> for <amount> and <currency> so that <instrument> some with <cardnumber> year <year> month <month> code <code> and the <purchaseAmount> along <purchaseExponent> and <purchaseDate> with <merchantName>
      Then Status code is returned
      Examples:
      | port_num  | clientIp    | Identifier                            | ServerIP      |  ServerPort  | machine       | url                                      | lang  | channel | amount | currency | instrument  | cardnumber        | year | month  | code | purchaseAmount  | purchaseExponent | purchaseDate   | merchantName      |
      | 60204     |92.97.46.218 | BBC51CD1-8DB7-4DC3-A285-A3DC428A73C0  | 195.229.84.28 | 443          | EPG-MS-SET-I  | /DevPaymentEx/MerchantPay/GetPreAuthData | En    | Web     | 10      | AED      | C           | 4111111111111111  | 2022 | 02     |123   | 10              | 2                | 20211214125651 | Demo Merchant New |


    @Dunedin
    Scenario Outline: Finalize call API
      Given API headers are provided
      When so when <customerName> and <lang> are provided
      Then Status code is returned
      Examples:
      | customerName  | lang  |
      | Demo Merchant | en    |

    @Dunedin
    Scenario Outline: Moto Transaction Auto Capture
      Given API headers are provided
      When <year> and <currency> along <orderName> and <lang> combined <code> and <orderId> is <channel> and <month> along <amount> also <cardNumber> for <hint> the <customer>
      Then Status code is returned
      Examples:
      | year  | currency  | orderName  | lang  | code  | orderId          | channel | month | amount  | cardNumber      | hint    | customer     |
      | 2022  | AED       | Pinger-NBAD|  en   |  123  | 990000227113719  | W       | 11    | 10      |4111111111111111 | CPT:Y;  | Demo Merchant|


    @Dunedin
    Scenario Outline: Moto Transaction Auto Capture
      Given API headers are provided
      When <currency> and <orderName> with <lang> for <orderId> along <channel> for <amount> and <hint> the <customer> for <cardTrack2>
      Then Status code is returned
      Examples:
      | currency  | orderName   | lang  | orderId         | channel | amount  | hint  | customer       | cardTrack2                               |
      | AED       | inger-NBAD  | en    | 990000227113719 | T       | 10      | CPT:Y | Demo Merchant  |  ;4111111111111111=16112011000089600000? |
