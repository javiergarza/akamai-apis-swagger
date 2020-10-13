---
title: "persistentConnection"
slug: "persistentconnection"
hidden: false
createdAt: "2020-06-15T21:44:25.634Z"
updatedAt: "2020-06-15T21:44:25.634Z"
---
__Property Manager name__: [Persistent Connections: Edge to Origin](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0060)

A [read-only behavior](#ro) that enables more efficient _persistent connections_ from origin to edge server to client. Compare with the [`persistentClientConnection`](#persistentclientconnection) behavior, which customizes persistent connections from edge to client. Contact Akamai Professional Services for help configuring either.

> __WARNING__: Disabling this behavior wastes valuable browser
resources. Leaving connections open too long makes them vulnerable to
attack. Avoid both of these scenarios.

__Options__:

<div class="option" markdown="1" id="persistentConnection.enabled" >

- `enabled` (_boolean_): Enables persistent connections.

</div>

<div class="option" markdown="1" id="persistentConnection.timeout" >

- `timeout` (_duration string_): Specifies the timeout period after which edge server closes a persistent connection.

</div>

</div>

<div class="feature" data-feature="personallyIdentifiableInformation" markdown="1">
