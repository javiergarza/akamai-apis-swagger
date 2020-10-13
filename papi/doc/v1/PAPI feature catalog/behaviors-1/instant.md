---
title: "instant"
slug: "instant"
hidden: false
createdAt: "2020-06-15T21:32:26.158Z"
updatedAt: "2020-06-15T21:32:26.158Z"
---
__Property Manager name__: [Akamai Instant](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0110)

The Instant feature allows you to prefetch content to the edge cache by adding link relation attributes to markup. For example:

```xml
<a href="page2.html" rel="Akamai-prefetch">Page 2</a>
```

Default link relation values are `prefetch` and `Akamai-prefetch`. Applies only to HTML elements that may specify an external file: `<a>`, `<base>`, `<img>`, `<script>`, `<input>`, `<link>`, `<table>`, `<td>`, or `<th>`. (For the latter three, some legacy browsers support a nonstandard `background` image attribute.)

This behavior provides an alternative to the [`prefetch`](#prefetch) and [`prefetchable`](#prefetchable) behaviors, which allow you to configure more general prefetching behavior outside of markup.

__Options__:

<div class="option" markdown="1" id="instant.prefetchCacheable" >

- `prefetchCacheable` (_boolean_): When enabled, applies prefetching only to objects already set to be cacheable, for example using the [`caching`](#caching) behavior. Only applies to content with the [`tieredDistribution`](#tiereddistribution) behavior enabled.

</div>

<div class="option" markdown="1" id="instant.prefetchNoStore" >

- `prefetchNoStore` (_boolean_): Allows otherwise non-cacheable `no-store` content to prefetch if the URL path ends with `/` to indicate a request for a default file, or if the extension matches the value of the `prefetchNoStoreExtensions` option. Only applies to content with the [`sureRoute`](#sureroute) behavior enabled.

</div>

<div class="option" markdown="1" id="instant.prefetchNoStoreExtensions" >

- `prefetchNoStoreExtensions` (_array of string values_): Specifies a set of file extensions for which the `prefetchNoStore` option is allowed.

</div>

<div class="option" markdown="1" id="instant.prefetchHtml" >

- `prefetchHtml` (_boolean_): When enabled, allows edge servers to prefetch additional HTML pages while pages that link to them are being delivered. This only applies to links from `<a>` or `<link>` tags with the appropriate link relation attribute.

</div>

<div class="option" markdown="1" id="instant.customLinkRelations" >

- `customLinkRelations` (_array of string values_): Specify link relation values that activate the prefetching behavior. For example, specifying `fetch` allows you to use shorter `rel="fetch"` markup.

</div>

</div>

<div class="feature" data-feature="instantConfig" markdown="1">
