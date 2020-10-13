---
title: "cacheError"
slug: "cacheerror"
hidden: false
createdAt: "2020-06-15T20:48:23.441Z"
updatedAt: "2020-06-15T20:48:23.441Z"
---
__Property Manager name__: [Cache HTTP Error Responses](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0020)

Caches the origin's error responses to decrease server load. Applies for 10 seconds by default to the following HTTP codes: `204`, `305`, `400`, `404`, `405`, `501`, `502`, `503`, `504`, and `505`.

__Options__:

<div class="option" markdown="1" id="cacheError.enabled" >

- `enabled` (_boolean_): When enabled, activates the error-caching behavior.

</div>

<div class="option" markdown="1" id="cacheError.ttl" >

- `ttl` (_duration string_): Overrides the default caching duration of `10s`. Note that if set to `0`, it is equivalent to `no-cache`, which forces revalidation and may cause a traffic spike. This can be counterproductive when, for example, the origin is producing an error code of `500`.

</div>

<div class="option" markdown="1" id="cacheError.preserveStale" >

- `preserveStale` (_boolean_): When enabled, the edge server preserves stale cached objects when the origin returns `400`, `500`, `502`, `503`, and `504` error codes. This avoids re-fetching and re-caching content after transient errors.

</div>

</div>

<div class="feature" data-feature="cacheId" markdown="1">
