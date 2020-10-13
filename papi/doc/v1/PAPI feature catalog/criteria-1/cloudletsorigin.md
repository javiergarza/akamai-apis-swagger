---
title: "cloudletsOrigin"
slug: "cloudletsorigin"
hidden: false
createdAt: "2020-06-15T22:18:24.283Z"
updatedAt: "2020-06-15T22:18:24.283Z"
---
__Property Manager name__: [Conditional Origin ID](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0027)

Allows Cloudlets Origins, referenced by label, to define their own criteria to assign custom origin definitions. The criteria may match, for example, for a specified percentage of requests defined by the cloudlet to use an alternative version of a website.

This criteria must be paired with a sibling [`origin`](#origin) definition.  It should not appear with any other criteria, and an [`allowCloudletsOrigins`](#allowcloudletsorigins) behavior must appear within a parent rule.

__Options__:

- `originId` (_string_): The Cloudlets Origins identifier, limited to alphanumeric and underscore characters.
