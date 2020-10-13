---
title: "dnsAsyncRefresh"
slug: "dnsasyncrefresh"
hidden: false
createdAt: "2020-06-15T21:13:33.170Z"
updatedAt: "2020-06-15T21:13:33.170Z"
---
__Property Manager name__: [DNS Asynchronous Refresh](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0112)

Allow an edge server to use an expired DNS record when forwarding a request to your origin. The _type A_ DNS record refreshes _after_ content is served to the end user, so there is no wait for the DNS resolution. Avoid this behavior if you want to be able to disable a server immediately after its DNS record expires.

__Options__:

<div class="option" markdown="1" id="dnsAsyncRefresh.enabled" >

- `enabled` (_boolean_): When enabled, allows edge servers to refresh an expired DNS record after serving content.

</div>

<div class="option" markdown="1" id="dnsAsyncRefresh.timeout" >

- `timeout` (_duration string_): Set the maximum allowed time an expired DNS record may be active.

</div>

</div>

<div class="feature" data-feature="dnsPrefresh" markdown="1">
