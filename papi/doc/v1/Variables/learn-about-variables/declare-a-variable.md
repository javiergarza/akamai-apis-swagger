---
title: "Declare a variable"
slug: "declare-a-variable"
hidden: false
createdAt: "2020-06-05T17:22:54.076Z"
updatedAt: "2020-06-11T13:01:02.631Z"
---
While the built-in system variables described above are read-only, you can create and modify your own set of _user_ variables. You can base their values on built-in system variables or other data about the request's context, then transform them as described in the [Modify a variable](#modifyavariable) section.

First you need to declare the variable within the default rule's `variables` array, otherwise you get an error when you later try to assign to them or invoke them in option values. The example below defines a single variable whose unique underlying name is `VAR_NAME`. Variable names may only feature alphanumeric and underscore characters. Uppercase is recommended by convention but is optional.

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"rules\": {\n        \"name\": \"default\",\n        \"criteriaMustSatisfy\": \"all\",\n        \"options\": {\n            \"is_secure\": false\n        },\n        \"variables\": [\n            {\n                \"name\": \"VAR_NAME\",\n                \"value\": \"default value\",\n                \"description\": \"This is a sample Property Manager variable.\",\n                \"hidden\": false,\n                \"sensitive\": false\n            }\n        ],\n        \"criteria\": [],\n        \"behaviors\": [],\n        \"children\": []\n    }\n}\n",
      "language": "json"
    }
  ]
}
[/block]

For details on the members included in each variable declaration object, see [Rule.variables[]](#82234a11).

There are three different ways variable names appear:

- Within the `variables` declaration, you specify the base `VAR_NAME`.

- When you modify the variable with [`setVariable`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#setvariable) or match it with [`matchVariable`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#matchvariable), you add a `PMUSER_` prefix to refer to the variable name as `PMUSER_VAR_NAME`. (In activated metadata, this appears as `%(PMUSER_VAR_NAME)`.)

- When you insert the variable as an expression within behavior and criteria option fields, you need an additional `user.` namespace prefix: `{{user.PMUSER_VAR_NAME}}`.