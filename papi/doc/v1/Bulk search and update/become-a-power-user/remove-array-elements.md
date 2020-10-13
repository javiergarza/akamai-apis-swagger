---
title: "Remove array elements"
slug: "remove-array-elements"
hidden: false
createdAt: "2020-06-05T18:17:08.607Z"
updatedAt: "2020-06-10T03:12:14.066Z"
---
PAPI also supports an alternate `remove` JSON Patch operation.  This allows you to pop elements from an array, rather than replace the entire array.

For example, suppose you have a [`fileExtension`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#fileextension) criteria that matches `.imm` files. You can use this expression to match it within the criteria's `values`:

```
$..criteria[?(@.name == 'fileExtension'].options.values[?(@ == 'imm')]
```

You then specify a patch to `remove` the element from the array:

[block:code]
{
  "codes": [
    {
      "code": "\"patches\": [\n    {\n        \"op\": \"remove\",\n        \"path\": \"/rules/children/0/criteria/1/options/values/0\"\n    }\n]\n",
      "language": "json"
    }
  ]
}
[/block]