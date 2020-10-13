---
title: "dnsPrefresh"
slug: "dnsprefresh"
hidden: false
createdAt: "2020-06-15T21:14:30.765Z"
updatedAt: "2020-06-15T21:14:30.765Z"
---
__Property Manager name__: [DNS Prefresh](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0034)

A [read-only behavior](#ro) that allows edge servers to refresh your origin's DNS record independently from end-user requests. The _type A_ DNS record refreshes before the origin's DNS record expires.

__Options__:

<div class="option" markdown="1" id="dnsPrefresh.enabled" >

- `enabled` (_boolean_): When enabled, allows edge servers to refresh DNS records before they expire.

</div>

<div class="option" markdown="1" id="dnsPrefresh.delay" >

- `delay` (_duration string_): Specifies the amount of time following a DNS record's expiration to asynchronously prefresh it.

</div>

<div class="option" markdown="1" id="dnsPrefresh.timeout" >

- `timeout` (_duration string_): Specifies the amount of time to prefresh a DNS entry if there have been no requests to the domain name.

</div>

</div>

<div class="feature" data-feature="downgradeProtocol" markdown="1">
