---
title: "largeFileOptimization"
slug: "largefileoptimization"
hidden: false
createdAt: "2020-06-15T21:33:13.991Z"
updatedAt: "2020-06-15T21:33:13.991Z"
---
__Property Manager name__: [Large File Optimization](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0054)

The [Large File Optimization](http://www.akamai.com/dl/feature_sheets/fs_lfdo.pdf) feature improves performance and reliability when delivering large files. This behavior is required for objects larger than 1.8GB, and recommended for anything over 100MB. You should apply it only to the specific content to be optimized, such as a download directory's `.gz` files, and enable the `useVersioning` option while enforcing your own filename versioning policy.  Note that it is best to use [NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html) for objects larger than 1.8GB.

See also the [`largeFileOptimizationAdvanced`](#largefileoptimizationadvanced) behavior, which provides additional options for to configure partial object caching and HTTP/2 prefetching.

__Options__:

<div class="option" markdown="1" id="largeFileOptimization.enabled" >

- `enabled` (_boolean_): Enables the file optimization behavior.

</div>

<div class="option" markdown="1" id="largeFileOptimization.enablePartialObjectCaching" >

- `enablePartialObjectCaching` (_enum string_): Caches entire objects if set to `NON_PARTIAL_OBJECT_CACHING`. Otherwise when set to `PARTIAL_OBJECT_CACHING`, allows _partial-object caching_, which always applies to large objects served from [NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html). To enable this, the origin must support byte range requests.

</div>

<div class="option" markdown="1" id="largeFileOptimization.minimumSize" >

- `minimumSize` (_string_): Optimization only applies to files larger than this, expressed as a number suffixed with a unit string such as `MB` or `GB`.

</div>

<div class="option" markdown="1" id="largeFileOptimization.maximumSize" >

- `maximumSize` (_string_): Optimization does not apply to files larger than this, expressed as a number suffixed with a unit string such as `MB` or `GB`.

</div>

<div class="option" markdown="1" id="largeFileOptimization.useVersioning" >

- `useVersioning` (_boolean_): When `enablePartialObjectCaching` is set to `PARTIAL_OBJECT_CACHING`, enabling this option signals your intention to vary filenames by version, strongly recommended to avoid serving corrupt content when chunks come from different versions of the same file.

</div>

</div>

<div class="feature" data-feature="largeFileOptimizationAdvanced" markdown="1">
