---
title: "Check search results"
slug: "check-search-results"
hidden: false
createdAt: "2020-06-05T17:49:26.556Z"
updatedAt: "2020-06-05T20:19:59.544Z"
---
After launching the bulk search, make a GET call on the link provided
in the POST response.  For example:

```
GET /papi/v0/bulk/rules-search-requests/737
```

For details on this GET operation, see [List bulk search
results](#getbulksearch).

The response object reflects back the original request's
`bulkSearchQuery`, to provide you context to help interpret the
additional search `results`, which span all properties available to
you in any account:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"bulkSearchId\": 5,\n    \"searchTargetStatus\": \"IN_PROGRESS\",\n    \"searchSubmitDate\": \"2018-01-18T00:00:00Z\",\n    \"searchUpdateDate\": \"2018-01-18T00:01:00Z\",\n    \"bulkSearchQuery\": {\n        \"syntax\": \"JSONPATH\",\n        \"match\": \"$.behaviors[?(@.name == 'origin')].options[?(@.hostname == 'old.example.com')].hostname\"\n    },\n    \"results\": [\n        {\n            \"propertyId\": \"prp_15\",\n            \"propertyVersion\": 2,\n            \"stagingStatus\": \"INACTIVE\",\n            \"productionStatus\": \"ACTIVE\",\n            \"lastModifiedTime\": \"2018-01-18T00:00:00Z\",\n            \"matchLocations\": [\n                \"/rules/behaviors/0/options/hostname\"\n            ]\n        }\n    ]\n}\n",
      "language": "json"
    }
  ]
}
[/block]
Check the `searchTargetStatus` value:

- If it's either `PENDING` or `IN_PROGRESS`, the search `results`
aren't yet finalized.  Wait some time, then run the GET operation
again to poll the result.

- Once it's `COMPLETE`, search results are ready.  The amount of time
it takes to get a set of `COMPLETE` results depends on the number of
properties you're searching, the size of the configuration, and the
complexity of the `match` expression.

The `results` include up to three versions for each `propertyId`:

- active on the staging network
- active on the production network
- most recently modified version

This simplified example features only two search results:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"bulkSearchId\": 5,\n    \"searchTargetStatus\": \"COMPLETE\",\n    \"searchSubmitDate\": \"2018-01-18T00:00:00Z\",\n    \"searchUpdateDate\": \"2018-01-18T00:01:00Z\",\n    \"bulkSearchQuery\": {\n        \"syntax\": \"JSONPATH\",\n        \"match\": \"$.behaviors[?(@.name == 'origin')].options[?(@.hostname == 'old.example.com')].hostname\"\n    },\n    \"results\": [\n        {\n            \"propertyId\": \"prp_1\",\n            \"propertyVersion\": 1,\n            \"stagingStatus\": \"ACTIVE\",\n            \"productionStatus\": \"INACTIVE\",\n            \"lastModifiedTime\": \"2018-01-18T00:00:00Z\",\n            \"matchLocations\": [\n                \"/rules/behaviors/0/options/hostname\"\n            ]\n        },\n        {\n            \"propertyId\": \"prp_15\",\n            \"propertyVersion\": 2,\n            \"stagingStatus\": \"INACTIVE\",\n            \"productionStatus\": \"ACTIVE\",\n            \"lastModifiedTime\": \"2018-01-18T00:00:00Z\",\n            \"matchLocations\": [\n                \"/rules/behaviors/0/options/hostname\"\n            ]\n        }\n    ]\n}\n",
      "language": "json"
    }
  ]
}
[/block]
The `matchLocations` provides a set of [JSON
Pointer](https://tools.ietf.org/html/rfc6901) values, whose path
expressions locate where within the rules the `old.example.com` value
appears. This example shows a single match location. Other types of
search may yield additional matches within the configuration.


[block:callout]
{
  "type": "success",
  "body": "The `matchLocations` included in the search results don't\nindicate the current value at each location. If you intend to use the\nsearch results to bulk-update your configurations, compare them to the\noriginally specified `match` to confirm the scope of your initial\nsearch is what you intend."
}
[/block]
You can use bulk search simply as a research tool, using the
`propertyId` and `propertyVersion` values to [modify individual
configurations](#getpropertyversionrules).

Assuming you want to update the configurations, save the `results`
array, which you'll need to bulk patch them.  If you want to update
currently active versions, you first need to use the data to create a
new set of editable property versions.
[block:callout]
{
  "type": "info",
  "body": "As an alternative to the two-step asynchronous bulk search\noperations, you can also run a single operation:\n[Synchronously bulk search a set of properties](#postbulksearchessynchronus).\nYou POST the same initial request to a different\n`/papi/v0/bulk/rules-search-requests-synch` URL endpoint. It yields\nthe same response object as the GET, but with potentially long\nlatency for the entire set of search results to `COMPLETE`.  It's more\nappropriate to run for small-batch bulk searches."
}
[/block]