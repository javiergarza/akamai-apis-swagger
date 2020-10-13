---
title: "List bulk-versioned properties"
slug: "get_bulk-property-version-creations-bulkcreateid"
excerpt: "List all new property versions that result from a [bulk versioning request](https://papi-akamai.readme.io/reference/bulkproperty-version-creations#post_bulk-property-version-creations), and poll the asynchronous process's status. The response is a [BulkVersion](#bulkversion) GET object. After the `bulkCreateVersionsStatus` is `COMPLETE`, use the new version numbers along with search paths from a [bulk search](https://papi-akamai.readme.io/reference/bulkrules-search-requests#post_bulk-rules-search-requests) operation to [bulk patch](https://papi-akamai.readme.io/reference/bulkrules-patch-requests#post_bulk-rules-patch-requests) them. See [Bulk Search and Update](doc:learn-about-bulk) for guidance."
hidden: false
createdAt: "2020-06-05T15:07:48.785Z"
updatedAt: "2020-06-10T13:51:31.534Z"
---
