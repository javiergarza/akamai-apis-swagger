---
title: "JSON problem responses"
slug: "json-problem-responses"
hidden: false
createdAt: "2020-06-05T21:06:43.081Z"
updatedAt: "2020-06-10T03:12:18.073Z"
---
API operations routinely respond with failure codes to a wide range of problems with the integrity of the data you're trying to modify, everything from malformed JSON, to missing fields, to mismatching `etags` digests. The API returns these error responses in the standard [JSON Problem](https://tools.ietf.org/html/rfc7807) format.

PAPI also serializes problems in some success responses. PAPI allows you to succeed in saving property rule or hostname data in a state that would later fail on activation, but by default it embeds guidance about each problem within the response. Two kinds of problem appear in success responses:

- An `errors` array notes any problem that would prevent activation. You need to fix these before activating the property.

- A `warnings` array notes less severe issues. You can either modify the data in response, or acknowledge the set of warnings when later activating the property.

For example, when you try to PUT a rule tree that's missing required [`origin`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#origin) and [`cpCode`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#cpcode) behaviors, a 200 response identifies them as `errors`:

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"accountId\": \"act_1-1TJZFB\",\n    \"contractId\": \"ctr_1-1TJZH5\",\n    \"groupId\": \"grp_15225\",\n    \"propertyId\": \"prp_173136\",\n    \"propertyVersion\": 3,\n    \"etag\": \"a9dfe78cf93090516bde891d009eaf57\",\n    \"errors\": [\n        {\n            \"type\": \"/papi/v0/errors/validation.required_behavior\",\n            \"title\": \"Missing required behavior in default rule\",\n            \"detail\": \"In order for this property to work correctly behavior Content Provider Code needs to be present in the default section\",\n            \"instance\": \"/papi/v0/properties/prp_173136/versions/3/rules#err_100\",\n            \"behaviorName\": \"cpCode\"\n        },\n        {\n            \"type\": \"/papi/v0/errors/validation.required_behavior\",\n            \"title\": \"Missing required behavior in default rule\",\n            \"detail\": \"In order for this property to work correctly behavior Origin needs to be present in the default section\",\n            \"instance\": \"/papi/v0/properties/prp_173136/versions/3/rules#err_101\",\n            \"behaviorName\": \"origin\"\n        }\n    ],\n    \"rules\": {\n        \"name\": \"default\",\n        \"options\": {\n            \"is_secure\": false\n        },\n        \"children\": [\n            {\n                \"name\": \"Handle /my-path\",\n                \"criteriaMustSatisfy\": \"all\",\n                \"criteria\": [\n                    {\n                        \"name\": \"wildcard\",\n                        \"value\": [\"/my-path\"]\n                    }\n                ],\n                \"behaviors\": [\n                    {\n                        \"name\": \"caching\",\n                        \"behavior\": \"MAX_AGE\",\n                        \"ttl\": \"1m\"\n                    }\n                ]\n            }\n        ]\n    }\n}\n",
      "language": "json"
    }
  ]
}
[/block]

Even though you can save the rule tree, you can't activate the property until you add the missing behaviors.

PAPI also allows you the option to skip potentially lengthy validation tests that would result in these `errors` and `warnings`. You'd still need to address the problems prior to activation, but this option allows you to modify and save data more quickly as a matter of routine throughout your development cycle. See [Fast validation, activation, and fallback](doc:fast-fallback) for more information.