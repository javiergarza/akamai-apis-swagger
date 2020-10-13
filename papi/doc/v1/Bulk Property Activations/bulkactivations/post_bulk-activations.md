---
title: "Bulk activate a set of properties"
slug: "post_bulk-activations"
excerpt: "XXX Bulk activate a set of property versions.\n(Alternately, perform a bulk [fallback](doc:fast-validation) to the previous\nactivation within an hour of the previous bulk activation.)\nBase the set of versions to activate on the results of a\n[bulk patch](https://dash.readme.com/project/papi-akamai/v1/refs/get_bulk-rules-patch-requests-bulkpatchid)\noperation, which you use to create a\n[BulkActivation](#bulkactivation) POST object.\nThis operation launches an asynchronous process to update\nproperties. To check its progress, run the\n[List bulk-activated properties](https://papi-akamai.readme.io/reference/bulkactivationsbulkactivationid#get_bulk-activations-bulkactivationid)\noperation, whose link is available in the `Location` header or\n`bulkActivationLink` member of this operation's response. See\n[Bulk Search and Update](doc:learn-about-bulk)\nfor overall guidance on this feature."
hidden: false
createdAt: "2020-06-05T15:08:16.231Z"
updatedAt: "2020-06-10T14:45:20.409Z"
---
