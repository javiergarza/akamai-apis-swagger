---
title: "Debug variables"
slug: "debug-variables"
hidden: false
createdAt: "2020-06-05T21:10:57.649Z"
updatedAt: "2020-06-10T03:14:34.279Z"
---
Most problems with rule trees are detected prior to activation, but problems with variables often occur only at runtime, and are thus more challenging to debug.

The most useful way to debug variables is to view their values in session-related response headers for test content on the staging network:

1. As discussed in the section on [Variables](doc:learn-about-variables), each variable defined in the default rule features two `hidden` and `sensitive` options, and you first need to disable both for any variables you want to inspect.

1. Activate the property that includes the variables on the staging network.

1. Once content activates, send a `Pragma:akamai-x-get-extracted-values` header in your test requests. The response includes `X-Akamai-Session-Info` headers that reflect the value of each declared variable.

1. After debugging, re-enable the `hidden` and `sensitive` options if necessary before activating to the production network.

Logging variables in session response headers allows you to check their final values after the rule tree executes. To specifically respond to errors as they occur within the rule tree, you can apply [`variableError`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#variableerror) criteria as part of a debugging rule after any [`setVariable`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#setvariable) that may cause a problem. For example, if you set user variables that extract the contents of a specific header or cookie name, an error results if either item is missing from the request. This criteria test executes if any errors occur for the specified set of variables:

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"name\" : \"variableError\",\n    \"options\" : {\n        \"variableNames\" : \"CUSTOM_HEADER CUSTOM_COOKIE\"\n    }\n}\n",
      "language": "json"
    }
  ]
}
[/block]

This approach doesn't allow you to report on the specific error, but you can still fashion appropriate behaviors, especially for use in testing on the staging network. For example, this denies the request and responds with an appropriate error:

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"name\" : \"denyAccess\",\n    \"options\" : {\n        \"enabled\" : true,\n        \"reason\" : \"missing-required-header-or-cookie\"\n    }\n}\n",
      "language": "json"
    }
  ]
}
[/block]

For more details on how variables work within rule trees, see [Assign a variable](doc:assign-a-variable), or [Variables](https://control.akamai.com/dl/rd/propmgr/PropMgr_CSH.htm#1151). in Control Panel.