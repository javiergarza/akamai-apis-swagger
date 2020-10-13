---
title: "Modify a variable"
slug: "modify-a-variable"
hidden: false
createdAt: "2020-06-05T17:27:19.291Z"
updatedAt: "2020-06-05T17:27:19.292Z"
---
In all of the examples above, the `transform` option is set to `NONE`,
which leaves the value unchanged after assigning it, but it supports a
large set of functions that in effect offers an embedded programming
language. Transform functions allow you to:

- do basic arithmetic
- perform bitwise operations
- convert case
- locate and generate substrings
- make regular expression substitutions
- perform many conversions and encodings

See the
[`setVariable`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#setvariable)
behavior for comprehensive details.

To modify a value within any
[`setVariable`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#setvariable)
behavior, set its `transform` function along with any necessary
dependencies. Each behavior can only transform its value once, so to
transform a value more than once you need to form a chain of
[`setVariable`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#setvariable)
behaviors. Each subsequent behavior needs to reassign the transformed
value back to itself, then perform an additional transformation.

This simple example modifies a `LANG` user variable, assigning it the
value of the request's `Accept-Language` header. The initial behavior
performs a `SUBSTRING` transform to limit the string to the initial
two-letter code. The second behavior reassigns `{{ "{{" }}user.PMUSER_LANG}}`
back into `LANG`, then runs the `UPPER` transform to convert to
uppercase.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"name\": \"setVariable\",\n    \"options\": {\n        \"variableName\": \"PMUSER_LANG\",\n        \"valueSource\": \"EXTRACT\",\n        \"extractLocation\": \"CLIENT_REQUEST_HEADER\",\n        \"headerName\": \"Accept-Language\",\n        \"transform\": \"SUBSTRING\",\n        \"startIndex\": \"1\",\n        \"endIndex\": \"2\"\n    }\n},\n{\n    \"name\": \"setVariable\",\n    \"options\": {\n        \"variableName\": \"PMUSER_LANG\",\n        \"valueSource\": \"EXPRESSION\",\n        \"variableValue\": \"{{ \"{{\" }}user.PMUSER_LANG}}\",\n        \"transform\": \"UPPER\"\n    }\n}\n",
      "language": "json"
    }
  ]
}
[/block]
For more details on how to use variables within the Property Manager
portal, see
[Variables](https://control.akamai.com/dl/rd/propmgr/PropMgr_CSH.htm#1151).