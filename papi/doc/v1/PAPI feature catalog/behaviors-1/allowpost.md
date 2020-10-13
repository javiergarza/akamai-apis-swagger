---
title: "allowPost"
slug: "allowpost"
hidden: false
createdAt: "2020-06-15T20:38:12.305Z"
updatedAt: "2020-06-15T20:38:12.305Z"
---
__Property Manager name__: [Allow POST](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0012)

Allow HTTP requests using the POST method. By default, only GET and HEAD are allowed, and all other methods result in a 403 error. See also the [`allowDelete`](#allowdelete), [`allowOptions`](#allowoptions), [`allowPatch`](#allowpatch), and [`allowPut`](#allowput) behaviors.

__Options__:

<div class="option" markdown="1" id="allowPost.enabled" >

- `enabled` (_boolean_): When enabled, allows POST requests.

</div>

<div class="option" markdown="1" id="allowPost.allowWithoutContentLength" >

- `allowWithoutContentLength` (_boolean_): By default, POST requests also require a `Content-Length` header, or they result in a 411 error. With this option enabled with no specified `Content-Length`, the edge server relies on a `Transfer-Encoding` header to chunk the data. If neither header is present, it assumes the request has no body, and it adds a header with a `0` value to the forward request.

</div>

</div>

<div class="feature" data-feature="allowPut" markdown="1">
