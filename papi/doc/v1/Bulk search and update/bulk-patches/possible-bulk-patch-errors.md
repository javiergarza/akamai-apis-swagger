---
title: "Possible bulk patch errors"
slug: "possible-bulk-patch-errors"
hidden: false
createdAt: "2020-06-05T18:03:51.078Z"
updatedAt: "2020-06-11T13:00:53.943Z"
---
Once the `bulkPatchStatus` of the bulk patch's GET response is `COMPLETE`, there may still be problems with individual updates.  For each object in the `patchPropertyVersions` array, check the `patchPropertyVersionStatus` value:

- If it's `FATAL_ERROR`, something prevented the property from updating, and an additional `fatalError` member provides guidance. The problem may be caused by invalid JSON Patch syntax, an invalid replacement value, or a mismatching `etag` digest.

    In the example discussed above, patching in a replacement `value`     that's not a valid hostname would cause a fatal error.

- If it's `UPDATED`, and no `papiWarnings` or `papiErrors` are present, you can go ahead and activate the property as discussed in the next section.

- If it's `UPDATED` but there's a `papiErrors` array, the property was saved, but you can't activate it in its current state with errors present.  Either modify each configuration individually to remove the error, or remove them from the batch to activate.

- If it's `UPDATED` but there's a `papiWarnings` and with no accompanying `papiErrors`, you can activate the property in the next step by acknowledging all the warnings. Warnings don't necessarily indicate an actual problem.  You can GET the `propertyVersionRulesLink` URL and scrutinize the `warnings` from the configuration to research the issue.

For details on the range of errors and warnings that may appear in PAPI configurations, see the [Errors](#errors) section.