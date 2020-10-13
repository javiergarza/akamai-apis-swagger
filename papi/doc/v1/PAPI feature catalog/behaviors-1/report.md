---
title: "report"
slug: "report"
hidden: false
createdAt: "2020-06-15T21:52:50.353Z"
updatedAt: "2020-06-15T21:52:50.353Z"
---
__Property Manager name__: [Log Request Details](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0072)

Specify the HTTP request headers or cookie names to log in your Log Delivery Service reports.

__Options__:

<div class="option" markdown="1" id="report.logHost" >

- `logHost` (_boolean_): Log the `Host` header.

</div>

<div class="option" markdown="1" id="report.logReferer" >

- `logReferer` (_boolean_): Log the `Referer` header.

</div>

<div class="option" markdown="1" id="report.logUserAgent" >

- `logUserAgent` (_boolean_): Log the `User-Agent` header.

</div>

<div class="option" markdown="1" id="report.logAcceptLanguage" >

- `logAcceptLanguage` (_boolean_): Log the `Accept-Language` header.

</div>

<div class="option" markdown="1" id="report.logCookies" >

- `logCookies` (_enum string_): With a set of defined `cookie` names, specifies whether you want to log `ALL` or `SOME` cookies, or to turn `OFF` the feature to stop logging cookies.

</div>

<div class="option" markdown="1" id="report.cookies" >

- `cookies` (_array of string values_): With `logCookies` set to `SOME`, this specifies the set of cookies names whose values you want to log.

</div>

<div class="option" markdown="1" id="report.logCustomLogField" >

- `logCustomLogField` (_boolean_): Whether to append additional custom data to each log line.

</div>

<div class="option" markdown="1" id="report.customLogField" >

- `customLogField` (_string; allows [variables](#vf)_): With `logCustomLogField` enabled, specifies an additional data field to append to each log line, maximum 40 bytes, typically based on a dynamically generated built-in system variable. For example, `round-trip: {{ "{{" }}builtin.AK_CLIENT_TURNAROUND_TIME}}ms` would log the total time to complete the response. See [Support for variables](#vf) for more information.

</div>

</div>

<div class="feature" data-feature="requestControl" markdown="1">
