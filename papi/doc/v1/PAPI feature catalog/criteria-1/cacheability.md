---
title: "cacheability"
slug: "cacheability"
hidden: false
createdAt: "2020-06-15T22:16:19.313Z"
updatedAt: "2020-06-15T22:16:19.313Z"
---
__Property Manager name__: [Response Cacheability](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches the current cache state.  Note that any `NO_STORE` or `BYPASS_CACHE` HTTP headers set on the origin's content overrides properties' [`caching`](#caching) instructions, in which case this criteria does not apply.

__Options__:

- `matchOperator` (_enum string_): When set to `IS`, matches the `value`. If set to `IS_NOT`, reverses the match so that the cache state does _not_ match the specified `value`.

- `value` (_enum string_): Content's cache is enabled (`CACHEABLE`) or not (`NO_STORE`), or else is ignored (`BYPASS_CACHE`).
