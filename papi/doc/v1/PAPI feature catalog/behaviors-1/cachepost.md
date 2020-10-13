---
title: "cachePost"
slug: "cachepost"
hidden: false
createdAt: "2020-06-15T20:51:44.663Z"
updatedAt: "2020-06-15T20:51:44.663Z"
---
__Property Manager name__: [Cache POST Responses](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9019)

By default, POST requests are passed to the origin. This behavior overrides the default, and allows you to cache POST responses.

__Options__:

<div class="option" markdown="1" id="cachePost.enabled" >

- `enabled` (_boolean_): Enables caching of POST responses.

</div>

<div class="option" markdown="1" id="cachePost.useBody" >

- `useBody` (_enum string_): Define how and whether to use the POST message body as a cache key:

    - `IGNORE` uses only the URL to cache the response.
    - `MD5` adds a string digest of the data as a query parameter to the     cache URL.
    - `QUERY` adds the raw request body as a query parameter to the     cache key, but only if the POST request's `Content-Type` is     `application/x-www-form-urlencoded`. (Use this in conjunction     with [`cacheId`](#cacheid) to define relevant query     parameters.)

</div>

</div>

<div class="feature" data-feature="cacheRedirect" markdown="1">
