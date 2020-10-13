---
title: "scheduleInvalidation"
slug: "scheduleinvalidation"
hidden: false
createdAt: "2020-06-15T21:59:18.323Z"
updatedAt: "2020-06-15T21:59:18.323Z"
---
__Property Manager name__: [Scheduled Invalidation](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9022)

Specifies when cached content that satisfies a rule's criteria expires, optionally at repeating intervals. In addition to periodic cache flushes, you can use this behavior to minimize potential conflicts when related objects expire at different times.

> __WARNING__: scheduled invalidations can significantly increase
origin servers' load when matching content expires simultaneously
across all edge servers. As best practice, schedule expirations during
periods of lowest traffic.

__Options__:

<div class="option" markdown="1" id="scheduleInvalidation.start" >

- `start` (_ISO 8601 format date/time string_): The UTC date and time when matching cached content is to expire.

</div>

<div class="option" markdown="1" id="scheduleInvalidation.repeat" >

- `repeat` (_boolean_): When enabled, invalidation recurs periodically from the `start` time based on the `repeatInterval` time.

</div>

<div class="option" markdown="1" id="scheduleInvalidation.repeatInterval" >

- `repeatInterval` (_duration string_): With `repeat` enabled, specifies how often to invalidate content from the `start` time, expressed in seconds. For example, an expiration set to midnight and an interval of `86400` seconds invalidates content once a day.  Repeating intervals of less than 5 minutes are not allowed for [NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html) origins.

</div>

<div class="option" markdown="1" id="scheduleInvalidation.refreshMethod" >

- `refreshMethod` (_enum string_): Specifies how to invalidate the content. Setting it to `INVALIDATE` sends an `If-Modified-Since` request to the origin, re-caching the content only if it is fresher. Setting it to `PURGE` re-caches content regardless of its freshness, potentially creating more traffic at the origin.

</div>

</div>

<div class="feature" data-feature="scriptManagement" markdown="1">
