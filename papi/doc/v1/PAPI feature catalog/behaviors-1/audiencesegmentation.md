---
title: "audienceSegmentation"
slug: "audiencesegmentation"
hidden: false
createdAt: "2020-06-15T20:42:16.685Z"
updatedAt: "2020-06-15T20:42:16.685Z"
---
__Property Manager name__: [Audience Segmentation Cloudlet](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0018)

Allows you to divide your users into different segments based on a persistent cookie. You can configure rules using either the Cloudlets Policy Manager application or the [Cloudlets API](https://learn.akamai.com/en-us/api/web_performance/cloudlets/v2.html).

__Options__:

<div class="option" markdown="1" id="audienceSegmentation.enabled" >

- `enabled` (_boolean_): Enables the Audience Segmentation cloudlet feature.

</div>

<div class="option" markdown="1" id="audienceSegmentation.cloudletPolicy" >

- `cloudletPolicy` (_object_): Identifies the Cloudlet policy in an object featuring unique numeric `id` and descriptive string `name` members.

</div>

<div class="option" markdown="1" id="audienceSegmentation.label" >

- `label` (_string_): Specifies a suffix to append to the cookie name. This helps distinguish this audience segmentation policy from any others within the same property.

</div>

<div class="option" markdown="1" id="audienceSegmentation.segmentTrackingMethod" >

- `segmentTrackingMethod` (_enum string_): Specifies the method to pass segment information to the origin. The Cloudlet passes the rule applied to a given request either `IN_COOKIE_HEADER`, `IN_QUERY_PARAM`, `IN_CUSTOM_HEADER`, or the default, `NONE`.

</div>

<div class="option" markdown="1" id="audienceSegmentation.segmentTrackingQueryParam" >

- `segmentTrackingQueryParam` (_string_): With `segmentTrackingMethod` set to `IN_QUERY_PARAM`, this query parameter specifies the name of the segmentation rule.

</div>

<div class="option" markdown="1" id="audienceSegmentation.segmentTrackingCookieName" >

- `segmentTrackingCookieName` (_string_): With `segmentTrackingMethod` set to `IN_COOKIE_HEADER`, this cookie name specifies the name of the segmentation rule.

</div>

<div class="option" markdown="1" id="audienceSegmentation.segmentTrackingCustomHeader" >

- `segmentTrackingCustomHeader` (_string_): With `segmentTrackingMethod` set to `IN_CUSTOM_HEADER`, this custom HTTP header specifies the name of the segmentation rule.

</div>

<div class="option" markdown="1" id="audienceSegmentation.populationCookieType" >

- `populationCookieType` (_enum string_): Specifies when the segmentation cookie expires, either `ON_BROWSER_CLOSE`, `NEVER`, or based on a specific `DURATION`.

</div>

<div class="option" markdown="1" id="audienceSegmentation.populationDuration" >

- `populationDuration` (_duration string_): With `populationCookieType` set to `DURATION`, specifies the lifetime of the segmentation cookie.

</div>

<div class="option" markdown="1" id="audienceSegmentation.populationRefresh" >

- `populationRefresh` (_boolean_): If disabled, sets the expiration time only if the cookie is not yet present in the request.

</div>

<div class="option" markdown="1" id="audienceSegmentation.specifyPopulationCookieDomain" >

- `specifyPopulationCookieDomain` (_boolean_): Whether to specify a cookie domain with the population cookie. It tells the browser to which domain to send the cookie.

</div>

<div class="option" markdown="1" id="audienceSegmentation.populationCookieDomain" >

- `populationCookieDomain` (_string_): With `specifyPopulationCookieDomain` enabled, specifies the domain to track the population cookie.

</div>

<div class="option" markdown="1" id="audienceSegmentation.populationCookieAutomaticSalt" >

- `populationCookieAutomaticSalt` (_boolean_): Whether to assign a _salt_ value automatically to the cookie to prevent manipulation by the user. You should not enable if sharing the population cookie across more than one property.

</div>

<div class="option" markdown="1" id="audienceSegmentation.populationCookieSalt" >

- `populationCookieSalt` (_string_): With `populationCookieAutomaticSalt` disabled, specifies the cookie's salt value. Use this option to share the cookie across many properties.

</div>

<div class="option" markdown="1" id="audienceSegmentation.populationCookieIncludeRuleName" >

- `populationCookieIncludeRuleName` (_boolean_): When enabled, includes in the session cookie the name of the rule in which this behavior appears.

</div>

</div>

<div class="feature" data-feature="autoDomainValidation" markdown="1">
