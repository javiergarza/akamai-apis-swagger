---
title: "allHttpInCacheHierarchy"
slug: "allhttpincachehierarchy"
hidden: false
createdAt: "2020-06-15T20:26:06.952Z"
updatedAt: "2020-06-15T20:32:41.411Z"
---
__Property Manager name__: [Allow All Methods on Parent Servers](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9071)

Allow all HTTP request methods to be used for the edge's parent servers, useful to implement features such as [Site Shield](https://learn.akamai.com/en-us/products/cloud_security/site_shield.html), [SureRoute](http://www.akamai.com/dl/feature_sheets/fs_edgesuite_sureroute.pdf), and Tiered Distribution. (See the [`siteShield`](#siteshield), [`sureRoute`](#sureroute), and [`tieredDistribution`](#tiereddistribution) behaviors.)

__Options__:

<div class="option" markdown="1" id="allHttpInCacheHierarchy.enabled" >

- `enabled` (_boolean_): Enables all HTTP requests for parent servers in the cache hierarchy.

</div>
