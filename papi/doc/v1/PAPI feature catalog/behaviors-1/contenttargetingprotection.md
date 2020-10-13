---
title: "contentTargetingProtection"
slug: "contenttargetingprotection"
hidden: false
createdAt: "2020-06-15T21:02:21.710Z"
updatedAt: "2020-06-15T21:02:21.710Z"
---
__Property Manager name__: [Content Targeting - Protection](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5003)

Content Targeting is based on [EdgeScape](https://developer.akamai.com/edgescape), Akamai's location-based access control system.  You can use it to allow or deny access to a set of geographic regions or IP addresses.

__Options__:

<div class="option" markdown="1" id="contentTargetingProtection.enabled" >

- `enabled` (_boolean_): Enables the Content Targeting feature.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.enableGeoProtection" >

- `enableGeoProtection` (_boolean_): When enabled, verifies IP addresses are unique to specific geographic regions.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.geoProtectionMode" >

- `geoProtectionMode` (_enum string_): With `enableGeoProtection` enabled, specifies whether to `ALLOW` or `DENY` requests.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.countries" >

- `countries` (_array of string values_): With `enableGeoProtection` enabled, specifies a set of two-character ISO 3166 country codes from which to allow or deny traffic. See [EdgeScape Data Codes](https://control.akamai.com/portal/content/akaServiceSupport/edgescape/shared/ES_datacodes.jsp) for a list.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.regions" >

- `regions` (_array of string values_): With `enableGeoProtection` enabled, specifies a set of ISO 3166-2 regional codes from which to allow or deny traffic. See [EdgeScape Data Codes](https://control.akamai.com/portal/content/akaServiceSupport/edgescape/shared/ES_datacodes.jsp) for a list.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.dmas" >

- `dmas` (_array of string values_): With `enableGeoProtection` enabled, specifies the set of Designated Market Area codes from which to allow or deny traffic.  See [EdgeScape Data Codes](https://control.akamai.com/portal/content/akaServiceSupport/edgescape/shared/ES_datacodes.jsp) for a list.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.overrideIPAddresses" >

- `overrideIPAddresses` (_array of string values_): With `enableGeoProtection` enabled, specify a set of IP addresses or CIDR blocks that exceptions to the set of included or excluded areas.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.enableGeoRedirectOnDeny" >

- `enableGeoRedirectOnDeny` (_boolean_): When enabled, redirects denied requests rather than responding with an error code.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.geoRedirectUrl" >

- `geoRedirectUrl` (_string_): With `enableGeoRedirectOnDeny` enabled, this specifies the full URL to the redirect page for denied requests.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.enableIPProtection" >

- `enableIPProtection` (_boolean_): When enabled, allows you to control access to your content from specific sets of IP addresses and CIDR blocks.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.ipProtectionMode" >

- `ipProtectionMode` (_enum string_): With `enableIPProtection` enabled, specifies whether to `ALLOW` or `DENY` requests.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.ipAddresses" >

- `ipAddresses` (_array of string values_): With `enableIPProtection` enabled, specify a set of IP addresses or CIDR blocks to allow or deny.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.enableIPRedirectOnDeny" >

- `enableIPRedirectOnDeny` (_boolean_): When enabled, redirects denied requests rather than responding with an error code.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.ipRedirectUrl" >

- `ipRedirectUrl` (_string_): With `enableIPRedirectOnDeny` enabled, this specifies the full URL to the redirect page for denied requests.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.enableReferrerProtection" >

- `enableReferrerProtection` (_boolean_): When enabled, allows you allow traffic from certain referring websites, and disallow traffic from unauthorized sites that hijack those links.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.referrerProtectionMode" >

- `referrerProtectionMode` (_enum string_): With `enableReferrerProtection` enabled, specify whether to `ALLOW` or `DENY` traffic from specified domains.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.referrerDomains" >

- `referrerDomains` (_array of string values_): With `enableReferrerProtection` enabled, specifies the set of domains from which to allow or deny traffic.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.enableReferrerRedirectOnDeny" >

- `enableReferrerRedirectOnDeny` (_boolean_): When enabled, redirects denied requests rather than responding with an error code.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.referrerRedirectUrl" >

- `referrerRedirectUrl` (_string_): With `enableReferrerRedirectOnDeny` enabled, this specifies the full URL to the redirect page for denied requests.

</div>

</div>

<div class="feature" data-feature="corsSupport" markdown="1">
