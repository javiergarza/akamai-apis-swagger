---
title: "Behaviors"
slug: "behaviors"
hidden: false
createdAt: "2020-06-05T17:03:47.918Z"
updatedAt: "2020-06-05T17:16:45.659Z"
---
The default rule needs to include a set of `behaviors`,
represented as an array of objects. New properties come with different
sets of default rules depending on the product, but this much simpler
example features the two behaviors that are _always_ necessary to
activate your property. The
[`origin`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#origin)
behavior determines how the edge network interacts with your origin
servers, and you need the
[`cpCode`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#cpcode)
behavior for billing and reporting on traffic.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"rules\": {\n        \"name\": \"default\",\n        \"options\": {\n            \"is_secure\": false\n        },\n        \"behaviors\": [\n            {\n                \"name\": \"origin\",\n                \"options\": {\n                    \"originType\": \"CUSTOMER\",\n                    \"hostname\": \"example.com\",\n                    \"forwardHostHeader\": \"REQUEST_HOST_HEADER\",\n                    \"cacheKeyHostname\": \"ORIGIN_HOSTNAME\",\n                    \"compress\": true,\n                    \"tcipEnabled\": false,\n                    \"httpPort\": 80\n                }\n            },\n            {\n                \"name\": \"cpCode\",\n                \"options\": {\n                    \"value\": {\n                        \"id\": 12345,\n                        \"name\": \"main site\"\n                    }\n                }\n            }\n        ]\n    }\n}\n",
      "language": "json"
    }
  ]
}
[/block]
While nominally optional, default rules typically also specify a
[`caching`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#caching)
behavior to position the content on the edge, and a
[`report`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#report)
behavior to refine the information you receive in traffic reports.

Each behavior object is identified by a `name` field. It features a
[`locked` member](#advancedfeatures), and most require a
nested `options` object. Some behaviors only feature an `enabled`
option that toggles whether the behavior is activated, while others
require more fields once they're activated. The exact set of options
you need to specify for each behavior often varies depending on what
you're trying to do, and some options are required based on the value
of others. The
[PAPI Feature Catalog Reference]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html)
details the requirements for each option.

In the
[`origin`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#origin)
example above, the `originType` is set to `CUSTOMER`, in which case
your own server is the origin and you need to identify it with the
`hostname` field. If the `originType` were set to any other value, the
`hostname` would be unnecessary and thus ignored. PAPI silently
ignores any unexpected values, but it always warns you about any
expected values that are missing. For example, setting the
`originType` to `NET_STORAGE` would require another `netStorage`
option providing details about your NetStorage account.