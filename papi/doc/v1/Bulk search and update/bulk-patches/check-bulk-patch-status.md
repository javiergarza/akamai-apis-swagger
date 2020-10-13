---
title: "Check bulk patch status"
slug: "check-bulk-patch-status"
hidden: false
createdAt: "2020-06-05T18:02:38.096Z"
updatedAt: "2020-06-11T13:00:53.822Z"
---
Once you have launched a bulk patch request, GET the response's `bulkPatchLink` URL to check on progress.  For details on this operation, see [List bulk-patched properties](#getbulkpatches):

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"bulkPatchId\": 7,\n    \"bulkPatchStatus\": \"COMPLETE\",\n    \"bulkPatchSubmitDate\": \"2018-01-18T00:00:00Z\",\n    \"bulkPatchUpdateDate\": \"2018-01-18T01:00:00Z\",\n    \"patchPropertyVersions\": [\n        {\n            \"propertyId\": \"prp_15\",\n            \"propertyVersion\": 3,\n            \"etag\": \"343410c585cf67fc\",\n            \"status\": \"UPDATED\",\n            \"patchSubmitDate\": \"2018-01-18T00:00:00Z\",\n            \"patchUpdateDate\": \"2018-01-18T00:00:00Z\",\n            \"propertyVersionRulesLink\": \"/papi/v1/properties/prp_1/versions/1/rules\",\n            \"patches\": [\n                {\n                    \"op\": \"replace\",\n                    \"path\": \"/rules/behaviors/0/options/hostname\",\n                    \"value\": \"new.example.com\"\n                }\n            ]\n        },\n        {\n            \"propertyId\": \"prp_3\",\n            \"propertyVersion\": 11,\n            \"status\": \"FATAL_ERROR\",\n            \"patchSubmitDate\": \"2018-01-18T00:00:00Z\",\n            \"patchUpdateDate\": \"2018-01-18T00:00:00Z\",\n            \"fatalError\": \"BAD SYNTAX UNABLE TO SAVE\",\n            \"patches\": [\n                {\n                    \"op\": \"replace\",\n                    \"path\": \"/rules/behaviors/0/options/hostname\",\n                    \"value\": \"new.example.com\"\n                }\n            ]\n        }\n    ]\n}\n",
      "language": "json"
    }
  ]
}
[/block]

Following the same pattern of other asynchronous responses, the response reflects back the original set of requested `patchPropertyVersions`, but with additional `status` for each property version's update progress.  The `bulkPatchStatus` reflects the status of the overall bulk patch process.  If its value isn't yet `COMPLETE` when you poll the operation, wait some time and call the operation again later.

[block:callout]
{
  "type": "success",
  "body": "Once you complete a single bulk patch operation, you can run additional bulk searches to update other values. From the search results, remove any active property versions. Doing so confines further updates to the set you just modified."
}
[/block]