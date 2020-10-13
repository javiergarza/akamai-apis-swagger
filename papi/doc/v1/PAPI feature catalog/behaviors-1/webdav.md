---
title: "webdav"
slug: "webdav"
hidden: false
createdAt: "2020-06-15T22:12:56.544Z"
updatedAt: "2020-06-15T22:12:56.544Z"
---
__Property Manager name__: [WebDAV](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9057)

Web-based Distributed Authoring and Versioning (WebDAV) is a set of extensions to the HTTP protocol that allows users to collaboratively edit and manage files on remote web servers. This behavior enables WebDAV, and provides support for the following additional request methods: PROPFIND, PROPPATCH, MKCOL, COPY, MOVE, LOCK, and UNLOCK. To apply this behavior, you need to match on a [`requestMethod`](#requestmethod).

__Options__:

<div class="option" markdown="1" id="webdav.enabled" >

- `enabled` (_boolean_): Enables the WebDAV behavior.

</div>

</div>

<div class="feature" data-feature="webSockets" markdown="1">
