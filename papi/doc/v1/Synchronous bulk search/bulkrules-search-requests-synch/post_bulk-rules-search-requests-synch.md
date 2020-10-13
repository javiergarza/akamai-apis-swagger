---
title: "Synchronously bulk search a set of properties"
slug: "post_bulk-rules-search-requests-synch"
excerpt: "Provides an alternative to the asynchronous [Bulk search a set of\nproperties](https://papi-akamai.readme.io/reference/bulkrules-search-requests#post_bulk-rules-search-requests) operation. It yields completed\nbulk search results directly, but with possibly high latency,\nmaking it more appropriate to target for small-batch searches.\nPOST a [BulkSearch](#bulksearch) object to search across all\nactive property versions, specifying a\n[JSONPath](http://goessner.net/articles/JsonPath/) expression to\nmatch their rule trees. After gathering results, you can create\nnew property versions, bulk patch the rule trees, then activate\nthem. See [Bulk Search and Update](doc:learn-about-bulk) for\nguidance on this feature.\nTo perform simpler searches for a property's name or hostnames\nto which it applies, run the [Search\nproperties](https://papi-akamai.readme.io/reference/searchfind-by-value#post_search-find-by-value) operation instead."
hidden: false
createdAt: "2020-06-05T15:07:35.774Z"
updatedAt: "2020-06-10T13:39:13.676Z"
---
