---
title: "cacheId"
slug: "cacheid"
hidden: false
createdAt: "2020-06-15T20:48:54.033Z"
updatedAt: "2020-06-15T20:48:54.033Z"
---
__Property Manager name__: [Cache ID Modification](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9050)

Controls which query parameters, headers, and cookies are included in or excluded from the cache key identifier.

Note that this behavior executes differently than usual within rule trees.  Applying a set of `cacheId` behaviors within the same rule results in a system of forming cache keys that applies independently to the rule's content.  If any `cacheId` behaviors are present in a rule, any others specified in parent rules or prior executing sibling rules no longer apply. Otherwise for any rule that lacks a `cacheId` behavior, the set of behaviors specified in an ancestor or prior sibling rule determines how to form cache keys for that content.

__Options__:

<div class="option" markdown="1" id="cacheId.rule" >

- `rule` (_enum string_): Specifies how to modify the cache ID:

    - `INCLUDE_HEADERS` includes specified HTTP headers in the cache ID.
    - `INCLUDE_COOKIES` includes specified cookies in the cache ID.
    - `INCLUDE_ALL_QUERY_PARAMS` includes all query parameters     when forming a cache ID.
    - `INCLUDE_QUERY_PARAMS` includes the specified set of     query parameters when forming a cache ID.
    - `EXCLUDE_QUERY_PARAMS` excludes the specified set of     query parameters when forming a cache ID.
    - `INCLUDE_VARIABLE` includes a specific [user variable](#vf)     in the cache ID.
    - `INCLUDE_URL` includes the full URL, the same as the default     without the `cacheid` behavior.

</div>

<div class="option" markdown="1" id="cacheId.includeValue" >

- `includeValue` (_boolean_): When enabled, includes the value of the specified elements in the cache ID. Otherwise only their names are included.

</div>

<div class="option" markdown="1" id="cacheId.optional" >

- `optional` (_boolean_): When enabled, requires the behavior's specified elements to be present for content to cache. When disabled, requests that lack the specified elements are still cached.  This option only applies when the `type` is `INCLUDE_COOKIES`, `INCLUDE_QUERY_PARAMS`, `INCLUDE_HEADERS`, or `EXCLUDE_QUERY_PARAMS`.

</div>

<div class="option" markdown="1" id="cacheId.elements" >

- `elements` (_array of string values_): Specifies the names of the query parameters, cookies, or headers to include or exclude from the cache ID. This only applies when the `rule` is `INCLUDE_COOKIES`, `INCLUDE_HEADERS`, `INCLUDE_QUERY_PARAMS`, or `EXCLUDE_QUERY_PARAMS`.

</div>

<div class="option" markdown="1" id="cacheId.variableName" >

- `variableName` (_string_): With `rule` set to `INCLUDE_VARIABLE`, specifies the name of the variable you want to include in the cache key.

</div>

</div>

<div class="feature" data-feature="cacheKeyIgnoreCase" markdown="1">
