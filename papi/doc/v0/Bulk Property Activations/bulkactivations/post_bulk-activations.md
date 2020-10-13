---
title: "Bulk activate a set of properties"
slug: "post_bulk-activations"
excerpt: "Bulk activate a set of property versions.\n(Alternately, perform a bulk [fallback](doc:fast-validation) to the previous\nactivation within an hour of the previous bulk activation.)\nBase the set of versions to activate on the results of a\n[bulk patch](#getbulkpatches)\noperation, which you use to create a\n[BulkActivation](#bulkactivation) POST object.\nThis operation launches an asynchronous process to update\nproperties. To check its progress, run the\n[List bulk-activated properties](#getbulkpropertyactivation)\noperation, whose link is available in the `Location` header or\n`bulkActivationLink` member of this operation's response. See\n[Bulk Search and Update](#bulksearchandupdate)\nfor overall guidance on this feature."
hidden: false
createdAt: "2020-06-05T15:08:16.231Z"
updatedAt: "2020-06-05T21:52:52.937Z"
---
