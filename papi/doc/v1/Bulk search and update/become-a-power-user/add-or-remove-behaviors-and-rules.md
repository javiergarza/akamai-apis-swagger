---
title: "Add or remove behaviors and rules"
slug: "add-or-remove-behaviors-and-rules"
hidden: false
createdAt: "2020-06-05T18:18:03.287Z"
updatedAt: "2020-06-10T03:12:14.164Z"
---
In addition to modifying simple scalar values, you can `add` and `remove` objects within arrays. This powerful capability means you can bulk-add new behaviors or criteria to an existing rule, or add new rules anywhere within a rule tree configuration.  You can also bulk-remove any existing behaviors, criteria, or rules.  This section describes all of these possibilities.

Suppose you want add a [caching](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#caching) behavior to a rule that applies to image matches.

This rather complex JSONPath expression matches an array of `behaviors`.  The two test expressions filter results down to sets of behaviors whose parent rule includes a `fileExtension` criteria that includes `jpg` image extensions:

```
$..children[?(@.criteria[?(@.name == 'fileExtension' && 'jpg' in @.options.values)].behaviors
```

The last segment of the search can match the `behaviors` array itself, or an element within the array such as `behaviors[-1]`. Either way, the patch's `path` value needs to specify an index location.

This example adds a `caching` behavior object. The special `-` index adds the object to the end of the array:

[block:code]
{
  "codes": [
    {
      "code": "\"patches\": [\n    {\n        \"op\": \"add\",\n        \"path\": \"/rules/children/0/children/2/behaviors/-\",\n        \"value\": {\n            \"name\": \"caching\",\n            \"options\": {\n                \"behavior\": \"MAX_AGE\",\n                \"mustRevalidate\": false,\n                \"ttl\": \"30d\"\n            }\n        }\n    }\n]\n",
      "language": "json"
    }
  ]
}
[/block]

> __Tip__. Make sure to configure any behavior or criteria objects to
do what you want before bulk-adding them. To avoid validation errors,
you should copy behaviors that already work.

To remove a behavior, you need to match the entire object.  This modifies the previous search to select any `caching` behaviors triggered by an image `fileExtension` match:

```
$..children[?(@.criteria[?(@.name == 'fileExtension' && 'jpg' in @.options.values)].behaviors[?(@.name == 'caching')]
```

Based on the bulk search results, a `remove` patch operation like this trims the `caching` behavior from other executing behaviors:

[block:code]
{
  "codes": [
    {
      "code": "\"patches\": [\n    {\n        \"op\": \"remove\",\n        \"path\": \"/rules/children/0/children/2/behaviors/4\"\n    }\n]\n",
      "language": "json"
    }
  ]
}
[/block]

The ability to bulk-add objects to arrays means you can also design new self-contained rules, and add the objects to your configuration. This simple search matches the first set of rules that executes under the top-level default rule:

```
$.children
```

This sample patch appends a new rule object to the `children` array. The rule matches common image file extensions, then applies [Image Manager](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#imagemanager). You can add rules that are as large as you want:

[block:code]
{
  "codes": [
    {
      "code": "\"patches\": [\n    {\n        \"op\": \"add\",\n        \"path\": \"/rules/children/-\",\n        \"value\": {\n            \"name\": \"Image Manager\",\n            \"comments\": \"Scale images for mobile.\",\n            \"criteriaMustSatisfy\": \"all\",\n            \"criteria\": [\n                {\n                    \"name\": \"fileExtension\",\n                    \"options\": {\n                        \"matchCaseSensitive\": false,\n                        \"matchOperator\": \"IS_ONE_OF\",\n                        \"values\": [ \"jpg\", \"gif\", \"jpeg\", \"png\", \"imm\" ]\n                    }\n                }\n            ]\n            \"behaviors\": [\n                {\n                    \"name\": \"imageManager\",\n                    \"options\": {\n                        \"enabled\": true,\n                        \"resize\": true,\n                        \"applyBestFileType\": true,\n                        \"superCacheRegion\": \"US\",\n                        \"cpCodeOriginal\": null,\n                        \"cpCodeTransformed\": null,\n                        \"advanced\": false,\n                        \"policyTokenDefault\": \"adapt4mobile\"\n                    }\n                }\n            ],\n            \"children\": []\n        }\n    }\n]\n",
      "language": "json"
    }
  ]
}
[/block]

> __Tip__. It's easy to copy any rule that you know already works the
way you want, for use as the patch `value`.  Within Property Manager,
select the rule you want to bulk-add, press the __View Rule JSON__
button, and copy the JSON source data.  But keep in mind that the JSON
for each rule includes any nested sub-rules.  The large JSON for the
top-level default rule is the same one available with PAPI's
[Get a rule tree](#getpropertyversionrules) operation.