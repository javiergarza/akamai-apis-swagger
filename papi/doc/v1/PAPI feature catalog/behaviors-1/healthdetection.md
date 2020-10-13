---
title: "healthDetection"
slug: "healthdetection"
hidden: false
createdAt: "2020-06-15T21:28:13.151Z"
updatedAt: "2020-06-15T21:28:13.151Z"
---
__Property Manager name__: [Origin Health Detection](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0113)

Monitors the health of your origin server by tracking unsuccessful attempts to contact it. Use this behavior to keep end users from having to wait several seconds before a forwarded request times out, or to reduce requests on the origin server when it is unavailable.

When client requests are forwarded to the origin, the edge server tracks the number of attempts to connect to each IP address. It cycles through IP addresses in least-recently-tested order to avoid hitting the same one twice in a row. If the number of consecutive unsuccessful tests reaches a threshold you specify, the behavior identifies the address as faulty and stops sending requests. The edge server returns an error message to the end user or else triggers any [`failAction`](#failaction) behavior you specify.

__Options__:

<div class="option" markdown="1" id="healthDetection.retryCount" >

- `retryCount` (_number_): The number of consecutive connection failures that mark an IP address as faulty.

</div>

<div class="option" markdown="1" id="healthDetection.retryInterval" >

- `retryInterval` (_duration string_): Specifies the amount of time the edge server will wait before trying to reconnect to an IP address it has already identified as faulty.

</div>

<div class="option" markdown="1" id="healthDetection.maximumReconnects" >

- `maximumReconnects` (_number_): Specifies the maximum number of times the edge server will contact your origin server. If your origin is associated with several IP addresses, `maximumReconnects` effectively overrides the value of `retryCount`.

</div>

</div>

<div class="feature" data-feature="http2" markdown="1">
