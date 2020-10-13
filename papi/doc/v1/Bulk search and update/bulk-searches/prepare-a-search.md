---
title: "Prepare a search"
slug: "prepare-a-search"
hidden: false
createdAt: "2020-06-05T17:45:27.450Z"
updatedAt: "2020-06-11T13:00:54.631Z"
---
To match the specific `hostname` value within the [`origin`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#origin) behavior, you need a JSONPath expression as in this example:

```
$.behaviors[?(@.name == 'origin')].options[?(@.hostname == 'old.example.com')].hostname
```

The [Sample bulk updates](#samplebulkupdates) section lists other types of search, and the [Contextual searches](#contextualsearches) section provides more detailed guidance on the syntax. This expression applies two filters to a set of behaviors on the default rule. The first tests its `name`, and the second tests the value of its `hostname` option.

Specify the JSONPath expression as a `match` in a [BulkSearch](#bulksearch) POST request object, for example:

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"bulkSearchQuery\": {\n        \"syntax\": \"JSONPATH\",\n        \"match\": \"$.behaviors[?(@.name == 'origin')].options[?(@.hostname == 'old.example.com')].hostname\"\n    }\n}\n",
      "language": "json"
    }
  ]
}
[/block]

The `bulkSearchQuery` area collects all the details about your search. The only available `syntax` is `JSONPATH`.  Make sure any double-quote characters in the `match` JSONPath value are escaped with backslashes, otherwise you can use single quotes, as in this example.

See [BulkSearch](#bulksearch) for more details on this object.