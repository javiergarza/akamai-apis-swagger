---
title: "cacheKeyIgnoreCase"
slug: "cachekeyignorecase"
hidden: false
createdAt: "2020-06-15T20:49:37.081Z"
updatedAt: "2020-06-15T20:49:37.081Z"
---
__Property Manager name__: [Ignore Case In Cache Key](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0021)

By default, cache keys are generated under the assumption that path and filename components are case-sensitive, so that `File.html` and `file.html` use separate cache keys. Enabling this behavior forces URL components whose case varies to resolve to the same cache key. Enable this behavior if your origin server is already case-insensitive, such as those based on Microsoft IIS.

With this behavior enabled, make sure any child rules do not match case-sensitive path components, or you may apply different settings to the same cached object.

Note that if already enabled, disabling this behavior potentially results in new sets of cache keys. Until these new caches are built, your origin server may experience traffic spikes as requests pass through. It may also result in _cache pollution_, excess cache space taken up with redundant content.

If you are using [NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html) in conjunction with this behavior, enable its __Force Case__ option to match it, and make sure you name the original files consistently as either upper- or lowercase.

__Options__:

<div class="option" markdown="1" id="cacheKeyIgnoreCase.enabled" >

- `enabled` (_boolean_): When enabled, ignores case when forming cache keys.

</div>

</div>

<div class="feature" data-feature="cacheKeyQueryParams" markdown="1">
