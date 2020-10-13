---
title: "List bulk-patched properties"
slug: "get_bulk-rules-patch-requests-bulkpatchid"
excerpt: "List all modified property\nversions that result from a [bulk patch](#postbulkpatch)\nrequest, and poll the asynchronous process's status. The\nresponse is a [BulkPatch](#bulkpatch) object. Once the\noverall `bulkPatchStatus` is `COMPLETE`, you can feed all\nsuccessfully updated property versions whose `status` is\n`UPDATED` into a subsequent request to\n[bulk activate](#postbulkpropertyactivations) them. See\n[Bulk Search and Update](#bulksearchandupdate)\nfor overall guidance on this feature."
hidden: false
createdAt: "2020-06-05T15:08:03.575Z"
updatedAt: "2020-06-05T15:08:03.575Z"
---
