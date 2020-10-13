---
title: "Assign a variable"
slug: "assign-a-variable"
hidden: false
createdAt: "2020-06-05T17:23:45.885Z"
updatedAt: "2020-06-11T13:01:02.636Z"
---
Once you declare a variable within the `default` rule's `variables` array, you assign a value to it using the [`setVariable`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#setvariable) behavior, which you can place anywhere as appropriate within the rule tree. This example assigns the value of the built-in `AK_EXTENSION` variable to store the request's file extension in a user variable named `EXT`. To assign a variable, specify the `variableName` you want to modify, specify the `valueSource` as `EXPRESSION`, then as the `variableValue` inject the variable using the same syntax as in any other option field. In this example, setting the `TRANSFORM` to `NONE` means you don't yet want to change the value.

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"name\": \"setVariable\",\n    \"options\": {\n        \"variableName\": \"PMUSER_EXT\",\n        \"valueSource\": \"EXPRESSION\",\n        \"variableValue\": \"{{ \"{{\" }}builtin.AK_EXTENSION}}\",\n        \"transform\": \"NONE\"\n    }\n}\n",
      "language": "json"
    }
  ]
}
[/block]

The [`matchVariable`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#matchvariable) criteria allows you to test a variable's value at runtime. This example set of `criteria` tests if the request is for a filename with no extension, but requiring a filename and thus excluding any directory-style URLs that end with a slash character:

[block:code]
{
  "codes": [
    {
      "code": "\"criteriaMustSatisfy\": \"all\",\n\"criteria\": [\n  {\n    \"name\": \"matchVariable\",\n    \"options\": {\n      \"variableName\": \"AK_FILENAME\",\n      \"mode\": \"IS_NOT_EMPTY\"\n    }\n  },\n  {\n    \"name\": \"matchVariable\",\n    \"options\": {\n      \"variableName\": \"PMUSER_EXT\",\n      \"mode\": \"IS_EMPTY\"\n    }\n  }\n]\n",
      "language": "json"
    }
  ]
}
[/block]

> __Note__. While the [`matchVariable`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#matchvariable) criteria offers a way to account for known error scenarios, see the [Debug variables](#debugvariables) section for more information on the [`variableError`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#variableerror) criteria, which allows you to detect other unforeseen error scenarios that only reveal themselves at runtime.

In response to the test `criteria` above, one of the rule's accompanying `behaviors` may assign a static `EXPRESSION` of `html` for use as a default file extension:

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"name\": \"setVariable\",\n    \"options\": {\n        \"variableName\": \"PMUSER_EXT\",\n        \"valueSource\": \"EXPRESSION\",\n        \"variableValue\": \"html\",\n        \"transform\": \"NONE\"\n    }\n}\n",
      "language": "json"
    }
  ]
}
[/block]

You can assign values from many other sources besides built-in system variables. Setting the [`setVariable`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#setvariable) behavior's `valueSource` to `EXTRACT` gives you the option to assign more specific values from the request. The `extractLocation` may specify header, cookie, and query parameter names, certificates, path directory components, and any embedded path parameters. Setting `extractLocation` to `EDGESCAPE` allows you to leverage a great deal of location-based data based on this request. The sample behaviors below assign the client request's geographic location to a pair of `LAT` and `LONG` variables.

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"name\": \"setVariable\",\n    \"options\": {\n        \"variableName\": \"PMUSER_LAT\",\n        \"valueSource\": \"EXTRACT\",\n        \"extractLocation\": \"EDGESCAPE\",\n        \"locationId\": \"LAT\",\n        \"transform\": \"NONE\"\n    }\n},\n{\n    \"name\": \"setVariable\",\n    \"options\": {\n        \"variableName\": \"PMUSER_LONG\",\n        \"valueSource\": \"EXTRACT\",\n        \"extractLocation\": \"EDGESCAPE\",\n        \"locationId\": \"LONG\",\n        \"transform\": \"NONE\"\n    }\n}\n",
      "language": "json"
    }
  ]
}
[/block]

In addition, when the `valueSource` is set to `GENERATE`, you can incorporate various random numbers and hex strings into variables. See the [`setVariable`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#setvariable) behavior for details on all the sources of information you can assign to variables.