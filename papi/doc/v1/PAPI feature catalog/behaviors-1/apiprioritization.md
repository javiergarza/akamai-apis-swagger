---
title: "apiPrioritization"
slug: "apiprioritization"
hidden: false
createdAt: "2020-06-15T20:40:17.654Z"
updatedAt: "2020-06-15T20:40:51.481Z"
---
apiPrioritization

__Property Manager name__: [API Prioritization Cloudlet](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0016)

Enables the API Prioritization Cloudlet, which maintains continuity in user experience by serving an alternate static response when load is too high. You can configure rules using either the Cloudlets Policy Manager application or the [Cloudlets API](https://learn.akamai.com/en-us/api/web_performance/cloudlets/v2.html). The feature is designed to serve static API content, such as fallback JSON data.  To serve non-API HTML content, use the [`visitorPrioritization`](#visitorprioritization) behavior.

__Options__:

<div class="option" markdown="1" id="apiPrioritization.enabled" >

- `enabled` (_boolean_): Activates the API Prioritization feature.

</div>

<div class="option" markdown="1" id="apiPrioritization.cloudletPolicy" >

- `cloudletPolicy` (_object_): Identifies the Cloudlet policy in an object featuring unique numeric `id` and descriptive string `name` members.

</div>

<div class="option" markdown="1" id="apiPrioritization.label" >

- `label` (_string_): A label to distinguish this API Prioritization policy from any others in the same property.

</div>

<div class="option" markdown="1" id="apiPrioritization.useThrottledCpCode" >

- `useThrottledCpCode` (_boolean_): Specifies whether to apply an alternative CP code for requests served the alternate response.

</div>

<div class="option" markdown="1" id="apiPrioritization.throttledCpCode" >

- `throttledCpCode` (_object_): With `useThrottledCpCode` enabled, this specifies the CP code as an object:

        "throttledCpCode": {
            "id"   : 12345,
            "name" : "sent to waiting room"
        }

</div>

<div class="option" markdown="1" id="apiPrioritization.useThrottledStatusCode" >

- `useThrottledStatusCode` (_boolean_): When enabled, allows you to assign a specific HTTP response code to a throttled request.

</div>

<div class="option" markdown="1" id="apiPrioritization.throttledStatusCode" >

- `throttledStatusCode` (_number_): With `change_response_code` enabled, specifies the HTTP response code for requests that receive the alternate response.

</div>

<div class="option" markdown="1" id="apiPrioritization.netStorage" >

- `netStorage` (_object_): Specify the NetStorage domain that contains the alternate response. For example:

        "netStorage": {
            "id"                 : "netstorage_id",
            "name"               : "Waiting Room",
            "downloadDomainName" : "example.wait.akamai.com",
            "cpCode"             : 12345
        }

</div>

<div class="option" markdown="1" id="apiPrioritization.netStoragePath" >

- `netStoragePath` (_string_): Specify the full NetStorage path for the alternate response, including trailing file name.

</div>

<div class="option" markdown="1" id="apiPrioritization.alternateResponseCacheTtl" >

- `alternateResponseCacheTtl` (_number within 5-30 range_): Specifies the alternate response's time to live in the cache, `5` minutes by default.

</div>

</div>

<div class="feature" data-feature="applicationLoadBalancer" markdown="1">
