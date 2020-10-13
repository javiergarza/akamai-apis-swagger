---
title: "Sample workflow"
slug: "sample-workflow"
hidden: false
createdAt: "2020-06-05T17:42:09.732Z"
updatedAt: "2020-06-05T17:42:09.732Z"
---
This simplified workflow provides pointers to more detailed steps below:

1. [Prepare a bulk search request](#prepareasearch) by specifying a
search expression.  Optionally specify additional searches to [reduce
the set of search results](#qualifyasearch).

1. [Launch the bulk search](#launchasearch), storing the response's
search ID.

1. Use the ID to [check the search results](#checksearchresults),
repeating if they're not yet complete. The results include any active
property version, along with the most recently modified version if
inactive.

1. If you want to further update a set of property versions that are
active, [bulk-create a new set of versions](#bv) and store the new set
of version numbers from the completed results.

1. Use data from the search results and any newly created version
numbers to form a bulk patch request. Specify a replacement value as
part of the patch.

1. Launch a request to [patch all the configurations](#bp), storing
the response's patch ID.

1. Use the patch ID to
[check the patch results](#checkbulkpatchstatus), repeating if they're
not yet complete.

1. Use the property IDs and versions from the bulk patch results to
launch a [bulk activation](#ba), storing the response's activation ID.

Once you confirm the bulk activation is complete, your updated
properties are live.