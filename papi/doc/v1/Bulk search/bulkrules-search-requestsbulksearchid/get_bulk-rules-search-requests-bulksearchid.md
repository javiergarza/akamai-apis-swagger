---
title: "List bulk search results"
slug: "get_bulk-rules-search-requests-bulksearchid"
excerpt: "List all property versions that result from a [bulk search request](https://papi-akamai.readme.io/reference/bulkrules-search-requests#post_bulk-rules-search-requests). Run this operation to poll the asynchronous process's status. The response is a [BulkSearch](#bulksearch) GET object. Once the `searchTargetStatus` is `COMPLETE`, you can feed the `results` into a [bulk versioning](https://papi-akamai.readme.io/reference/bulkproperty-version-creations#post_bulk-property-version-creations) operation. Also use the JSON path `matchLocations` to run a [bulk patch](https://papi-akamai.readme.io/reference/bulkrules-patch-requests#post_bulk-rules-patch-requests) operation over the rule trees. See [Bulk Search and Update](doc:learn-about-bulk) for guidance."
hidden: false
createdAt: "2020-06-05T15:07:19.081Z"
updatedAt: "2020-06-10T13:51:33.870Z"
---
