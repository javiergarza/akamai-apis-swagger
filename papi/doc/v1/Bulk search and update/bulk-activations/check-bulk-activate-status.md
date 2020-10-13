---
title: "Check bulk activate status"
slug: "check-bulk-activate-status"
hidden: false
createdAt: "2020-06-05T18:08:34.912Z"
updatedAt: "2020-06-11T13:00:53.261Z"
---
GET the URL link from the response discussed above to check bulk activation progress. See [List bulk-activated properties](#getbulkpropertyactivation) for details on this operation.

As with all bulk operations, the GET response features all the original requested data, but with additional data to reflect the status of the activations.  Some of the global `defaultActivationSettings` are also repeated within each of the `activatePropertyVersions`:

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"bulkActivationId\": 234,\n    \"bulkActivationStatus\": \"NEW\",\n    \"bulkActivationSubmitDate\": \"2018-01-18T00:00:00Z\",\n    \"bulkActivationUpdateDate\": \"2018-01-18T01:00:00Z\",\n    \"defaultActivationSettings\": {\n        \"acknowledgeAllWarnings\": true,\n        \"useFastFallback\": false,\n        \"fastPush\": true,\n        \"notifyEmails\": [\n            \"you@example.com\",\n            \"them@example.com\"\n        ]\n    },\n    \"activatePropertyVersions\": [\n        {\n            \"propertyId\": \"prp_15\",\n            \"propertyVersion\": 3,\n            \"note\": \"Testing new origin host for 'prp_15' v3\",\n            \"network\": \"STAGING\",\n            \"acknowledgeAllWarnings\": true,\n            \"activationStatus\": \"ACTIVATED\",\n            \"activationSubmitDate\": \"2018-01-18T00:00:00Z\",\n            \"activationUpdateDate\": \"2018-01-18T00:00:00Z\",\n            \"fastPush\": true,\n            \"propertyActivationLink\": \"/papi/v1/properties/prp_1/activations/act_1\",\n            \"useFastFallback\": false,\n            \"notifyEmails\": [\n                \"you@example.com\",\n                \"them@example.com\"\n            ]\n        },\n        {\n            \"propertyId\": \"prp_3\",\n            \"propertyVersion\": 11,\n            \"note\": \"Testing new origin host for 'prp_3' v11\",\n            \"network\": \"STAGING\",\n            \"acknowledgeAllWarnings\": true,\n            \"activationStatus\": \"ACTIVATING\",\n            \"activationSubmitDate\": \"2018-01-18T00:00:00Z\",\n            \"activationUpdateDate\": null,\n            \"fastPush\": true,\n            \"propertyActivationLink\": \"/papi/v1/properties/prp_1/activations/act_2\",\n            \"useFastFallback\": false,\n            \"notifyEmails\": [\n                \"you@example.com\",\n                \"them@example.com\"\n            ]\n        }\n    ]\n}\n",
      "language": "json"
    }
  ]
}
[/block]

As with all of PAPI's bulk operations, the GET response's top-level object indicates the status of the overall bulk job.  If the `bulkActivationStatus` isn't yet `COMPLETE`, GET it again later. Once the `bulkActivationStatus` is `COMPLETE`, check each `activatePropertyVersions` object.  If the `activationStatus` is `ACTIVATED`, the property is serving live traffic.  Your bulk update is complete.