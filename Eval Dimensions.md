# Eval Dimensions
The following is the eval dimensions for the Cartwheel Agent created in HW 2

- Authenticated role 
  - Reason: The User types, impacts Authentication and is requried for evals
  - Values:Shopper, Merchant, Support
- User intent
  - Reason: Ensures testing all the functional areas supported and Out of Scope Functionalities
  - Values: Request Refund, Refund Status, View Order, View recent Orders, Product Questions, Policy Questions via Help center, Cancel Order, Out of Scope(Account Changes, Random Questions), Check on Escalation Request status
- The record involved (an order and its state, a product, a store policy page, or none) 
  - Reason: Details out type of record needed for the scenario
  - Values: ex. order above approval threshold, Order within 30 day return window, Order within 15 day return window, Product Within user Order, Store Policy More strict then Platform, or Null
- Applicable platform or store policy.
  - Reason: If there is a unique Platform or Store Policy that is leveraged, otherwise null
  - Values: Platform Return Policy, Store Specific Return Policy, Store product return scenario, etc.
- Request difficulty.
  - Reason: Provides diversity in types of user requests and data provided
  - Values:  Well Specified, Ambiguous, Missing Information, Boundry case (ex. refund on an order whose total exquals approval threshold)
- User Scenario
  - Reason: Handles different types of user tones and helps the Agent generalize through wider diversity in data set 
  - Values: neutral_conversational, terse_fragmentary, typo_heavy, confused_rambling, frustrated_impatient, repetitive_pressuring, operational_shorthand, requests_short_plain_answer
- Data Quality Issue
  - Reason: Provides the data quality example that should be given
  - Values: Data_quality_case_id (dq-product-duplicate-title, dq-product-missing-title, dq-product-invalid-price, dq-order-reversed-dates, dq-order-missing-delivery-date,dq-order-store-mismatch) or Null
- Number of Turns
  - Gives the ability for the user to ask follow up questions
  - Values: Number of times a user can respond with follow up messages

## Derrived Values
- Number of tool calls needed. 

# Hand Written Touples
*Based on the reading it highlighted the value of human doing 10-20 touples by hand o get an understanding of the data*
1) Shopper, Request Refund, Order below approval threshold, Platform return Policy, Well Specified, nweutral_Conversation, Null, 1
2) Shopper, Request Refund, Order Above approval Threshold, Platform Return policy, Ambiguous, typo_heavy, Null, 1
3) Shopper, View Order, Product within Order, Null, well specified, confused_rambling, Null, 1
4) Merchant, View Order, PRoduct within Order, Null, missing information, Frustrated_impatient, 1
5) Merchant, Cancel Order, Order over 30 days, null, Well specified, Operational_shorthand, DQ-order-reversed-dates, 1
6) Merchant, Request Refund, Order equal to approval Threshold, Platform Refund Policy, Boundry Case, Request_Short_plain_answers, Null, 1
7) Support, Policy Questions, Store Policy Refund page, Store Policy Refund different then Companyl, Ambiguous, typo_heavy, null, 1
8) Shopper, Cancel Order, Order Out of Cancel window, Platform Cancel Policy, Ambiguous, Repetitive_Pressure,3