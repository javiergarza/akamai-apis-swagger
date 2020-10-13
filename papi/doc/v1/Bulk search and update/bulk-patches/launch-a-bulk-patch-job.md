---
title: "Launch a bulk patch job"
slug: "launch-a-bulk-patch-job"
hidden: false
createdAt: "2020-06-05T17:56:07.219Z"
updatedAt: "2020-06-10T03:23:16.996Z"
---
Review the `results` array from the earlier bulk search GET response. You'll need to build a simple [JSON Patch](http://jsonpatch.com) operation for each of the `matchLocations`, and apply it to the newly created version:

[block:code]
{
  "codes": [
    {
      "code": "[\n    {\n        \"propertyId\": \"prp_1\",\n        \"propertyVersion\": 1,\n        \"stagingStatus\": \"ACTIVE\",\n        \"productionStatus\": \"INACTIVE\",\n        \"lastModifiedTime\": \"2018-01-18T00:00:00Z\",\n        \"matchLocations\": [\n            \"/rules/behaviors/0/options/hostname\"\n        ]\n    },\n    {\n        \"propertyId\": \"prp_15\",\n        \"propertyVersion\": 2,\n        \"stagingStatus\": \"INACTIVE\",\n        \"productionStatus\": \"ACTIVE\",\n        \"lastModifiedTime\": \"2018-01-18T00:00:00Z\",\n        \"matchLocations\": [\n            \"/rules/behaviors/0/options/hostname\"\n        ]\n    }\n]\n",
      "language": "json"
    }
  ]
}
[/block]

Create a new [BulkPatch](#bulkpatch) POST request, as in the example below.  For each pairing of property ID and version from the original results, specify an object with:

- the `propertyId`.

- the newly created `propertyVersion` number, or the original value if no versioning was necessary.

- an optional `etag` for any bulk-versioned properties.

From the property ID and version pairings in the original search `results`, you need the JSON pointer expressions that appear in the `matchLocations` to build a series of `patches` with corresponding JSON Patch operations.  Pass in the original value from the `matchLocations` as the `path`.  Also specify the new `value` you want to change it to.  Specify the JSON Patch operation (`op`) as `replace`:

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"patchPropertyVersions\": [\n        {\n            \"propertyId\": \"prp_15\",\n            \"propertyVersion\": 3,\n            \"etag\": \"343410c585cf67fc\",\n            \"patches\": [\n                {\n                    \"op\": \"replace\",\n                    \"path\": \"/rules/behaviors/0/options/hostname\",\n                    \"value\": \"new.example.com\"\n                }\n            ]\n        },\n        {\n            \"propertyId\": \"prp_3\",\n            \"propertyVersion\": 11,\n            \"etag\": \"3333333c33cc333\",\n            \"patches\": [\n                {\n                    \"op\": \"replace\",\n                    \"path\": \"/rules/behaviors/0/options/hostname\",\n                    \"value\": \"new.example.com\"\n                }\n            ]\n        }\n    ]\n}\n",
      "language": "json"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "success",
  "body": "Make sure that the replacement `value` specifies the same JSON data type as the original match, or the update fails"
}
[/block]

Once you refine your set of `patches`, POST the object to this URL:

```
POST /papi/v0/bulk/rules-patch-requests
```

See [Bulk patch a set of properties](#postbulkpatch) for details on the operation.  It repeatedly invokes a lower-level [Patch a rule tree](#patchpropertyversionrules) operation, which you can use to modify an individual configuration.

Again, once you launch the bulk patch process, the response's `Location` header and JSON response object provides a navigable link to check on its progress:

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"bulkPatchLink\": \"/papi/v0/bulk/rules-patch-requests/42\"\n}\n",
      "language": "json"
    }
  ]
}
[/block]