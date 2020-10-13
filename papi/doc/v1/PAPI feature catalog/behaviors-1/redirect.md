---
title: "redirect"
slug: "redirect"
hidden: false
createdAt: "2020-06-15T21:49:32.137Z"
updatedAt: "2020-06-15T21:49:32.137Z"
---
__Property Manager name__: [Redirect](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0069)

Respond to the client request with a redirect without contacting the origin. Specify the redirect as a path expression starting with a `/` character relative to the current root, or as a fully qualified URL. This behavior relies primarily on `destinationHostname` and `destinationPath` to manipulate the hostname and path independently.

See also the [`redirectplus`](#redirectplus) behavior, which allows you to use [variables](#vf) more flexibly to express the redirect's destination.

__Options__:

<div class="option" markdown="1" id="redirect.mobileDefaultChoice" >

- `mobileDefaultChoice` (_enum string_): When set to `MOBILE`, allows only a `302` response code. When set to `DEFAULT`, allows all other `responseCode` values.

</div>

<div class="option" markdown="1" id="redirect.destinationProtocol" >

- `destinationProtocol` (_enum string_): Choose the protocol for the redirect URL, either `HTTP`, `HTTPS`, or `SAME_AS_REQUEST` to pass through the original protocol.

</div>

<div class="option" markdown="1" id="redirect.destinationHostname" >

- `destinationHostname` (_enum string_): Specify how to change the requested hostname, independently from the pathname:

    - `SUBDOMAIN` prepends a subdomain from the     `destinationHostSubdomain` field.
    - `SIBLING` replaces the leftmost subdomain with the     `destinationHostSibling` field.
    - `OTHER` specifies a static domain in the     `destinationHostnameOther` field.
    - `SAME_AS_REQUEST` preserves the hostname unchanged.

</div>

<div class="option" markdown="1" id="redirect.destinationHostSubdomain" >

- `destinationHostSubdomain` (_string; allows [variables](#vf)_): If `destinationHostname` is set to `SUBDOMAIN`, this specifies a subdomain to prepend to the current hostname. For example, a value of `m` changes `www.example.com` to `m.www.example.com`.

</div>

<div class="option" markdown="1" id="redirect.destinationHostSibling" >

- `destinationHostSibling` (_string; allows [variables](#vf)_): If `destinationHostname` is set to `SIBLING`, this specifies the subdomain with which to replace to the current hostname's leftmost subdomain. For example, a value of `m` changes `www.example.com` to `m.example.com`.

</div>

<div class="option" markdown="1" id="redirect.destinationHostnameOther" >

- `destinationHostnameOther` (_string; allows [variables](#vf)_): If `destinationHostname` is set to `OTHER`, this specifies the full hostname with which to replace the current hostname.

</div>

<div class="option" markdown="1" id="redirect.destinationPath" >

- `destinationPath` (_enum string_): Specify how to change the requested pathname, independently from the hostname:

    - `PREFIX_REQUEST` prepends a path with the     `destinationPathPrefix` field. You also have the option to     specify a suffix using `destinationPathSuffix` and     `destinationPathSuffixStatus`.
    - `OTHER` replaces the current path with the     `destinationPathOther` field.
    - `SAME_AS_REQUEST` preserves the current path unchanged.

</div>

<div class="option" markdown="1" id="redirect.destinationPathPrefix" >

- `destinationPathPrefix` (_string; allows [variables](#vf)_): When `destinationPath` is set to `PREFIX_REQUEST`, this prepends the current path. For example, a value of `/prefix/path` changes `/example/index.html` to `/prefix/path/example/index.html`.

</div>

<div class="option" markdown="1" id="redirect.destinationPathSuffixStatus" >

- `destinationPathSuffixStatus` (_enum string_): When `destinationPath` is set to `PREFIX_REQUEST`, this gives you the option of adding a suffix. Specify `NO_SUFFIX` if you want to preserve the end of the path unchanged. If you specify `SUFFIX`, the `destinationPathSuffix` provides the value.

</div>

<div class="option" markdown="1" id="redirect.destinationPathSuffix" >

- `destinationPathSuffix` (_string; allows [variables](#vf)_): When `destinationPath` is set to `PREFIX_REQUEST` and `destinationPathSuffixStatus` is set to `SUFFIX`, this specifies the suffix to append to the path.

</div>

<div class="option" markdown="1" id="redirect.destinationPathOther" >

- `destinationPathOther` (_string; allows [variables](#vf)_): When `destinationPath` is set to `PREFIX_REQUEST`, this replaces the current path.

</div>

<div class="option" markdown="1" id="redirect.queryString" >

- `queryString` (_enum string_): When set to `APPEND`, passes incoming query string parameters as part of the redirect URL. Otherwise set this to `IGNORE`.

</div>

<div class="option" markdown="1" id="redirect.responseCode" >

- `responseCode` (_numeric enum_): Specify the redirect's response code: `301` (Moved Permanently), `302` (Found), `303` (See Other), or `307` (Temporary Redirect).

</div>

</div>

<div class="feature" data-feature="redirectplus" markdown="1">
