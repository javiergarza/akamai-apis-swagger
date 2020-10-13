---
title: "List bulk-patched properties"
slug: "get_bulk-rules-patch-requests-bulkpatchid"
excerpt: "List all modified property versions that result from a [bulk patch](https://papi-akamai.readme.io/reference/bulkrules-patch-requests#post_bulk-rules-patch-requests) request, and poll the asynchronous process's status. The response is a [BulkPatch](#bulkpatch) object. Once the overall `bulkPatchStatus` is `COMPLETE`, you can feed all successfully updated property versions whose `status` is `UPDATED` into a subsequent request to [bulk activate](https://papi-akamai.readme.io/reference/bulkactivations#post_bulk-activations) them. See [Bulk Search and Update](doc:learn-about-bulk) for overall guidance on this feature."
hidden: false
createdAt: "2020-06-05T15:08:03.575Z"
updatedAt: "2020-06-10T13:51:29.185Z"
---
