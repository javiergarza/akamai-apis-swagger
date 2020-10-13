---
title: "simulateErrorCode"
slug: "simulateerrorcode"
hidden: false
createdAt: "2020-06-15T22:02:50.386Z"
updatedAt: "2020-06-15T22:02:50.386Z"
---
__Property Manager name__: [Simulate Error Response Code](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9048)

A [read-only behavior](#ro) that simulates various error response codes. Contact Akamai Professional Services for help configuring it.

__Options__:

<div class="option" markdown="1" id="simulateErrorCode.errorType" >

- `errorType` (_enum string_): Specifies the type of error, any of the following:

<pre style="-webkit-column-width:3in;-moz-column-width:3in;column-width:3in;margin-left:3pc">
 ERR_CONNECT_FAIL
 ERR_CONNECT_TIMEOUT
 ERR_DNS_FAIL
 ERR_DNS_IN_REGION
 ERR_DNS_TIMEOUT
 ERR_NO_GOOD_FWD_IP
 ERR_READ_ERROR
 ERR_READ_TIMEOUT
 ERR_SUREROUTE_DNS_FAIL
 ERR_WRITE_ERROR
</pre>

</div>

<div class="option" markdown="1" id="simulateErrorCode.timeout" >

- `timeout` (_duration string_): When the `errorType` is `ERR_CONNECT_TIMEOUT`, `ERR_DNS_TIMEOUT`, `ERR_SUREROUTE_DNS_FAIL`, or `ERR_READ_TIMEOUT`, generates an error after the specified amount of time from the initial request.

</div>

</div>

<div class="feature" data-feature="siteShield" markdown="1">
