---
title: "visitorPrioritization"
slug: "visitorprioritization"
hidden: false
createdAt: "2020-06-15T22:11:06.581Z"
updatedAt: "2020-06-15T22:11:06.581Z"
---
## visitorPrioritization

__Property Manager name__: [Visitor Prioritization Cloudlet](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0085)

The [Visitor Prioritization Cloudlet](http://www.akamai.com/html/technology/visitor-prioritization.html) is designed to decrease abandonment by providing a user-friendly waiting room experience.  With cloudlets available on your contract, choose __Your services__ &rArr; __Edge logic Cloudlets__ to control Visitor Prioritization within [Control Center](https://control.akamai.com). Otherwise use the [Cloudlets API](https://learn.akamai.com/en-us/api/web_performance/cloudlets/v2.html) to configure it programmatically.  To serve non-HTML API content such as JSON blocks, see the [`apiPrioritization`](#apiprioritization) behavior.

__Options__:

<div class="option" markdown="1" id="visitorPrioritization.enabled" >

- `enabled` (_boolean_): Enables the Visitor Prioritization behavior.

</div>

<div class="option" markdown="1" id="visitorPrioritization.cloudletPolicy" >

- `cloudletPolicy` (_object_): Identifies the Cloudlet policy in an object featuring unique numeric `id` and descriptive string `name` members.

</div>

<div class="option" markdown="1" id="visitorPrioritization.userIdentificationByCookie" >

- `userIdentificationByCookie` (_boolean_): When enabled, identifies users by the value of a cookie.

</div>

<div class="option" markdown="1" id="visitorPrioritization.userIdentificationKeyCookie" >

- `userIdentificationKeyCookie` (_string_): With `userIdentificationByCookie` enabled, specifies the name of the cookie whose value identifies users. To match a user, the value of the cookie needs to remain constant across all requests.

</div>

<div class="option" markdown="1" id="visitorPrioritization.userIdentificationByHeaders" >

- `userIdentificationByHeaders` (_boolean_): When enabled, identifies users by the values of GET or POST request headers.

</div>

<div class="option" markdown="1" id="visitorPrioritization.userIdentificationKeyHeaders" >

- `userIdentificationKeyHeaders` (_array of string values_): With `userIdentificationByHeaders` enabled, specifies names of request headers whose values identify users. To match a user, values for all the specified headers need to remain constant across all requests.

</div>

<div class="option" markdown="1" id="visitorPrioritization.userIdentificationByIp" >

- `userIdentificationByIp` (_boolean_): When enabled, allows IP addresses to identify users.

</div>

<div class="option" markdown="1" id="visitorPrioritization.userIdentificationByParams" >

- `userIdentificationByParams` (_boolean_): When enabled, identifies users by the values of GET or POST request parameters.

</div>

<div class="option" markdown="1" id="visitorPrioritization.userIdentificationKeyParams" >

- `userIdentificationKeyParams` (_array of string values_): With `userIdentificationByParams` enabled, specifies names of request parameters whose values identify users. To match a user, values for all the specified parameters need to remain constant across all requests. Parameters that are absent or blank may also identify users.

</div>

<div class="option" markdown="1" id="visitorPrioritization.allowedUserCookieEnabled" >

- `allowedUserCookieEnabled` (_boolean_): When enabled, sets a cookie for users who have been allowed through to the site.

</div>

<div class="option" markdown="1" id="visitorPrioritization.allowedUserCookieLabel" >

- `allowedUserCookieLabel` (_string_): With `allowedUserCookieEnabled` on, specifies a label to distinguish this cookie for an allowed user from others. The value appends to the cookie's name, and helps you to maintain the same user assignment across behaviors within a property, and across properties.

</div>

<div class="option" markdown="1" id="visitorPrioritization.allowedUserCookieDuration" >

- `allowedUserCookieDuration` (_number within 0-600 range_): With `allowedUserCookieEnabled` on, sets the number of seconds for the allowed user's session once allowed through to the site.

</div>

<div class="option" markdown="1" id="visitorPrioritization.allowedUserCookieRefresh" >

- `allowedUserCookieRefresh` (_boolean_): With `allowedUserCookieEnabled` on, enabling this resets the duration of an allowed cookie with each request, so that it only expires if the user doesn't make any requests for the specified duration. Do not enable this option if you want to set a fixed time for all users.

</div>

<div class="option" markdown="1" id="visitorPrioritization.allowedUserCookieAdvanced" >

- `allowedUserCookieAdvanced` (_boolean_): With `allowedUserCookieEnabled` on, sets advanced configuration options for the allowed user's cookie.

</div>

<div class="option" markdown="1" id="visitorPrioritization.allowedUserCookieAutomaticSalt" >

- `allowedUserCookieAutomaticSalt` (_boolean_): With `allowedUserCookieAdvanced` enabled, sets an automatic _salt_ value to verify the integrity of the cookie for an allowed user. Disable this if you want to share the cookie across properties.

</div>

<div class="option" markdown="1" id="visitorPrioritization.allowedUserCookieSalt" >

- `allowedUserCookieSalt` (_string_): With `allowedUserCookieAdvanced` enabled and `allowedUserCookieAutomaticSalt` disabled, specifies a fixed _salt_ value, which is incorporated into the cookie's value to prevent users from manipulating it. You can use the same salt string across different behaviors or properties to apply a single cookie to all allowed users.

</div>

<div class="option" markdown="1" id="visitorPrioritization.allowedUserCookieDomainType" >

- `allowedUserCookieDomainType` (_enum string_): With `allowedUserCookieAdvanced` enabled, selects whether to use the `DYNAMIC` incoming host header, or a `CUSTOMER`-defined cookie domain.

</div>

<div class="option" markdown="1" id="visitorPrioritization.allowedUserCookieDomain" >

- `allowedUserCookieDomain` (_string_): With `allowedUserCookieAdvanced` enabled, specifies a domain for an allowed user cookie.

</div>

<div class="option" markdown="1" id="visitorPrioritization.allowedUserCookieHttpOnly" >

- `allowedUserCookieHttpOnly` (_boolean_): With `allowedUserCookieAdvanced` enabled, applies the `HttpOnly` flag to the allowed user's cookie to ensure it's accessed over HTTP and not manipulated by the client.

</div>

<div class="option" markdown="1" id="visitorPrioritization.allowedUserCookieSecure" >

- `allowedUserCookieSecure` (_boolean_): With `allowedUserCookieAdvanced` enabled, applies the `Secure` flag to the allowed user's cookie to transmit it over a secure connection.  You can apply this option only if the property itself is secure.  See [Secure property requirements](#sf) for guidance.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCookieEnabled" >

- `waitingRoomCookieEnabled` (_boolean_): Enables a cookie to track a waiting room assignment.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCookieShareLabel" >

- `waitingRoomCookieShareLabel` (_boolean_): With `allowedUserCookieEnabled` and `waitingRoomCookieEnabled` both `true`, enabling this option shares the same `allowedUserCookieLabel` string. If disabled, specify a different `waitingRoomCookieLabel`.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCookieLabel" >

- `waitingRoomCookieLabel` (_string_): With `waitingRoomCookieEnabled` on and either `allowedUserCookieEnabled` or `waitingRoomCookieShareLabel` off, specifies a label to distinguish this waiting room cookie from others. The value appends to the cookie's name, and helps you to maintain the same waiting room assignment across behaviors within a property, and across properties.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCookieDuration" >

- `waitingRoomCookieDuration` (_number within 0-120 range_): With `waitingRoomCookieEnabled` on, sets the number of seconds for which users remain in the waiting room. During this time, users who refresh the waiting room page remain there.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCookieAdvanced" >

- `waitingRoomCookieAdvanced` (_boolean_): When enabled along with `waitingRoomCookieEnabled`, sets advanced configuration options for the waiting room cookie.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCookieAutomaticSalt" >

- `waitingRoomCookieAutomaticSalt` (_boolean_): With `waitingRoomCookieAdvanced` enabled, sets an automatic _salt_ value to verify the integrity of the waiting room cookie.  Disable this if you want to share the cookie across properties.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCookieSalt" >

- `waitingRoomCookieSalt` (_string_): With `waitingRoomCookieAdvanced` enabled and `waitingRoomCookieAutomaticSalt` disabled, specifies a fixed _salt_ value, which is incorporated into the cookie's value to prevent users from manipulating it. You can use the same salt string across different behaviors or properties to apply a single cookie for the waiting room session.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCookieDomainType" >

- `waitingRoomCookieDomainType` (_enum string_): With `waitingRoomCookieAdvanced` enabled, selects whether to use the `DYNAMIC` incoming host header, or a `CUSTOMER`-defined cookie domain.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCookieDomain" >

- `waitingRoomCookieDomain` (_string_): With `waitingRoomCookieAdvanced` enabled, specifies a domain for the waiting room cookie.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCookieHttpOnly" >

- `waitingRoomCookieHttpOnly` (_boolean_): With `waitingRoomCookieAdvanced` enabled, applies the `HttpOnly` flag to the waiting room cookie to ensure it's accessed over HTTP and not manipulated by the client.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCookieSecure" >

- `waitingRoomCookieSecure` (_boolean_): With `waitingRoomCookieAdvanced` enabled, applies the `Secure` flag to the waiting room cookie to transmit it over a secure connection.  You can apply this option only if the property itself is secure. See [Secure property requirements](#sf) for guidance.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomStatusCode" >

- `waitingRoomStatusCode` (_number_): Specifies the response code for requests sent to the waiting room.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomUseCpCode" >

- `waitingRoomUseCpCode` (_boolean_): When enabled, allows you to assign a different CP code that tracks any requests that are sent to the waiting room.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCpCode" >

- `waitingRoomCpCode` (_object_): With `waitingRoomUseCpCode` enabled, specifies a `cpcode` object for requests sent to the waiting room, including a numeric `id` key and a descriptive `name`:

        "waitingRoomCpCode": {
            "id": 12345,
            "name": "sent to waiting room"
        }

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomNetStorage" >

- `waitingRoomNetStorage` (_object_): Specifies the NetStorage domain for the waiting room page. For example:

        "waitingRoomNetStorage": {
            "id": "netstorage_id",
            "name": "Example Downloads",
            "downloadDomainName": "download.example.com",
            "cpCode": 12345
        }

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomDirectory" >

- `waitingRoomDirectory` (_string; allows [variables](#vf)_): Specifies the NetStorage directory that contains the static waiting room page, with no trailing slash character.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCacheTtl" >

- `waitingRoomCacheTtl` (_number within 5-30 range_): Specifies the waiting room page's time to live in the cache, `5` minutes by default.

</div>

</div>

<div class="feature" data-feature="watermarkUrl" markdown="1">
