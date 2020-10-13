---
title: "Bulk search a set of properties"
slug: "post_bulk-rules-search-requests"
excerpt: "POST a\n[BulkSearch](#bulksearch) object to search across all active\nproperty versions, specifying a\n[JSONPath](http://goessner.net/articles/JsonPath/) expression to\nmatch their rule trees. This operation launches an asynchronous\nprocess to gather search results. To check its progress, run the\n[List bulk search results](#getbulksearch) operation, whose link\nis available in the `Location` header or the `bulkSearchLink`\nmember of this operation's response. After gathering completed\nresults, you can create new property versions, bulk patch the\nrule trees, then activate them. See\n[Bulk Search and Update](#bulksearchandupdate)\nfor guidance on this feature.\nRun [Synchronously bulk search a set of\nproperties](#postbulksearchessynchronus) as an alternative to\nget completed search results directly.\nTo perform simpler\nsearches for a property's name or hostnames to which it applies,\nrun the [Search properties](#postfindbyvalue) operation instead."
hidden: false
createdAt: "2020-06-05T15:07:19.079Z"
updatedAt: "2020-06-05T15:07:19.079Z"
---
