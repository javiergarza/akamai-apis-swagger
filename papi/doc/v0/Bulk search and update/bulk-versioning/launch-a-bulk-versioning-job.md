---
title: "Launch a bulk versioning job"
slug: "launch-a-bulk-versioning-job"
hidden: false
createdAt: "2020-06-05T17:51:59.759Z"
updatedAt: "2020-06-05T17:53:30.815Z"
---
Once you have a set of search results, create a new
[BulkVersion](#bulkversion) POST object as in this example.
Reflect each pair of `propertyId` and `propertyVersion` values from
the search `results` as `propertyId` and `createFromVersion` values
within the array:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"createPropertyVersions\": [\n        {\n            \"propertyId\": \"prp_1\",\n            \"createFromVersion\": 1\n        },\n        {\n            \"propertyId\": \"prp_15\",\n            \"createFromVersion\": 2\n        }\n    ]\n}\n",
      "language": "json"
    }
  ]
}
[/block]
POST the object to this URL:

```
POST /papi/v0/bulk/property-version-creations
```

Just like the initial bulk search request, the bulk versioning request
executes asynchronously, and its results are available in a separate
GET operation.  The link to the URL is available in the response's
`Location` header, or in the JSON response's
`bulkCreateVersionLink`. Store the value:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"bulkCreateVersionLink\": \"/papi/v0/bulk/property-version-creations/737\"\n}",
      "language": "json"
    }
  ]
}
[/block]