---
title: "responseCookie"
slug: "responsecookie"
hidden: false
createdAt: "2020-06-15T21:55:11.820Z"
updatedAt: "2020-06-15T21:55:11.820Z"
---
__Property Manager name__: [Set Response Cookie](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0076)

Set a cookie to send downstream to the client, either with a fixed value or a unique stamp.

__Options__:

<div class="option" markdown="1" id="responseCookie.enabled" >

- `enabled` (_boolean_): When enabled, allows you to set a response cookie.

</div>

<div class="option" markdown="1" id="responseCookie.cookieName" >

- `cookieName` (_string; allows [variables](#vf)_): Specifies the name of the cookie, which serves as a key to determine if the cookie is set.

</div>

<div class="option" markdown="1" id="responseCookie.type" >

- `type` (_enum string_): Assign either a `UNIQUE` value, or a `FIXED` one based on the `value` field.

</div>

<div class="option" markdown="1" id="responseCookie.value" >

- `value` (_string; allows [variables](#vf)_): If the cookie `type` is `FIXED`, this specifies the cookie value.

</div>

<div class="option" markdown="1" id="responseCookie.format" >

- `format` (_enum string_): When the `type` of cookie is set to `UNIQUE`, set this to either `APACHE` or `AKAMAI` format. The latter format adds milliseconds to the date stamp.

</div>

<div class="option" markdown="1" id="responseCookie.defaultDomain" >

- `defaultDomain` (_boolean_): When enabled, uses the default domain value, otherwise the set specified in the `domain` field.

</div>

<div class="option" markdown="1" id="responseCookie.defaultPath" >

- `defaultPath` (_boolean_): When enabled, uses the default path value, otherwise the set specified in the `path` field.

</div>

<div class="option" markdown="1" id="responseCookie.domain" >

- `domain` (_string; allows [variables](#vf)_): If the `defaultDomain` is disabled, this sets the domain for which the cookie is valid. For example, `example.com` makes the cookie valid for that hostname and all subdomains.

</div>

<div class="option" markdown="1" id="responseCookie.path" >

- `path` (_string; allows [variables](#vf)_): If the `defaultPath` is disabled, sets the path component for which the cookie is valid.

</div>

<div class="option" markdown="1" id="responseCookie.expires" >

- `expires` (_enum string_): Sets various ways to specify when the cookie expires:

    - A value of `NEVER` lets the cookie persist indefinitely.
    - A value of `ON_BROWSER_CLOSE` limits the cookie to the duration     of the session.
    - A value of `DURATION` requires a corresponding `DURATION` field     value.
    - A value of `FIXED_DATE` requires a corresponding     `expirationDate` field value.

</div>

<div class="option" markdown="1" id="responseCookie.expirationDate" >

- `expirationDate` (_ISO 8601 format date/time string_): If `expires` is set to `FIXED_DATE`, this sets when the cookie expires as a UTC date and time.

</div>

<div class="option" markdown="1" id="responseCookie.duration" >

- `duration` (_duration string_): If `expires` is set to `DURATION`, this sets the cookie's lifetime.

</div>

<div class="option" markdown="1" id="responseCookie.secure" >

- `secure` (_boolean_): When enabled, sets the cookie's `Secure` flag to transmit it with `HTTPS`.

</div>

</div>

<div class="feature" data-feature="restrictObjectCaching" markdown="1">
