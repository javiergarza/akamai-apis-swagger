---
title: "allowTransferEncoding"
slug: "allowtransferencoding"
hidden: false
createdAt: "2020-06-15T20:39:22.218Z"
updatedAt: "2020-06-15T20:39:22.218Z"
---
__Property Manager name__: [Chunked Transfer Encoding](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0015)

Controls whether to allow or deny Chunked Transfer Encoding (CTE) requests to pass to your origin. If your origin supports CTE, you should enable this behavior. This behavior also protects against a known issue when pairing [`http2`](#http2) and [`webdav`](#webdav) behaviors within the same rule tree, in which case it is required.

__Options__:

<div class="option" markdown="1" id="allowTransferEncoding.enabled" >

- `enabled` (_boolean_): Allows Chunked Transfer Encoding requests.

</div>

</div>

<div class="feature" data-feature="apiPrioritization" markdown="1">
