---
title: "Sample bulk updates"
slug: "sample-bulk-updates"
hidden: false
createdAt: "2020-06-05T17:42:31.597Z"
updatedAt: "2020-06-10T03:12:17.442Z"
---
This section summarizes some of the more useful searches you may want to run, along with the [JSONPath](http://goessner.net/articles/JsonPath/) syntax needed for the bulk search request, and sample replacement values.

Most of these searches match anywhere within the configuration.  See the [Contextual searches](#contextualsearches) section if you need help searching more specific locations within the configuration. See the [PAPI Feature Catalog Reference](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html) for a full reference of all behavior and criteria options you can update within your configurations.

| Match | JSONPath search | Replacement |
| :--- | :--- | :--- |
| Default [origin](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#origin) hostname | `$.behaviors[?(@.name == 'origin')].options.hostname` | `"www.example.com"` |
| Any origin hostname set to `old.example.com` | `$..behaviors[?(@.name == 'origin')].options[?(@.hostname == 'old.example.com')].hostname` | `"new.example.com"` |
| Default [caching](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#caching) TTL | `$.behaviors[?(@.name == 'caching')].options.defaultTtl` | `"12h"` |
| Any caching TTL value other than 1 day | `$..behaviors[?(@.name == 'caching')].options[?(@.defaultTtl != '1d')].defaultTtl` | `"1d"` |
| Any [CP code](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#cpcode) | `$..behaviors[?(@.name == 'cpCode'].options.value.id` | `12345` |
| CP code set to `12345` | `$..behaviors[?(@.name == 'cpCode'].options.value[?(@.id == 12345)].id` | `54321` |
| [Edge Redirector](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#edgeredirector), enabled or disabled | `$..behaviors[?(@.name == 'edgeRedirector')].options.enabled` | `false` |
| [Forward rewrite](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#forwardrewrite), disabled | `$..behaviors[?(@.name == 'forwardRewrite'].options[?(@.enabled == false)].enabled` | `true` |
| [SureRoute](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#sureroute) test URL | `$..behaviors[?(@.name == 'sureRoute')].options.testObjectUrl` | `"/new-object"` |
| ID of [custom behavior](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#custombehavior) named `customized` | `$..behaviors[?(@.name == 'customBehavior')].options[?(@.name == 'customized')].behaviorId` | `"myCustomRedirect"` |
| Change one of the [path](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#path) match values from `/catalog` to `/shop` | `$..criteria[?(@.name == 'path')].options.value[?(@ == '/catalog')]` | `"/shop"` |

[block:callout]
{
  "type": "success",
  "body": "All JSONPath expressions evaluate within the `rules` section of a property configuration, available as JSON from PAPI's [Get a rule tree](#getpropertyversionrules) operation."
}
[/block]