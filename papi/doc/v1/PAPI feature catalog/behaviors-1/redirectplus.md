---
title: "redirectplus"
slug: "redirectplus"
hidden: false
createdAt: "2020-06-15T21:49:54.735Z"
updatedAt: "2020-06-15T21:49:54.735Z"
---
__Property Manager name__: [Redirect Plus](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0069)

Respond to the client request with a redirect without contacting the origin. This behavior fills the same need as [`redirect`](#redirect), but allows you to use [variables](#vf) to express the redirect `destination`'s component values more concisely.

__Options__:

<div class="option" markdown="1" id="redirectplus.enabled" >

- `enabled` (_boolean_): Enables the redirect feature.

</div>

<div class="option" markdown="1" id="redirectplus.destination" >

- `destination` (_string; allows [variables](#vf)_): Specifies the redirect as a path expression starting with a `/` character relative to the current root, or as a fully qualified URL. Optionally inject variables, as in this example that refers to the original request's filename: `/path/to/{{ "{{" }}builtin.AK_FILENAME}}`.

</div>

<div class="option" markdown="1" id="redirectplus.responseCode" >

- `responseCode` (_numeric enum_): Assigns the status code for the redirect response, either `301`, `302`, `303`, or `307`.

</div>

</div>

<div class="feature" data-feature="refererChecking" markdown="1">
