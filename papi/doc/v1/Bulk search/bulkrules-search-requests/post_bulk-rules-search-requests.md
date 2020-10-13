---
title: "Bulk search a set of properties"
slug: "post_bulk-rules-search-requests"
excerpt: "POST a\n[BulkSearch](#bulksearch) object to search across all active\nproperty versions, specifying a\n[JSONPath](http://goessner.net/articles/JsonPath/) expression to\nmatch their rule trees. This operation launches an asynchronous\nprocess to gather search results. To check its progress, run the\n[List bulk search results](https://papi-akamai.readme.io/reference/bulkrules-search-requestsbulksearchid#get_bulk-rules-search-requests-bulksearchid) operation, whose link\nis available in the `Location` header or the `bulkSearchLink`\nmember of this operation's response. After gathering completed\nresults, you can create new property versions, bulk patch the\nrule trees, then activate them. See\n[Bulk Search and Update](doc:learn-about-bulk)\nfor guidance on this feature.\nRun [Synchronously bulk search a set of\nproperties](https://papi-akamai.readme.io/reference/bulkrules-search-requests#post_bulk-rules-search-requestssynchronus) as an alternative to\nget completed search results directly.\nTo perform simpler\nsearches for a property's name or hostnames to which it applies,\nrun the [Search properties](https://papi-akamai.readme.io/reference/searchfind-by-value#post_search-find-by-value) operation instead."
hidden: false
createdAt: "2020-06-05T15:07:19.079Z"
updatedAt: "2020-06-08T20:20:21.384Z"
---
