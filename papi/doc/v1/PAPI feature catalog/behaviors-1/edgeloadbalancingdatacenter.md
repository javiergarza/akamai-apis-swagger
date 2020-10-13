---
title: "edgeLoadBalancingDataCenter"
slug: "edgeloadbalancingdatacenter"
hidden: false
createdAt: "2020-06-15T21:19:47.593Z"
updatedAt: "2020-06-15T21:19:47.593Z"
---
__Property Manager name__: [Edge Load Balancing: Data Center](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0039)

The [Edge Load Balancing](http://control.akamai.com/dl/customers/other/Edge_Load_Balancing/Terra_Alta_Edge_Load_Balancing.pdf) module allows you to specify groups of data centers that implement load balancing, session persistence, and real-time dynamic failover. Enabling ELB routes requests contextually based on location, device, or network, along with optional rules you specify.

This behavior specifies details about a data center, and must be paired in the same rule with an [`edgeLoadBalancingOrigin`](#edgeloadbalancingorigin) behavior, which specifies its origin. An _origin_ is an abstraction that helps group a logical set of a website or application. It potentially includes information about many data centers and cloud providers, as well as many end points or IP addresses for each data center. More than one data center can thus refer to the same origin.

__Options__:

<div class="option" markdown="1" id="edgeLoadBalancingDataCenter.originId" >

- `originId` (_string_): Corresponds to the `id` specified by the [`edgeLoadBalancingOrigin`](#edgeloadbalancingorigin) behavior associated with this data center.

</div>

<div class="option" markdown="1" id="edgeLoadBalancingDataCenter.description" >

- `description` (_string_): Provides a description for the ELB data center, for your own reference.

</div>

<div class="option" markdown="1" id="edgeLoadBalancingDataCenter.hostname" >

- `hostname` (_string_): Specifies the data center's hostname.

</div>

<div class="option" markdown="1" id="edgeLoadBalancingDataCenter.cookieName" >

- `cookieName` (_string_): If using session persistence, this specifies the value of the cookie named in the corresponding [`edgeLoadBalancingOrigin`](#edgeloadbalancingorigin) behavior's `cookie_name` option.

</div>

<div class="option" markdown="1" id="edgeLoadBalancingDataCenter.enableFailover" >

- `enableFailover` (_boolean_): When enabled, allows you to specify failover rules.

</div>

<div class="option" markdown="1" id="edgeLoadBalancingDataCenter.ip" >

- `ip` (_string_): With `enableFailover` enabled, specifies this data center's IP address.

</div>

<div class="option" markdown="1" id="edgeLoadBalancingDataCenter.failoverRules" >

- `failoverRules` (_array_): With `enableFailover` enabled, provides up to four failover rules to apply in the specified order. These rules appear as objects with the following fields:

    - `modify_request` (_boolean_): When enabled, allows you to modify     the request's hostname or path.

    - `override_hostname` (_boolean_): When enabled, overrides the     request's hostname with the `failover_hostname`.

    - `failover_hostname`: The hostname of the data center to fail over     to.

    - `context_root`: Specifies the path to use in the forwarding     request, typically the root (`/`) when failing over to a different     data center, or a full path such as `/static/error.html` when     failing over to an error page.

    - `absolute_path` (_boolean_): If enabled, the path specified by     `context_root` is interpreted as an absolute server path, for     example to reference a site-down page. If disabled, the path is     appended to the request.

</div>

</div>

<div class="feature" data-feature="edgeLoadBalancingOrigin" markdown="1">
