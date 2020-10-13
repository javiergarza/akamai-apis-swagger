---
title: "webApplicationFirewall"
slug: "webapplicationfirewall"
hidden: false
createdAt: "2020-06-15T22:12:39.105Z"
updatedAt: "2020-06-15T22:12:39.105Z"
---
__Property Manager name__: [Web Application Firewall](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9059)

The [Web Application Firewall](http://www.akamai.com/html/solutions/web-application-firewall.html) behavior implements a suite of security features that blocks threatening HTTP and HTTPS requests. Use it as your primary firewall, or in addition to existing security measures.  Only one referenced configuration is allowed per property, so this behavior typically belongs as part of its default rule.

__Options__:

<div class="option" markdown="1" id="webApplicationFirewall.firewallConfiguration" >

- `firewallConfiguration` (_object_): An object featuring details about your firewall configuration, for example:

        "firewallConfiguration": {
            "configId"          : 1,
            "productionStatus"  : "Active",
            "productionVersion" : 1,
            "stagingStatus"     : "Active",
            "stagingVersion"    : 1
        }

</div>

</div>

<div class="feature" data-feature="webdav" markdown="1">
