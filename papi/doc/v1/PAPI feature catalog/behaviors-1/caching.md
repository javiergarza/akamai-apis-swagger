---
title: "caching"
slug: "caching"
hidden: false
createdAt: "2020-06-15T20:53:51.995Z"
updatedAt: "2020-06-15T20:53:51.995Z"
---
__Property Manager name__: [Caching](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0024)

Control content caching on edge servers: whether or not to cache, whether to honor the origin's caching headers, and for how long to cache.  Note that any `NO_STORE` or `BYPASS_CACHE` HTTP headers set on the origin's content overrides this behavior.

__Options__:

<div class="option" markdown="1" id="caching.behavior" >

- `behavior` (_enum string_): Specify the caching option:

    - `NO_STORE` clears the cache and serves from the origin.
    - `BYPASS_CACHE` retains the cache but serves from the origin.
    - Honor the origin's `MAX_AGE` header
    - Honor the origin's `CACHE_CONTROL` header
    - Honor the origin's `EXPIRES` header
    - Honor `CACHE_CONTROL_AND_EXPIRES` the origin's `CACHE_CONTROL`     or `EXPIRES` header, whichever comes last.

    __Note__. New `CACHE_CONTROL_BETA` and
    `CACHE_CONTROL_AND_EXPIRES_BETA` values add support for the
    `s-maxage` response directive specified in
    [RFC 7234](https://tools.ietf.org/html/rfc7234).
    Use these alternative values to instruct a downstream CDN how long
    to cache content.

</div>

<div class="option" markdown="1" id="caching.mustRevalidate" >

- `mustRevalidate` (_boolean_): Determines what to do once the cached content has expired, by which time the Akamai platform should have re-fetched and validated content from the origin. If enabled, only allows the re-fetched content to be served. If disabled, may serve stale content if the origin is unavailable.

</div>

<div class="option" markdown="1" id="caching.ttl" >

- `ttl` (_duration string_): The maximum time content may remain cached. Setting the value to `0` is the same as setting a `no-cache` header, which forces content to revalidate.

</div>

<div class="option" markdown="1" id="caching.defaultTtl" >

- `defaultTtl` (_duration string_): Set the `MAX_AGE` header for the cached content.

</div>

<div class="option" markdown="1" id="caching.honorPrivateEnabled" >

- `honorPrivateEnabled` (_boolean_): With the `behavior` set to either `CACHE_CONTROL` or `CACHE_CONTROL_AND_EXPIRES`, enabling this instructs edge servers to honor `Cache-Control: private` headers.

</div>

<div class="option" markdown="1" id="caching.honorMustrevalidateEnabled" >

- `honorMustrevalidateEnabled` (_boolean_): With the `behavior` set to either `CACHE_CONTROL` or `CACHE_CONTROL_AND_EXPIRES`, enabling this instructs edge servers to honor `Cache-Control: must-revalidate` headers.

</div>

</div>

<div class="feature" data-feature="centralAuthorization" markdown="1">
