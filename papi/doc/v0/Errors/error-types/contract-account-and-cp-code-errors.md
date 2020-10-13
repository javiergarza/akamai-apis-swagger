---
title: "Contract, account, and CP code errors"
slug: "contract-account-and-cp-code-errors"
hidden: false
createdAt: "2020-06-05T21:22:05.239Z"
updatedAt: "2020-06-05T21:22:25.299Z"
---
| Code | Type | Problem |
| :--- | :--- | :--- |
| [400](https://httpstatuses.com/400) | `problem-extracting-contract-group` | Unable to calculate the contract or group assigned to a property, in which case you need to provide both `contractId` and `groupId` as query parameters. |
| [403](https://httpstatuses.com/403) | `cpcode/invalid-services` | The current product doesn't allow you to create CP codes.|
| [429](https://httpstatuses.com/429) | `cpcode/rate-limit-reached` | You made too many CP code requests. Try again later.|

These errors may be listed within [Rule](#rule) or
[Hostname](#hostname) objects, and may prevent you from
activating the property version:

| Type | Description |
| :--- | :--- |
| `advanced_cpcodes_outside_account_cp_validated_false` | The property invokes a CP code not provisioned under this account, and Origin Domains will be enforced. Contact your account representative for more information. |
| `advanced_cpcodes_outside_account_cp_validated_true` | The property invokes a CP code not provisioned under this account, and Origin Domain enforcement is disabled. Choose different CP codes, or move them into the current account. |
| `advanced_cpcodes_outside_group_or_contract` | The property invokes a CP code that doesn't belong to its group or contract. |
| `fixed_limit_exceeded` | A limit has been exceeded for the property. |
| `generic_behavior_issue.cpcode_created_recently` | The property invokes a recently created CP code that may not have fully propagated across the network. Activating the property version may disrupt your service. |
| `generic_behavior_issue.cpcode_not_available` | The specified CP code can't be used with this property. If you just created the CP code, try again later. |
| `limit_key.elements_per_property` | The property exceeds the number of allowed behaviors and criteria. |
| `limit_key.max_nested_rules` | The property exceeds the number of nested rules allowed. |
| `not_granted_by_modules_on_contract` | Your current contract doesn't include a necessary module. |
| `not_granted_by_modules_on_contract_readonly` | Your current contract doesn't include a necessary module. |
| `product_behavior_issue.cpcode_incorrect_product` | The CP code isn't configured for use with this property's product, which may affect how traffic is reported. |
| `product_not_on_contract` | The product isn't available on your contract. Add the product to the contract, or switch the property to a different product or contract. |