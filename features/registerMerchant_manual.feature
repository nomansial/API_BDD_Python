
  Feature: Manual Merchant Registration


    Scenario Outline: Register merchant with different data set
      Given API headers are provided
      When User executed API with <Currency> <OrderName> <order_info> and <return_Path> <orderID> <extraData> with <Channel> <Amount> <transactionHint> <Customer>
      Then Status code is returned
      Examples:
      | Currency |  OrderName | order_info    | return_Path                       | orderID       | extraData          |  Channel |  Amount | transactionHint | Customer       |
      | AED      |  Test Java | test          | http://demo-ipg.comtrust.ae/test  | TEST{Y}{m}{d} | I  am in ExtraData |  Web     |  10     | CPT:N           | Demo Merchant  |
      | AED      |  Java Test | testing       | http://demo-ipg.comtrust.ae/test  | TEST{Y}{m}{d} | This is extra Data |  Web     |  20     | CPT:N           | Demo Merchant  |
      #| PKT      |  Java Test | testing       | http://demo-ipg.comtrust.ae/test  | TEST{Y}{m}{d} | This is extra Data |  Web     |  20     | CPT:N           | Demo Merchant  |
