
  Feature: Manual Merchant Registration


    Scenario Outline: test registration with amount
      Given user basic information is provided
      When user executed API with <amount>
      Then status code is returned
      Examples:
        | amount  |
        | 10      |


    Scenario Outline: test registration with extra data
      Given user basic information is provided
      When run API with <extraData>
      Then status code is returned
      Examples:
        | extraData         |
        | I am in ExtraData |

    Scenario Outline: test registration with channel
      Given user basic information is provided
      When when <channel> is provided
      Then status code is returned
      Examples:
        | channel |
        | Web     |

    Scenario Outline: test registration with currency
      Given user basic information is provided
      When <currency> type is provided
      Then status code is returned
      Examples:
        | currency |
        | AED      |

    Scenario Outline: test registration with path
      Given user basic information is provided
      When return <path> is give to the request
      Then status code is returned
      Examples:
        | path                                  |
        | http://demo-ipg.comtrust.ae/test      |

    Scenario Outline: test registration with order name
      Given user basic information is provided
      When <order> name is provided
      Then status code is returned
      Examples:
        | order      |
        | Test Java |

    Scenario Outline: test registration with customer name
      Given user basic information is provided
      When <customer> is added for the order
      Then status code is returned
      Examples:
        | customer      |
        | Demo Merchant |


    Scenario Outline: register user with password
      Given user basic information is provided
      When certificate <password> is entered
      Then status code is returned
      Examples:
        | password         |
        | ProgramProgram99 |
