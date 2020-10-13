---
title: "Bulk patch a set of properties"
slug: "post_bulk-rules-patch-requests"
excerpt: "Apply a series of JSON Patch\noperations to modify a set of property versions. Form this set\nof `patches` based on the\n[JSONPath](http://goessner.net/articles/JsonPath/) locations\nfrom a [bulk search](#postbulksearches) response. Specify a set\nof new property versions based on the results of a\n[bulk versioning](#postbulkpropertyversions) operation. The\nrequest is a [BulkPatch](#bulkpatch) POST object. This\noperation launches an asynchronous process to update rule\ntrees. To check its progress, run the [List bulk-updated\nproperties](#getbulkpatches) operation, whose link is available\nin the `Location` header or `bulkPatchLink` member of this\noperation's response. See\n[Bulk Search and Update](#bulksearchandupdate)\nfor overall guidance on this feature."
hidden: false
createdAt: "2020-06-05T15:08:03.573Z"
updatedAt: "2020-06-05T15:08:03.573Z"
---
