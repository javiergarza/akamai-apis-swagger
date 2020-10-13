---
title: "gzipResponse"
slug: "gzipresponse"
hidden: false
createdAt: "2020-06-15T21:27:27.040Z"
updatedAt: "2020-06-15T21:27:27.040Z"
---
__Property Manager name__: [Last Mile Acceleration](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0049)

Apply _gzip_ compression to speed transfer time. This behavior applies best to text-based content such as HTML, CSS, and JavaScript, especially once files exceed about 10KB. Do not apply it to already compressed image formats, or to small files that would add more time to uncompress. To apply this behavior, you should match on [`contentType`](#contenttype) or the content's [`cacheability`](#cacheability).

__Options__:

<div class="option" markdown="1" id="gzipResponse.behavior" >

- `behavior` (_enum string_): Specify when to compress responses, either `ALWAYS`, `NEVER`, or `ORIGIN_RESPONSE` to clients that send an `Accept-Encoding: gzip` header.

</div>

</div>

<div class="feature" data-feature="hdDataAdvanced" markdown="1">
