---
title: "Bulk version a set of properties"
slug: "post_bulk-property-version-creations"
excerpt: "POST a [BulkVersion](#bulkversion) object to create new\nversions of a set of properties based on any previous version.\nThis operation launches an asynchronous process to increment\nversions. To check its progress,\nrun the [List bulk-versioned properties](https://papi-akamai.readme.io/reference/bulkproperty-version-creationsbulkcreateid#get_bulk-property-version-creations-bulkcreateid)\noperation, whose link is available in the `Location` header or\n`bulkCreateVersionLink` member of this operation's response.\nRun this operation only after\n[bulk searching](https://papi-akamai.readme.io/reference/bulkrules-search-requests#post_bulk-rules-search-requests) a set of properties you want\nto change, to prepare new versions to bulk patch. See\n[Bulk Search and Update](doc:learn-about-bulk)\nfor guidance on this feature."
hidden: false
createdAt: "2020-06-05T15:07:48.783Z"
updatedAt: "2020-06-08T20:20:16.224Z"
---
