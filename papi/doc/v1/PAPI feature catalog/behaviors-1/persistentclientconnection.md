---
title: "persistentClientConnection"
slug: "persistentclientconnection"
hidden: false
createdAt: "2020-06-15T21:44:02.151Z"
updatedAt: "2020-06-15T21:44:02.151Z"
---
__Property Manager name__: [Persistent Connections: Client to Edge](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0060)

This [read-only behavior](#ro) activates _persistent connections_ between edge servers and clients, which allow for better performance and more efficient use of resources. Compare with the [`persistentConnection`](#persistentconnection) behavior, which configures persistent connections for the entire journey from origin to edge to client.  Contact Akamai Professional Services for help configuring either.

> __WARNING__: Disabling or removing this behavior may negatively
affect performance.

__Options__:

<div class="option" markdown="1" id="persistentClientConnection.enabled" >

- `enabled` (_boolean_): Enables the persistent connections behavior.

</div>

<div class="option" markdown="1" id="persistentClientConnection.timeout" >

- `timeout` (_duration string_): Specifies the timeout period after which edge server closes the persistent connection with the client, 500 seconds by default.

</div>

</div>

<div class="feature" data-feature="persistentConnection" markdown="1">
