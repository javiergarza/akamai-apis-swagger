---
title: "inputValidation"
slug: "inputvalidation"
hidden: false
createdAt: "2020-06-15T21:31:38.766Z"
updatedAt: "2020-06-15T21:31:38.766Z"
---
__Property Manager name__: [Input Validation Cloudlet](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0053)

The Input Validation Cloudlet detects anomalous edge requests and helps mitigate repeated invalid requests.  You can configure it using either the Cloudlets Policy Manager application, available within [Control Center](https://control.akamai.com) under __Your services__ &rArr; __Edge logic Cloudlets__, or the [Cloudlets API](https://learn.akamai.com/en-us/api/web_performance/cloudlets/v2.html).

Use this behavior to specify criteria that identifies each unique end user, and optionally supplement the Input Validation policy with additional criteria your origin uses to identify invalid requests. Specify the threshold number of invalid requests that triggers a penalty, and the subsequent response.  Also specify an ordinary failure response for those who have not yet met the threshold, which should not conflict with any other behavior that defines a failure response.

__Options__:

<div class="option" markdown="1" id="inputValidation.enabled" >

- `enabled` (_boolean_): Applies the Input Validation Cloudlet behavior.

</div>

<div class="option" markdown="1" id="inputValidation.cloudletPolicy" >

- `cloudletPolicy` (_object_): Identifies the Cloudlet policy in an object featuring unique numeric `id` and descriptive string `name` members.

</div>

<div class="option" markdown="1" id="inputValidation.label" >

- `label` (_string_): Distinguishes this Input Validation policy from any others within the same property.

</div>

<div class="option" markdown="1" id="inputValidation.userIdentificationByCookie" >

- `userIdentificationByCookie` (_boolean_): When enabled, identifies users by the value of a cookie.

</div>

<div class="option" markdown="1" id="inputValidation.userIdentificationKeyCookie" >

- `userIdentificationKeyCookie` (_string_): With `userIdentificationByCookie` enabled, this specifies the cookie name whose value must remain constant across requests to identify a user.

</div>

<div class="option" markdown="1" id="inputValidation.userIdentificationByIp" >

- `userIdentificationByIp` (_boolean_): When enabled, identifies users by specific IP address. Do not enable this if you are concerned about DDoS attacks from many different IP addresses.

</div>

<div class="option" markdown="1" id="inputValidation.userIdentificationByHeaders" >

- `userIdentificationByHeaders` (_boolean_): When enabled, identifies users by specific HTTP headers on GET or POST requests.

</div>

<div class="option" markdown="1" id="inputValidation.userIdentificationKeyHeaders" >

- `userIdentificationKeyHeaders` (_array of string values_): With `userIdentificationByHeaders` enabled, this specifies the HTTP headers whose combined set of values identify each end user.

</div>

<div class="option" markdown="1" id="inputValidation.userIdentificationByParams" >

- `userIdentificationByParams` (_boolean_): When enabled, identifies users by specific query parameters on GET or POST requests.

</div>

<div class="option" markdown="1" id="inputValidation.userIdentificationKeyParams" >

- `userIdentificationKeyParams` (_array of string values_): With `userIdentificationByParams` enabled, this specifies the query parameters whose combined set of values identify each end user.

</div>

<div class="option" markdown="1" id="inputValidation.allowLargePostBody" >

- `allowLargePostBody` (_boolean_): Fails POST request bodies that exceed 16 KB when enabled, otherwise allows them to pass with no validation for policy compliance.

</div>

<div class="option" markdown="1" id="inputValidation.resetOnValid" >

- `resetOnValid` (_boolean_): Upon receiving a valid request, enabling this resets the `penaltyThreshold` counter to zero.  Otherwise, even those series of invalid requests that are interrupted by valid requests may trigger the `penaltyAction`.

</div>

<div class="option" markdown="1" id="inputValidation.validateOnOriginWith" >

- `validateOnOriginWith` (_enum string_): For any validation that edge servers can't perform alone, this specifies additional validation steps based on how the origin identifies an invalid request.  If a request is invalid, the origin can indicate this to the edge server either with a `RESPONSE_CODE` or `RESPONSE_CODE_AND_HEADER`.  If no additional validation is necessary, specify `DISABLED`.

</div>

<div class="option" markdown="1" id="inputValidation.validateOnOriginHeaderName" >

- `validateOnOriginHeaderName` (_string_): If `validateOnOriginWith` is set to `RESPONSE_CODE_AND_HEADER`, this specifies the header name for a request that the origin identifies as invalid.

</div>

<div class="option" markdown="1" id="inputValidation.validateOnOriginHeaderValue" >

- `validateOnOriginHeaderValue` (_string_): If `validateOnOriginWith` is set to `RESPONSE_CODE_AND_HEADER`, this specifies an invalid request's header value that corresponds to the `validateOnOriginHeaderName`.

</div>

<div class="option" markdown="1" id="inputValidation.validateOnOriginResponseCode" >

- `validateOnOriginResponseCode` (_number_): Unless `validateOnOriginWith` is `DISABLED`, this identifies the integer response code for requests the origin identifies as invalid.

</div>

<div class="option" markdown="1" id="inputValidation.failure302Uri" >

- `failure302Uri` (_string_): Specifies the redirect link for invalid requests that have not yet triggered a penalty.

</div>

<div class="option" markdown="1" id="inputValidation.penaltyThreshold" >

- `penaltyThreshold` (_number_): Specifies the number of invalid requests permitted before executing the `penaltyAction`.

</div>

<div class="option" markdown="1" id="inputValidation.penaltyAction" >

- `penaltyAction` (_enum string_): Once the `penaltyThreshold` of invalid requests is met, this specifies the response, either `BRANDED_403`, `BLANK_403` or `REDIRECT_302`.

</div>

<div class="option" markdown="1" id="inputValidation.penalty302Uri" >

- `penalty302Uri` (_string_): With `penaltyAction` set to `REDIRECT_302`, this specifies the redirect link for end users who trigger the penalty.

</div>

<div class="option" markdown="1" id="inputValidation.penaltyNetStorage" >

- `penaltyNetStorage` (_object_): With `penaltyAction` set to `BRANDED_403`, this specifies the NetStorage account that serves out the penalty's static 403 response content. Details appear in an object featuring a `downloadDomainName` string member that identifies the NetStorage hostname, and an integer `cpCode` to track the traffic.

</div>

<div class="option" markdown="1" id="inputValidation.penalty403NetStoragePath" >

- `penalty403NetStoragePath` (_string_): With `penaltyAction` set to `BRANDED_403`, this specifies the full path to the static 403 response content relative to the `downloadDomainName` in the `penaltyNetStorage` object.

</div>

<div class="option" markdown="1" id="inputValidation.penaltyBrandedDenyCacheTtl" >

- `penaltyBrandedDenyCacheTtl` (_number within 5-30 range_): With `penaltyAction` set to `BRANDED_403`, this specifies the penalty response's time to live in the cache, `5` minutes by default.

</div>

</div>

<div class="feature" data-feature="instant" markdown="1">
