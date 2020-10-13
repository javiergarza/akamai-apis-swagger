---
title: "cacheTagVisible"
slug: "cachetagvisible"
hidden: false
createdAt: "2020-06-15T20:53:11.029Z"
updatedAt: "2020-06-15T20:53:11.029Z"
---
__Property Manager name__: Cache Tag Visibility

Cache tags are comma-separated string values you define within an `Edge-Cache-Tag` header. You can use them to flexibly fast purge tagged segments of your cached content. You can either define these headers at the origin server level, or use the [`modifyOutgoingResponseHeader`](#modifyoutgoingresponseheader) behavior to configure them at the edge.  Apply this behavior to confirm you're deploying the intended set of cache tags to your content.

See [Fast Purge](https://learn.akamai.com/en-us/webhelp/fast-purge/fast-purge/) for guidance on best practices to deploy cache tags. Use the [Fast Purge API](https://developer.akamai.com/api/core_features/fast_purge/v3.html) to purge by cache tag programmatically.

__Options__:

<div class="option" markdown="1" id="cacheTagVisible.behavior" >

- `behavior` (_enum string_): Specify `ALWAYS` to include the `Edge-Cache-Tag` header in all responses. Specify `NEVER` to match edge servers' default response, stripping out the header.  Otherwise if you specify `PRAGMA_HEADER`, edge servers respond with the `Edge-Cache-Tag` header only when you pass in a `Pragma: akamai-x-get-cache-tags` header as part of the request.

</div>

</div>

<div class="feature" data-feature="caching" markdown="1">
