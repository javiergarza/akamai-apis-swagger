---
title: "verifyJsonWebToken"
slug: "verifyjsonwebtoken"
hidden: false
createdAt: "2020-06-15T22:08:49.866Z"
updatedAt: "2020-06-15T22:08:49.866Z"
---
__Property Manager name__: [JWT verification](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9053)

This behavior allows you to use JSON Web Tokens (JWT) to verify requests.

__Options__:

<div class="option" markdown="1" id="verifyJsonWebToken.extractLocation" >

- `extractLocation` (_enum string_): Specify from where to extract the JWT value, either from the `CLIENT_REQUEST_HEADER` or from the request's `QUERY_STRING`.

</div>

<div class="option" markdown="1" id="verifyJsonWebToken.headerName" >

- `headerName` (_string_): With `extractLocation` set to `CLIENT_REQUEST_HEADER`, this specifies the name of the header from which to extract the JWT value.

</div>

<div class="option" markdown="1" id="verifyJsonWebToken.queryParameterName" >

- `queryParameterName` (_string_): With `extractLocation` set to `QUERY_STRING`, this specifies the name of the query parameter from which to extract the JWT value.

</div>

<div class="option" markdown="1" id="verifyJsonWebToken.jwt" >

- `jwt` (_string_): An identifier for the JWT keys collection.

</div>

<div class="option" markdown="1" id="verifyJsonWebToken.enableRS256" >

- `enableRS256` (_boolean_): 2DO.

</div>

<div class="option" markdown="1" id="verifyJsonWebToken.enableES256" >

- `enableES256` (_boolean_): 2DO.

</div>

</div>

<div class="feature" data-feature="verifyJsonWebTokenForDcp" markdown="1">
