---
title: "readTimeout"
slug: "readtimeout"
hidden: false
createdAt: "2020-06-15T21:48:37.744Z"
updatedAt: "2020-06-15T21:48:37.744Z"
---
__Property Manager name__: [Read Timeout](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9002)

A [read-only behavior](#ro) that specifies how long the edge server should wait for a response from the requesting forward server after a connection has already been established. Any failure to read aborts the request and sends a `504` Gateway Timeout error to the client. Contact Akamai Professional Services for help configuring this behavior.

__Options__:

<div class="option" markdown="1" id="readTimeout.value" >

- `value` (_duration string_): Specifies the read timeout necessary before failing with a `504` error. This value should never be zero.

</div>

</div>

<div class="feature" data-feature="realUserMonitoring" markdown="1">
