
  Feature: Manual Merchant Registration

    @Dunedin
    Scenario Outline: Register merchant with different data set
      Given API headers are provided
      When User executed API with <Currency> <OrderName> <order_info> and <return_Path> <orderID> <extraData> with <Channel> <Amount> <transactionHint> <Customer>
      Then Status code is returned
      Examples:
      | Currency |  OrderName | order_info    | return_Path                       | orderID       | extraData          |  Channel |  Amount | transactionHint | Customer       |
      | AED      |  Test Java | test          | http://demo-ipg.comtrust.ae/test  | TEST{Y}{m}{d} | I  am in ExtraData |  Web     |  10     | CPT:N           | Demo Merchant  |

    @Dunedin
    Scenario Outline: Payment Page Query
      Given API headers are provided
      When <Version> provided <Language> selected <Port> number <AddressIP> selected <ServerIP> with <ServerPort> and <Machine> for <Channel> and <TransactionID>
      Then Status code is returned
      Examples:
      | Version | Language  | Port  | AddressIP     | ServerIP      | ServerPort  | Machine       | Channel | TransactionID |
      | 2.0     | en        | 28742 | 86.96.250.27  | 195.229.84.28 | 443         | EPG-MS-SET-I  | Web     | 284304470226  |