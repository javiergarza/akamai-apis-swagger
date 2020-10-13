---
title: "largeFileOptimizationAdvanced"
slug: "largefileoptimizationadvanced"
hidden: false
createdAt: "2020-06-15T21:33:38.080Z"
updatedAt: "2020-06-15T21:33:38.080Z"
---
__Property Manager name__: [Large File Optimization](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0054)

The [Large File Optimization](http://www.akamai.com/dl/feature_sheets/fs_lfdo.pdf) feature improves performance and reliability when delivering large files. This behavior is required for objects larger than 1.8GB, and recommended for anything over 100MB. You should apply it only to the specific content to be optimized, such as a download directory's `.gz` files.  Note that it is best to use [NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html) for objects larger than 1.8GB.

This advanced behavior provides additional HTTP/2 options not present in the [`largeFileOptimization`](#largefileoptimization) behavior.

__Options__:

<div class="option" markdown="1" id="largeFileOptimizationAdvanced.enabled" >

- `enabled` (_boolean_): Enables the file optimization behavior.

</div>

<div class="option" markdown="1" id="largeFileOptimizationAdvanced.objectSize" >

- `objectSize` (_string_): Specifies the size of the file at which point to apply partial object (POC) caching. Append a numeric value with a `MB` or `GB` suffix.

</div>

<div class="option" markdown="1" id="largeFileOptimizationAdvanced.fragmentSize" >

- `fragmentSize` (_enum string_): Specifies the size of each fragment used for partial object caching, either `HALF_MB`, `ONE_MB`, `TWO_MB`, or `FOUR_MB`.

</div>

<div class="option" markdown="1" id="largeFileOptimizationAdvanced.prefetchDuringRequest" >

- `prefetchDuringRequest` (_number_): The number of POC fragments to prefetch during the request.

</div>

<div class="option" markdown="1" id="largeFileOptimizationAdvanced.prefetchAfterRequest" >

- `prefetchAfterRequest` (_number_): The number of POC fragments to prefetch after the request.

</div>

</div>

<div class="feature" data-feature="limitBitRate" markdown="1">
