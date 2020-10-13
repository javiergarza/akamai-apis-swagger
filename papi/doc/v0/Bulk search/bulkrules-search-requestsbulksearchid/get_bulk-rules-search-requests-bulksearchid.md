---
title: "List bulk search results"
slug: "get_bulk-rules-search-requests-bulksearchid"
excerpt: "List all property versions that result from a [bulk search\nrequest](#postbulksearches). Run this operation to poll\nthe asynchronous process's status. The response is a\n[BulkSearch](#bulksearch) GET object. Once the\n`searchTargetStatus` is `COMPLETE`, you can feed the\n`results` into a\n[bulk versioning](#postbulkpropertyversions) operation.\nAlso use the JSON path `matchLocations` to run a\n[bulk patch](#postbulkpatch) operation over the rule\ntrees. See [Bulk Search and Update](#bulksearchandupdate)\nfor guidance."
hidden: false
createdAt: "2020-06-05T15:07:19.081Z"
updatedAt: "2020-06-05T15:07:19.081Z"
---
