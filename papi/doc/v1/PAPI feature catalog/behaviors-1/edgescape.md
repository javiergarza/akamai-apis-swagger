---
title: "edgeScape"
slug: "edgescape"
hidden: false
createdAt: "2020-06-15T21:21:32.071Z"
updatedAt: "2020-06-15T21:21:32.071Z"
---
__Property Manager name__: [Content Targeting](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0043)

[EdgeScape](https://control.akamai.com/dl/customers/ESCAPE/EdgeScape_users_guide.pdf)
allows you to customize content based on the end user's geographic
location or connection speed. When enabled, the edge server sends a
special `X-Akamai-Edgescape` header to the origin server encoding
relevant details about the end-user client as key-value pairs.

__Options__:

<div class="option" markdown="1" id="edgeScape.enabled" >

- `enabled` (_boolean_): When enabled, sends the `X-Akamai-Edgescape` request header to the origin.

</div>

</div>

<div class="feature" data-feature="edgeSideIncludes" markdown="1">
