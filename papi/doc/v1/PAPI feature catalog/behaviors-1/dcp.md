---
title: "dcp"
slug: "dcp"
hidden: false
createdAt: "2020-06-15T21:06:16.530Z"
updatedAt: "2020-06-15T21:06:16.530Z"
---
__Property Manager name__: [IoT Edge Connect](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9024)

The [Internet of Things: Edge Connect](https://learn.akamai.com/en-us/products/web_performance/iot_edge_connect.html) product allows connected users and devices to communicate on a publish-subscribe basis within reserved namespaces. (The [IoT Edge Connect API](https://developer.akamai.com/api/web_performance/iot_edge_connect/v1.html) allows programmatic access.) This behavior allows you to select previously reserved namespaces and set the protocols for users to publish and receive messages within these namespaces.  Use the [`verifyJsonWebTokenForDcp`](#verifyjsonwebtokenfordcp) behavior to control access.

__Options__:

<div class="option" markdown="1" id="dcp.enabled" >

- `enabled` (_boolean_): Enables IoT Edge Connect.

</div>

<div class="option" markdown="1" id="dcp.namespaceId" >

- `namespaceId` (_string_): Specifies the globally reserved name for a specific configuration. It includes authorization rules over publishing and subscribing to logical categories known as _topics_. This provides a root path for all topics defined within a namespace configuration.  You can use the [IoT Edge Connect API](https://developer.akamai.com/api/web_performance/iot_edge_connect/v1.html) to configure access control lists for your namespace configuration.

</div>

<div class="option" markdown="1" id="dcp.tlsenabled" >

- `tlsenabled` (_boolean_): When enabled, you can publish and receive messages over a secured MQTT connection on port 8883.

</div>

<div class="option" markdown="1" id="dcp.wsenabled" >

- `wsenabled` (_boolean_): When enabled, you can publish and receive messages through a secured MQTT connection over WebSockets on port 443.

</div>

<div class="option" markdown="1" id="dcp.gwenabled" >

- `gwenabled` (_boolean_): When enabled, you can publish and receive messages over a secured HTTP connection on port 443.

</div>

</div>

<div class="feature" data-feature="dcpAuthHMACTransformation" markdown="1">
