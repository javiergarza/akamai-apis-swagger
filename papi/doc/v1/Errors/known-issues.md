---
title: "Known issues"
slug: "known-issues"
hidden: false
createdAt: "2020-06-05T21:06:03.443Z"
updatedAt: "2020-06-10T03:12:18.042Z"
---
These known issues may affect your ability to use the Property Manager API:

- Large rule trees that take more than 5 minutes to validate may time out with a 500 error. As a workaround, try to create smaller configurations targeting smaller sets of hostnames. The less executable logic each configuration contains, the less time it takes to validate it.

- If you associate PAPI credentials with a user who has access to more than one portal account, attempts to create edge hostnames result in authorization errors.

- If you create a property with an empty set of hostnames, running [List property version hostnames](https://papi-akamai.readme.io/reference/propertiespropertyidversionspropertyversionhostnames#get_properties-propertyid-versions-propertyversion-hostnames) results in a 500 error.

- Some streaming media configurations aren't supported. PAPI supports all properties supported by Property Manager.

- Before using PAPI, you may need to upgrade any properties created with the older Configuration Manager.  You upgrade properties within [Control Center](https://control.akamai.com).