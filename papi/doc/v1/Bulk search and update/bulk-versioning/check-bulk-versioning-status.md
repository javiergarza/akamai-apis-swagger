---
title: "Check bulk versioning status"
slug: "check-bulk-versioning-status"
hidden: false
createdAt: "2020-06-05T17:54:24.032Z"
updatedAt: "2020-06-10T03:12:16.820Z"
---
Go ahead and GET the URL from the step above.  The GET response reflects back all the originally requested set of `createPropertyVersions`, but filled out with more data:

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"bulkCreateId\": 9,\n    \"bulkCreateVersionsStatus\": \"IN_PROGRESS\",\n    \"bulkCreateVersionSubmitDate\": \"2018-01-18T00:00:00Z\",\n    \"bulkCreateVersionUpdateDate\": null,\n    \"createPropertyVersions\": [\n        {\n            \"propertyId\": \"prp_15\",\n            \"createFromVersion\": 2,\n            \"createFromVersionEtag\": \"343410c585cf67fc\",\n            \"propertyVersion\": 3,\n            \"createVersionStatus\": \"CREATING\",\n            \"propertyVersionLink\": null,\n            \"etag\": null,\n            \"createVersionSubmitDate\": \"2018-01-18T00:00:00Z\",\n            \"createVersionUpdateDate\": null\n        },\n        {\n            \"propertyId\": \"prp_3\",\n            \"createFromVersion\": 10,\n            \"createFromVersionEtag\": \"6c7v5c65c6cvcv65\",\n            \"propertyVersion\": 11,\n            \"createVersionsStatus\": \"CREATED\",\n            \"propertyVersionLink\": \"/papi/v1/properties/prp_3/versions/11?contractId=1-1TJZFW&groupId=15166\",\n            \"etag\": \"3333333c33cc333\",\n            \"createVersionSubmitDate\": \"2018-01-18T00:00:00Z\",\n            \"createVersionUpdateDate\": \"2018-01-18T00:00:00Z\"\n        }\n    ]\n}\n",
      "language": "json"
    }
  ]
}
[/block]

Just like the initial bulk search request, you may again need to wait for the entire bulk versioning job to complete.  Check the top-level `bulkCreateVersionsStatus` for a value of `COMPLETE`.  If it's not yet ready, run the operation again later.

For all newly created versions:

- Map the original `createFromVersion` to the newly created `propertyVersion`, for use in the subsequent bulk patch operation. Note that the version number isn't necessarily incremented.

- Optionally store the new version's `etag` value.  Including this value in the subsequent bulk patch operation ensures that your update doesn't overwrite anyone else's changes. To avoid the issue, make sure to first inform anyone else who may modify the properties that you want to bulk update them.