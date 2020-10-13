---
title: "requestType"
slug: "requesttype"
hidden: false
createdAt: "2020-06-15T22:27:03.556Z"
updatedAt: "2020-06-15T22:27:03.556Z"
---
__Property Manager name__: [Request Type](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches the basic type of request.  To use this match, you need to be thoroughly familiar with how Akamai edge servers process requests.  Contact your Akamai Technical representative if you need help, and test thoroughly on staging before activating on production.

__Options__:

- `matchOperator` (_enum string_): Specifies whether the request `IS` or `IS_NOT` the type of specified `value`.

- `value` (_enum string_): Specifies the type of request, either a standard `CLIENT_REQ` or an `ESI_FRAGMENT`.
