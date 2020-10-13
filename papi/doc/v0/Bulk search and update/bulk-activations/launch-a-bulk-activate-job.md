---
title: "Launch a bulk activate job"
slug: "launch-a-bulk-activate-job"
hidden: false
createdAt: "2020-06-05T18:06:13.036Z"
updatedAt: "2020-06-05T20:22:34.065Z"
---
Build a [BulkActivation](#bulkactivation) POST object as in the
example below.  From the set of `patchPropertyVersions` you updated
earlier, pass in this data:

- `propertyId`
- `propertyVersion`
- optional `etag` value
- any `note` you want to include for each property's activation
- the `network` to activate on, either `STAGING` or `PRODUCTION`
[block:callout]
{
  "type": "success",
  "body": "Bulk activate to `STAGING` and test thoroughly on more than\none property before bulk activating to `PRODUCTION`."
}
[/block]
In addition to the properties you want to activate, you also need to
specify global settings that apply to all the activations. Specify
these `defaultActivationSettings`:

- a common set of `notifyEmails` to inform people of changes to
activation status.

- `"acknowledgeAllWarnings":true` if configurations include any
routine warnings.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"defaultActivationSettings\": {\n        \"acknowledgeAllWarnings\": true,\n        \"notifyEmails\": [\n            \"you@example.com\",\n            \"them@example.com\"\n        ]\n    },\n    \"activatePropertyVersions\": [\n        {\n            \"propertyId\": \"prp_15\",\n            \"propertyVersion\": 3,\n            \"note\": \"Testing new origin host for 'prp_15' v3\",\n            \"network\": \"STAGING\"\n        },\n        {\n            \"propertyId\": \"prp_3\",\n            \"propertyVersion\": 11,\n            \"note\": \"Testing new origin host for 'prp_3' v11\",\n            \"network\": \"STAGING\"\n        }\n    ]\n}\n",
      "language": "json"
    }
  ]
}
[/block]
Once you've built the [BulkActivation](#bulkactivation) object as in
this example, POST it to this URL:

```
POST /papi/v0/bulk/activations
```

For details on this operation, see [Bulk activate a set of
properties](#postbulkpropertyactivations)

As with all bulk POST operations, the response object includes a URL
link to poll for status on the activations.  This `bulkActivationLink`
is also available in the response's `Location` header:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"bulkActivationLink\": \"/papi/v0/bulk/activations/311\"\n}",
      "language": "json"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "You're limited to 100 activations for both the staging\nand production networks for each day within an account. Make sure your\nbulk activation request doesn't exceed that limit, which includes\nconventional non-bulk activation requests over the same period. See\n[Rate and resource limiting](#ratelimiting) for details."
}
[/block]