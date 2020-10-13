---
title: "cacheKeyQueryParams"
slug: "cachekeyqueryparams"
hidden: false
createdAt: "2020-06-15T20:50:10.394Z"
updatedAt: "2020-06-15T20:50:10.394Z"
---
__Property Manager name__: [Cache Key Query Parameters](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0022)

By default, cache keys are formed as URLs with full query strings. This behavior allows you to consolidate cached objects based on specified sets of query parameters.

Note also that whenever you apply behavior that generates new cache keys, your origin server may experience traffic spikes before the new cache starts to serve out.

__Options__:

<div class="option" markdown="1" id="cacheKeyQueryParams.behavior" >

- `behavior` (_enum string_): Configures how sets of query string parameters translate to cache keys:

    - `IGNORE_ALL` causes query string parameters to be ignored when     forming cache keys.
    - `IGNORE` or `INCLUDE` makes the key depend on the sequence of     values in the `parameters`     field.
    - `INCLUDE_ALL_PRESERVE_ORDER` forms a separate key for the entire     set of query parameters, but sensitive to the order in which they     appear. (For example, `?q=akamai&state=ma` and     `?state=ma&q=akamai` cache separately.)
    - `INCLUDE_ALL_ALPHABETIZE_ORDER` forms keys for the entire set of     parameters, but the order doesn't matter. The examples above     both use the same cache key.

    Be careful when applying `behavior`
    not to ignore any parameters that result in substantially different
    content, as it is _not_ reflected in the cached object.

</div>

<div class="option" markdown="1" id="cacheKeyQueryParams.parameters" >

- `parameters` (_array of string values_): With `behavior` set to `INCLUDE` or `IGNORE`, `parameters` specifies the set of parameter field names to include in or exclude from the cache key. By default, these match the field names as string prefixes.

</div>

<div class="option" markdown="1" id="cacheKeyQueryParams.exactMatch" >

- `exactMatch` (_boolean_): When enabled, `parameters` must match exactly. Keep disabled to match string prefixes.

</div>

</div>

<div class="feature" data-feature="cacheKeyRewrite" markdown="1">
