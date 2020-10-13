---
title: "saasDefinitions"
slug: "saasdefinitions"
hidden: false
createdAt: "2020-06-15T21:57:27.707Z"
updatedAt: "2020-06-15T21:57:27.707Z"
---
__Property Manager name__: [SaaS Definitions](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0078)

Configures how the Software as a Service feature identifies _customers_, _applications_, and _users_. A different set of options is available for each type of targeted request, each enabled with the `action`-suffixed option. In each case, you can use `PATH`, `COOKIE`, `QUERY_STRING`, or `HOSTNAME` components as identifiers, or `disable` the [SaaS](https://control.akamai.com/dl/customers/SaaS/SaaS-User-Guide.pdf) behavior for certain targets. If you rely on a `HOSTNAME`, you also have the option of specifying a _CNAME chain_ rather than an individual hostname. The various options suffixed `regex` and `replace` subsequently remove the identifier from the request. This behavior requires a sibling [`origin`](#origin) behavior whose `originType` option is set to `SAAS_DYNAMIC_ORIGIN`.

__Options__:

<div class="option" markdown="1" id="saasDefinitions.applicationAction" >

- `applicationAction` (_enum string_): Specifies the request component that identifies a SaaS application, either `COOKIE`, `HOSTNAME`, `PATH`, or `QUERY_STRING`. Setting it to `DISABLED` effectively ignores applications.

</div>

<div class="option" markdown="1" id="saasDefinitions.applicationCookie" >

- `applicationCookie` (_string_): With `applicationAction` set to `COOKIE`, this specifies the name of the cookie that identifies the application.

</div>

<div class="option" markdown="1" id="saasDefinitions.applicationQueryString" >

- `applicationQueryString` (_string_): With `applicationAction` set to `QUERY_STRING`, this names the query parameter that identifies the application.

</div>

<div class="option" markdown="1" id="saasDefinitions.applicationCnameEnabled" >

- `applicationCnameEnabled` (_boolean_): With `applicationAction` set to `HOSTNAME`, enabling this allows you to identify applications using a _CNAME chain_ rather than a single hostname.

</div>

<div class="option" markdown="1" id="saasDefinitions.applicationCnameLevel" >

- `applicationCnameLevel` (_number_): With `applicationCnameEnabled` on, this specifies the number of CNAMEs to use in the chain.

</div>

<div class="option" markdown="1" id="saasDefinitions.applicationRegex" >

- `applicationRegex` (_string_): Specifies a Perl-compatible regular expression with which to substitute the request's application ID.

</div>

<div class="option" markdown="1" id="saasDefinitions.applicationReplace" >

- `applicationReplace` (_string_): Specifies a string to replace the request's application ID matched by `applicationRegex`.

</div>

<div class="option" markdown="1" id="saasDefinitions.customerAction" >

- `customerAction` (_enum string_): Specifies the request component that identifies a SaaS customer, either `COOKIE`, `HOSTNAME`, `PATH`, or `QUERY_STRING`. Setting it to `DISABLED` effectively ignores customers.

</div>

<div class="option" markdown="1" id="saasDefinitions.customerCookie" >

- `customerCookie` (_string_): With `customerAction` set to `COOKIE`, this specifies the name of the cookie that identifies the customer.

</div>

<div class="option" markdown="1" id="saasDefinitions.customerQueryString" >

- `customerQueryString` (_string_): With `customerAction` set to `QUERY_STRING`, this names the query parameter that identifies the customer.

</div>

<div class="option" markdown="1" id="saasDefinitions.customerCnameEnabled" >

- `customerCnameEnabled` (_boolean_): With `customerAction` set to `HOSTNAME`, enabling this allows you to identify customers using a _CNAME chain_ rather than a single hostname.

</div>

<div class="option" markdown="1" id="saasDefinitions.customerCnameLevel" >

- `customerCnameLevel` (_number_): With `customerCnameEnabled` on, this specifies the number of CNAMEs to use in the chain.

</div>

<div class="option" markdown="1" id="saasDefinitions.customerRegex" >

- `customerRegex` (_string_): Specifies a Perl-compatible regular expression with which to substitute the request's customer ID.

</div>

<div class="option" markdown="1" id="saasDefinitions.customerReplace" >

- `customerReplace` (_string_): Specifies a string to replace the request's customer ID matched by `customerRegex`.

</div>

<div class="option" markdown="1" id="saasDefinitions.usersAction" >

- `usersAction` (_enum string_): Specifies the request component that identifies a SaaS user, either `COOKIE`, `HOSTNAME`, `PATH`, or `QUERY_STRING`. Setting it to `DISABLED` effectively ignores users.

</div>

<div class="option" markdown="1" id="saasDefinitions.usersCookie" >

- `usersCookie` (_string_): With `usersAction` set to `COOKIE`, this specifies the name of the cookie that identifies the user.

</div>

<div class="option" markdown="1" id="saasDefinitions.usersQueryString" >

- `usersQueryString` (_string_): With `usersAction` set to `QUERY_STRING`, this names the query parameter that identifies the user.

</div>

<div class="option" markdown="1" id="saasDefinitions.usersCnameEnabled" >

- `usersCnameEnabled` (_boolean_): With `usersAction` set to `HOSTNAME`, enabling this allows you to identify users using a _CNAME chain_ rather than a single hostname.

</div>

<div class="option" markdown="1" id="saasDefinitions.usersCnameLevel" >

- `usersCnameLevel` (_number_): With `userCnameEnabled` on, this specifies the number of CNAMEs to use in the chain.

</div>

<div class="option" markdown="1" id="saasDefinitions.usersRegex" >

- `usersRegex` (_string_): Specifies a Perl-compatible regular expression with which to substitute the request's user ID.

</div>

<div class="option" markdown="1" id="saasDefinitions.usersReplace" >

- `usersReplace` (_string_): Specifies a string to replace the request's user ID matched by `usersRegex`.

</div>

</div>

<div class="feature" data-feature="salesForceCommerceCloudClient" markdown="1">
