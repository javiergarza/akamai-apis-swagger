---
title: "fastInvalidate"
slug: "fastinvalidate"
hidden: false
createdAt: "2020-06-15T21:23:53.841Z"
updatedAt: "2020-06-15T21:23:53.841Z"
---
__Property Manager name__: [Fast Invalidate](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9076)

Applies Akamai's _Fast Purge_ feature to selected edge content, invalidating it within approximately five seconds.  This behavior sends an `If-Modified-Since` request to the origin for subsequent requests, replacing it with origin content if its timestamp is more recent. Otherwise if the origin lacks a `Last-Modified` header, it sends a simple GET request. Note that this behavior does not simply delete content if more recent origin content is unavailable.  See the [Fast Purge API](https://learn.akamai.com/en-us/api/core_features/fast_purge/v3.html) for an independent way to invalidate selected sets of content, and for more information on the feature.

__Options__:

<div class="option" markdown="1" id="fastInvalidate.enabled" >

- `enabled` (_boolean_): When enabled, forces a validation test for all edge content to which the behavior applies.

</div>

</div>

<div class="feature" data-feature="firstPartyMarketing" markdown="1">
