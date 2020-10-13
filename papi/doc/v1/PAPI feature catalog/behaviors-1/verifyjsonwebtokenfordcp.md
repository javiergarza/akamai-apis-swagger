---
title: "verifyJsonWebTokenForDcp"
slug: "verifyjsonwebtokenfordcp"
hidden: false
createdAt: "2020-06-15T22:09:19.301Z"
updatedAt: "2020-06-15T22:09:19.301Z"
---
__Property Manager name__: [JWT](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9044)

This behavior allows you to use JSON web tokens (JWT) to verify requests for use in implementing [IoT Edge Connect](https://learn.akamai.com/en-us/products/web_performance/iot_edge_connect.html), which you use the [`dcp`](#dcp) behavior to configure. You can specify the location in a request to pass a JSON web token (JWT), collections of public keys to verify the integrity of this token, and specific claims to extract from it. Use the [`verifyJsonWebToken`](#verifyjsonwebtoken) behavior for other JWT validation.

When authenticating to edge servers with both JWT and mutual authentication (using the [`dcpAuthVariableExtractor`](#dcpauthvariableextractor) behavior), the JWT method is ignored, and you need to authenticate with a client authentication certificate.

__Options__:

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.extractLocation" >

- `extractLocation` (_enum string_): Specifies whether to get the JWT value from the `CLIENT_REQUEST_HEADER`, or from a `QUERY_STRING`.

</div>

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.primaryLocation" >

- `primaryLocation` (_enum string_): 2DO: `CLIENT_REQUEST_HEADER`, `QUERY_STRING`.

</div>

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.customHeader" >

- `customHeader` (_boolean_): With `extractLocation` set to `CLIENT_REQUEST_HEADER`, The JWT value comes from the `X-Akamai-DCP-Token` header by default.  Enabling this option allows you to extract it from another header name that you specify.

</div>

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.headerName" >

- `headerName` (_string_): With `customHeader` enabled, this specifies the name of the header to extract the JWT value from.

</div>

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.queryParameterName" >

- `queryParameterName` (_string_): With `extractLocation` set to `QUERY_STRING`, this specifies the name of the query parameter from which to extract the JWT value.

</div>

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.jwt" >

- `jwt` (_string_): An identifier for the JWT keys collection.

</div>

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.extractClientId" >

- `extractClientId` (_boolean_): When enabled, allows you to extract the client ID claim name stored in JWT.

</div>

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.clientId" >

- `clientId` (_string_): With `extractClientId` enabled, this specifies the claim name.

</div>

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.extractAuthorizations" >

- `extractAuthorizations` (_boolean_): When enabled, allows you to extract the authorization groups stored in the JWT.

</div>

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.authorizations" >

- `authorizations` (_string_): With `extractAuthorizations` enabled, this specifies the authorization group name.

</div>

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.extractUserName" >

- `extractUserName` (_boolean_): When enabled, allows you to extract the user name stored in the JWT.

</div>

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.userName" >

- `userName` (_string_): With `extractUserName` enabled, this specifies the user name.

</div>

</div>

<div class="feature" data-feature="verifyTokenAuthorization" markdown="1">
