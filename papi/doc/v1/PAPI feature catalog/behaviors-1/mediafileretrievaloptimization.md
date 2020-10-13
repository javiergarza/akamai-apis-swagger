---
title: "mediaFileRetrievalOptimization"
slug: "mediafileretrievaloptimization"
hidden: false
createdAt: "2020-06-15T21:36:47.404Z"
updatedAt: "2020-06-15T21:36:47.404Z"
---
__Property Manager name__: [Media File Retrieval Optimization](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9043)

Media File Retrieval Optimization (MFRO) speeds the delivery of large media files by relying on caches of partial objects. You should use it for files larger than 100 MB. It's required for files larger than 1.8 GB, and works best with [NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html). To apply this behavior, you should match on a [`fileExtension`](#fileextension).

__Options__:

<div class="option" markdown="1" id="mediaFileRetrievalOptimization.enabled" >

- `enabled` (_boolean_): Enables the partial-object caching behavior.

</div>

</div>

<div class="feature" data-feature="mediaOriginFailover" markdown="1">
