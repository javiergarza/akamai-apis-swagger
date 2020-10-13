---
title: "Qualify a search"
slug: "qualify-a-search"
hidden: false
createdAt: "2020-06-05T17:46:33.362Z"
updatedAt: "2020-06-05T20:17:38.798Z"
---
Specifying additional search criteria can help you narrow down the
scope of the search to a smaller set of property configurations.

Suppose you want all origins where the `hostname` is
`old.example.com`, but only those tracked under a specific CP code.
The information you want to test appears within the default rule as
the `cpCode` behavior.  Form another JSONPath expression with logic
as in this example, which matches rule trees with a specific CP
code value:

```
$.behaviors[?(@.name == 'cpCode'].options.value[?(@.id == 12345)].id
```

Specify this as `bulkSearchQualifiers` criteria.  For the search to
produce results, the `match` criteria needs to yield results, but only
those where the full set of `bulkSearchQualifiers` also matches the
configuration:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"bulkSearchQuery\": {\n        \"syntax\": \"JSONPATH\",\n        \"match\": \"$.behaviors[?(@.name == 'origin')].options[?(@.hostname == 'old.example.com')].hostname\",\n        \"bulkSearchQualifiers\": [\n            \"$.behaviors[?(@.name == 'cpCode'].options.value[?(@.id == 12345)].id\"\n        ]\n    }\n}\n",
      "language": "json"
    }
  ]
}
[/block]
These additional qualifiers test the configuration independently from
the `match`, and the locations they match within the rules don't
appear as search results themselves.


[block:callout]
{
  "type": "success",
  "body": "There may be cases where a single `match` may be able to\ncombine all the logic you want within a single expression.  But in\nsome cases, specifying a separate set of `bulkSearchQualifiers` may\nallow you to simplify the main `match` syntax."
}
[/block]