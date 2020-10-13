---
title: "customBehavior"
slug: "custombehavior"
hidden: false
createdAt: "2020-06-15T21:05:01.870Z"
updatedAt: "2020-06-15T21:05:01.870Z"
---
__Property Manager name__: [Custom Behavior](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0031)

Allows you to insert a customized XML metadata behavior into any property's rule tree.  Talk to your Akamai representative to implement the customized behavior. Once it's ready, run PAPI's [List custom behaviors](https://learn.akamai.com/en-us/api/core_features/adaptive_acceleration/v1.html#getcustombehaviors) operation, then apply the relevant `behaviorId` value from the response within the current `customBehavior`. See [Custom behaviors and overrides](https://learn.akamai.com/en-us/api/core_features/property_manager/v1.html#custombehaviors) for guidance on custom metadata behaviors.

__Options__:

<div class="option" markdown="1" id="customBehavior.behaviorId" >

- `behaviorId` (_string_): The unique identifier for the predefined custom behavior you want to insert into the current rule.

</div>

</div>

<div class="feature" data-feature="datastream" markdown="1">
