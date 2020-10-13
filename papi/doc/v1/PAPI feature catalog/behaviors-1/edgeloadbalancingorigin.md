---
title: "edgeLoadBalancingOrigin"
slug: "edgeloadbalancingorigin"
hidden: false
createdAt: "2020-06-15T21:20:11.959Z"
updatedAt: "2020-06-15T21:20:11.959Z"
---
__Property Manager name__: [Edge Load Balancing: Origin Definition](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0040)

The [Edge Load Balancing](http://control.akamai.com/dl/customers/other/Edge_Load_Balancing/Terra_Alta_Edge_Load_Balancing.pdf) module allows you to implement groups of data centers featuring load balancing, session persistence, and real-time dynamic failover. Enabling ELB routes requests contextually based on location, device, or network, along with optional rules you specify.

This behavior specifies the data center's origin, and must be paired in the same rule with at least one [`edgeLoadBalancingDataCenter`](#edgeloadbalancingdatacenter) behavior, which provides details about a particular data center. An _origin_ is an abstraction that helps group a logical set of a website or application. It potentially includes information about many data centers and cloud providers, as well as many end points or IP addresses for each data center. To specify an ELB origin, you must have configured an [`origin`](#origin) behavior whose `type` is set to `elb_origin_group`.

__Options__:

<div class="option" markdown="1" id="edgeLoadBalancingOrigin.id" >

- `id` (_string_): Specifies a unique descriptive string for this ELB origin. The value must match the `origin_id` specified by the [`edgeLoadBalancingDataCenter`](#edgeloadbalancingdatacenter) behavior associated with this origin.

</div>

<div class="option" markdown="1" id="edgeLoadBalancingOrigin.description" >

- `description` (_string_): Provides a description for the ELB origin, for your own reference.

</div>

<div class="option" markdown="1" id="edgeLoadBalancingOrigin.hostname" >

- `hostname` (_string_): Specifies the hostname associated with the ELB rule.

</div>

<div class="option" markdown="1" id="edgeLoadBalancingOrigin.enableSessionPersistence" >

- `enableSessionPersistence` (_boolean_): When enabled, allows you to specify a cookie to pin the user's browser session to one data center. When disabled, ELB's default load balancing may send users to various data centers within the same session.

</div>

<div class="option" markdown="1" id="edgeLoadBalancingOrigin.cookieName" >

- `cookieName` (_string_): With `enableSessionPersistence` enabled, this specifies the name of the cookie that marks users' persistent sessions. The accompanying [`edgeLoadBalancingDataCenter`](#edgeloadbalancingdatacenter) behavior's `description` option specifies the cookie's value.

</div>

</div>

<div class="feature" data-feature="edgeOriginAuthorization" markdown="1">
