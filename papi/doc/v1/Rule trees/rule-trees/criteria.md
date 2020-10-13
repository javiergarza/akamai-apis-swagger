---
title: "Criteria"
slug: "criteria"
hidden: false
createdAt: "2020-06-05T17:05:00.013Z"
updatedAt: "2020-06-10T03:20:03.505Z"
---
Rules are more powerful when they respond to the client request's different _criteria_. To do so, the rule needs to specify `children` containing an array of nested rule objects. Along with a descriptive `name`, child rules may contain an additional set of `criteria` objects that determine when its `behaviors` execute.

In this example, the child rule's [`contentType`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#contenttype) criteria matches requests for common HTML, CSS, and JavaScript files, and applies the [`gzipResponse`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#gzipresponse) behavior to compress them.

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"rules\": {\n        \"name\": \"default\",\n        \"options\": {\n            \"is_secure\": false\n        },\n        \"behaviors\": [\n            {\n                \"name\": \"origin\",\n                \"options\": {\n                    \"originType\": \"CUSTOMER\",\n                    \"hostname\": \"example.com\",\n                    \"forwardHostHeader\": \"REQUEST_HOST_HEADER\",\n                    \"cacheKeyHostname\": \"ORIGIN_HOSTNAME\",\n                    \"compress\": true,\n                    \"tcipEnabled\": false,\n                    \"httpPort\": 80\n                }\n            },\n            {\n                \"name\": \"cpCode\",\n                \"options\": {\n                    \"value\": {\n                        \"id\": 12345,\n                        \"name\": \"main site\"\n                    }\n                }\n            }\n        ],\n        \"children\": [\n            {\n                \"name\": \"Compress Text Content\",\n                \"criteria\": [\n                    {\n                        \"name\": \"contentType\",\n                        \"options\": {\n                            \"matchOperator\": \"IS_ONE_OF\",\n                            \"matchWildcard\": true,\n                            \"matchCaseSensitive\": false,\n                            \"values\": [\n                                \"text/html*\",\n                                \"text/css*\",\n                                \"application/x-javascript*\"\n                            ]\n                        }\n                    }\n                ],\n                \"behaviors\": [\n                    {\n                        \"name\": \"gzipResponse\",\n                        \"options\": { \"behavior\": \"ALWAYS\" }\n                    }\n                ]\n            }\n        ]\n    }\n}\n",
      "language": "json"
    }
  ]
}
[/block]

Criteria are structured exactly the same as `behavior` objects, with a `name` string identifier and a nested `options` object. Most criteria options behave similarly. The `values` option usually specifies the set of strings you're trying to match. Throughout PAPI, whenever a value is optionally plural, it's _always_ represented as an array. Various `matchWildcard` options allow you to match flexibly with `*` and `?` characters, and various `matchCaseSensitive` options allow you to ignore case. The `matchOperator` option typically allows you to invert the result, so that the criteria succeeds if specified values don't match.

The example above features a single [`contentType`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#contenttype) criteria. Once you define more than one, the rule needs a
`criteriaMustSatisfy` field to set whether to match `any` or `all`
criteria. This alternate example of the `children` array adds a
[`random`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#random)
criteria to match half the requests for the specified
[`contentType`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#contenttype).

[block:code]
{
  "codes": [
    {
      "code": "\"children\": [\n    {\n        \"name\": \"Compress Half of Requests for Text Content\",\n        \"criteriaMustSatisfy\": \"all\",\n        \"criteria\": [\n            {\n                \"name\": \"contentType\",\n                \"options\": {\n                    \"matchOperator\": \"IS_ONE_OF\",\n                    \"matchWildcard\": true,\n                    \"matchCaseSensitive\": false,\n                    \"values\": [\n                        \"text/html*\",\n                        \"text/css*\",\n                        \"application/x-javascript*\"\n                    ]\n                }\n            },\n            {\n                \"name\": \"random\",\n                \"options\": { \"bucket\": 50 }\n            }\n        ],\n        \"behaviors\": [\n            {\n                \"name\": \"gzipResponse\",\n                \"options\": { \"behavior\": \"ALWAYS\" }\n            }\n        ]\n    }\n]\n",
      "language": "json"
    }
  ]
}
[/block]

In this example, `criteriaMustSatisfy` is set to `all`. If it were set to `any`, the criteria would compress _all_ text content, and half of all other content, including images that are already compressed. This is almost certainly not what you want, and exemplifies the sort of problem that falls beyond what the API can identify for you, as discussed in the [Errors](#errors) section.

Note that rules don't provide any explicit support for _else_ cases in response to criteria matches, but there are a couple of ways to implement them:

- __Specify exclusive pairs of match criteria__. From the example above, the first rule could specify a `contentType` criteria that matches HTML/CSS/JavaScript using a `matchOperator` of `IS_ONE_OF`. The second rule could specify the same `contentType` criteria, only with a `matchOperator` of `IS_NOT_ONE_OF`.

- __Override a parent rule's behavior__. In the `random` example above, if you were to apply some other behavior to the remaining half of the requests, you'd need to do so as part of the parent rule. If the parent rule enables a behavior that shouldn't apply to the child, the child rule needs to specify the behavior again specifically to disable it.

Overall, the rules for how rules work are very simple. They're evaluated from top to bottom. A rule first evaluates its `criteria`, then executes its `behaviors` and `children` if the set of criteria matches. If any behavior is specified more than once within a set of executing rules, the last one overrides those that precede it. In some cases the ordering of different behaviors that perform similar functions may also matter. In other cases you can re-use the same behavior to do different things that don't conflict with each other, for example, by modifying one HTTP header and then a different one.

Based on the newly added custom hostname discussed in [Create a new edge hostname](#postedgehostnames), you'd typically add a corresponding set of rules. Appending this simple example to the rule's array of `children` as part of a PUT request tests the [`hostname`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#hostname) and assigns a different CP code to report on and separately bill for the custom site's traffic.

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"name\": \"Custom Site\",\n    \"criteria\": [\n        {\n            \"name\": \"hostname\",\n            \"options\": {\n                \"matchOperator\": \"IS_ONE_OF\",\n                \"values\": [ \"custom.example.com\" ]\n            }\n        }\n    ],\n    \"behaviors\": [\n        {\n            \"name\": \"cpCode\",\n            \"options\": {\n                \"value\": {\n                    \"id\": 54321,\n                    \"name\": \"custom site\"\n                }\n            }\n        }\n    ]\n}\n",
      "language": "json"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "success",
  "body": "While the [`hostname`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#hostname) criteria matches hostnames, the\n[`clientIp`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#clientip) criteria matches IP addresses."
}
[/block]

```
PUT /papi/v1/properties/prp_175780/versions/3/rules/?contractId=ctr_1-1TJZH5&groupId=grp_15225
```

If the API detects any problems with the data, they're noted as part of the response, and you may need to either fix or acknowledge them before you activate the property with that rule tree. See the [Activate a property](#postpropertyactivations) operation. For details on the range of problems you may encounter when modifying a rule tree, see the [Errors](#errors) section.