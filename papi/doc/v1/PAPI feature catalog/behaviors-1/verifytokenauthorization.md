---
title: "verifyTokenAuthorization"
slug: "verifytokenauthorization"
hidden: false
createdAt: "2020-06-15T22:09:54.190Z"
updatedAt: "2020-06-15T22:09:54.190Z"
---
__Property Manager name__: [Auth Token 2.0 Verification](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9068)

Verifies Auth 2.0 tokens.

__Options__:

<div class="option" markdown="1" id="verifyTokenAuthorization.useAdvanced" >

- `useAdvanced` (_boolean_): If enabled, allows you to specify advanced options such as `algorithm`, `escapeHmacInputs`, `ignoreQueryString`, `transitionKey`, and `salt`.

</div>

<div class="option" markdown="1" id="verifyTokenAuthorization.location" >

- `location` (_enum string_): Specifies where to find the token in the incoming request, either `CLIENT_REQUEST_HEADER`, `QUERY_STRING`, or `COOKIE`.

</div>

<div class="option" markdown="1" id="verifyTokenAuthorization.locationId" >

- `locationId` (_string_): When `location` is `CLIENT_REQUEST_HEADER`, specifies the name of the incoming request's header where to find the token.

</div>

<div class="option" markdown="1" id="verifyTokenAuthorization.algorithm" >

- `algorithm` (_enum string_): With `useAdvanced` enabled, specifies the algorithm that generates the token, either `SHA256`, `SHA1`, or `MD5`, in order of descending security. It must match the method chosen in the token generation code.

</div>

<div class="option" markdown="1" id="verifyTokenAuthorization.escapeHmacInputs" >

- `escapeHmacInputs` (_boolean_): With `useAdvanced` enabled, URL-escapes HMAC inputs passed in as query parameters.

</div>

<div class="option" markdown="1" id="verifyTokenAuthorization.ignoreQueryString" >

- `ignoreQueryString` (_boolean_): With `useAdvanced` enabled, enabling this removes the query string from the URL used to form an encryption key.

</div>

<div class="option" markdown="1" id="verifyTokenAuthorization.key" >

- `key` (_string_): The shared secret used to validate tokens, which must match the key used in the token generation code.

</div>

<div class="option" markdown="1" id="verifyTokenAuthorization.transitionKey" >

- `transitionKey` (_string_): With `useAdvanced` enabled, specifies a transition key as a hex value.

</div>

<div class="option" markdown="1" id="verifyTokenAuthorization.salt" >

- `salt` (_string_): With `useAdvanced` enabled, specifies a salt string for input when generating the token, which must match the salt value used in the token generation code.

</div>

<div class="option" markdown="1" id="verifyTokenAuthorization.failureResponse" >

- `failureResponse` (_boolean_): When enabled, sends an HTTP error when an authentication test fails.

</div>

</div>

<div class="feature" data-feature="visitorPrioritization" markdown="1">
