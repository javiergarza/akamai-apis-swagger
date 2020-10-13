---
title: "downstreamCache"
slug: "downstreamcache"
hidden: false
createdAt: "2020-06-15T21:16:06.334Z"
updatedAt: "2020-06-15T21:16:06.334Z"
---
__Property Manager name__: [Downstream Cacheability](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0038)

Specify the caching instructions the edge server sends to the end user's client or client proxies. By default, the cache's duration is whichever is less: the remaining lifetime of the edge cache, or what the origin's header specifies. If the origin is set to `no-store` or `bypass-cache`, edge servers send _cache-busting_ headers downstream to prevent downstream caching.

__Options__:

<div class="option" markdown="1" id="downstreamCache.behavior" >

- `behavior` (_enum string_): Specify the caching instructions the edge server sends to the end user's client. It accepts the following values:

    - `ALLOW`: The value of `allowBehavior` chooses the caching     method and headers to send to the client.
    - `MUST_REVALIDATE`: This equates to a `Cache-Control: no-cache`     header, which allows caching but forces the client browser to send     an `if-modified-since` request each time it requests the object.
    - `BUST`: Sends cache-busting headers downstream.
    - `TUNNEL_ORIGIN`: This passes `Cache-Control` and `Expires` headers     from the origin to the downstream client.
    - `NONE`: Don't send any caching headers. Allow client browsers to     cache content according to their own default settings.

</div>

<div class="option" markdown="1" id="downstreamCache.allowBehavior" >

- `allowBehavior` (_enum string_): Specify how the edge server calculates the downstream cache by setting the value of the `Expires` header:

    - `FROM_VALUE` sends the value of the edge cache's duration.
    - `FROM_MAX_AGE` sends the `cache:max-age` value applied to the     object, without evaluating the cache's duration.
    - `LESSER` sends the lesser value of what the origin specifies and     the edge cache's remaining duration. This is the default behavior.
    - `GREATER` sends the greater value of what the origin specifies and     the edge cache's remaining duration.
    - `REMAINING_LIFETIME` sends the value of the edge cache's remaining     duration, without comparing it to the origin's headers.
    - `PASS_ORIGIN` sends the value of the origin's header, without     evaluating the edge cache's duration.

</div>

<div class="option" markdown="1" id="downstreamCache.ttl" >

- `ttl` (_duration string_): Set the duration of the cache. Setting the value to `0` equates to a `no-cache` header that forces revalidation.

</div>

<div class="option" markdown="1" id="downstreamCache.sendHeaders" >

- `sendHeaders` (_enum string_): Specifies the HTTP headers to include in the response to the client:

    - `PASS_ORIGIN` sends the same set of `Cache-Control` and `Expires`     headers received from the origin.
    - `CACHE_CONTROL` sends only the origin's `Cache-Control` header.
    - `EXPIRES` sends only the origin's `Expires` header.
    - `CACHE_CONTROL_AND_EXPIRES` sends both `Cache-Control` and `Expires` header.
    - `NONE` strips both headers.

</div>

<div class="option" markdown="1" id="downstreamCache.sendPrivate" >

- `sendPrivate` (_boolean_): When enabled, adds a `Cache-Control: private` header to prevent objects from being cached in a shared caching proxy.

</div>

</div>

<div class="feature" data-feature="dynamicAdInsertion" markdown="1">
