---
title: "Bulk searches"
slug: "bulk-searches"
hidden: false
createdAt: "2020-06-05T17:43:35.032Z"
updatedAt: "2020-06-05T20:17:04.020Z"
---
All the steps discussed below focus on a simple task: searching for a
set of
[`origin`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#origin)
behaviors in the configuration's top-level rule, and changing the
origin server's `hostname` from `old.example.com` to `new.example.com`.
[block:callout]
{
  "type": "success",
  "body": "If you intend to use search results for a bulk update, make\nsure nobody else is modifying any of the property configurations\nbefore launching your search."
}
[/block]
This simplified object shows the type of rule you want to match,
available from the [Get a rule tree](#getpropertyversionrules)
operation's response:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"accountId\": \"act_1-1TJZFB\",\n    \"contractId\": \"ctr_1-1TJZH5\",\n    \"groupId\": \"grp_15225\",\n    \"propertyId\": \"prp_173136\",\n    \"propertyVersion\": 3,\n    \"etag\": \"a9dfe78cf93090516bde891d009eaf57\",\n    \"ruleFormat\": \"v2018-02-27\",\n    \"rules\": {\n        \"name\": \"default\",\n        \"criteria\": [],\n        \"behaviors\": [\n            {\n                \"name\": \"origin\",\n                \"options\": {\n                    \"httpPort\": 80,\n                    \"enableTrueClientIp\": false,\n                    \"compress\": true,\n                    \"cacheKeyHostname\": \"ORIGIN_HOSTNAME\",\n                    \"forwardHostHeader\": \"REQUEST_HOST_HEADER\",\n                    \"hostname\": \"old.example.com\",\n                    \"originType\": \"CUSTOMER\"\n                }\n            },\n            {\n                \"name\": \"cpCode\",\n                \"options\": {\n                    \"value\": {\n                        \"id\": 12345,\n                        \"name\": \"my CP code\"\n                    }\n                }\n            }\n        ],\n        \"children\": []\n    }\n}\n",
      "language": "json"
    }
  ]
}
[/block]