---
title: "phasedRelease"
slug: "phasedrelease"
hidden: false
createdAt: "2020-06-15T21:45:15.256Z"
updatedAt: "2020-06-15T21:45:15.256Z"
---
__Property Manager name__: [Phased Release Cloudlet](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0062)

The Phased Release Cloudlet provides gradual and granular traffic management to an alternate origin in near real time.  Use the [Cloudlets API](https://learn.akamai.com/en-us/api/web_performance/cloudlets/v2.html) or the Cloudlets Policy Manager application within [Control Center](https://control.akamai.com) to set up your Cloudlets policies.

__Options__:

<div class="option" markdown="1" id="phasedRelease.enabled" >

- `enabled` (_boolean_): Enables the Phased Release Cloudlet.

</div>

<div class="option" markdown="1" id="phasedRelease.cloudletPolicy" >

- `cloudletPolicy` (_object_): Specifies the Cloudlet policy as an object containing two members: a descriptive `name` string and an integer `id` set by the Cloudlet application.

</div>

<div class="option" markdown="1" id="phasedRelease.label" >

- `label` (_string_): A label to distinguish this Phased Release policy from any others within the same property.

</div>

<div class="option" markdown="1" id="phasedRelease.populationCookieType" >

- `populationCookieType` (_enum string_): For the population of users the Cloudlet defines, select whether to assign a cookie to them, or else `NONE`.  Other option values specify when the cookie expires: after a specific `DURATION`, at a `FIXED_DATE`, once the browser session ends (`ON_BROWSER_CLOSE`), or `NEVER`. If you select the Cloudlet's _random_ membership option, it overrides the option value so that it is effectively `NONE`.

</div>

<div class="option" markdown="1" id="phasedRelease.populationExpirationDate" >

- `populationExpirationDate` (_ISO 8601 format date/time string_): With the `populationCookieType` set to `FIXED_DATE`, this specifies the date and time when membership expires, and the browser no longer sends the cookie. Subsequent requests re-evaluate based on current membership settings.

</div>

<div class="option" markdown="1" id="phasedRelease.populationDuration" >

- `populationDuration` (_duration string_): With the `populationCookieType` set to `DURATION`, this sets the lifetime of the cookie from the initial request. Subsequent requests re-evaluate based on current membership settings.

</div>

<div class="option" markdown="1" id="phasedRelease.populationRefresh" >

- `populationRefresh` (_boolean_): With the `populationCookieType` set to `DURATION`, enabling this option resets the original duration of the cookie if the browser refreshes before the cookie expires.

</div>

<div class="option" markdown="1" id="phasedRelease.failoverEnabled" >

- `failoverEnabled` (_boolean_): Allows failure responses at the origin defined by the Cloudlet to fail over to the prevailing origin defined by the property.

</div>

<div class="option" markdown="1" id="phasedRelease.failoverResponseCode" >

- `failoverResponseCode` (_array of string values_): With `failoverEnabled` on, this defines the set of failure codes that initiate the failover response.

</div>

<div class="option" markdown="1" id="phasedRelease.failoverDuration" >

- `failoverDuration` (_number within 0-300 range_): Specifies the number of seconds to wait until the client tries to access the failover origin after the initial failure is detected. Set the value to `0` to immediately request the alternate origin upon failure.

</div>

</div>

<div class="feature" data-feature="preconnect" markdown="1">
