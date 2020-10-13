---
title: "Create a new edge hostname"
slug: "post_edgehostnames"
excerpt: "This operation creates a new edge\nhostname.  As detailed in the sections below, you can use three\napproaches to secure new edge hostnames:\n[Standard TLS](doc:standard-tls-edge-hostname), [Enhanced TLS](doc:enhanced-tls-edge-hostname), or a\n[Shared Certificate](doc:shared-certificate-edge-hostname).\nYou can [assign a use case](#assignausecase) mapping profile\nto optimize the hostname to serve specific types of traffic.\nFor more information, see\n[Create edge hostnames using PAPI](http://learn.akamai.com/en-us/api/learn_akamai/getting_started_with_akamai_developers/core_features/create_edgehostnames.html).\nOnce the hostname is active, you can\n[Update a property's hostnames](#putpropertyversionhostnames)\nto assign it to a property. After you\n[activate a property](#postpropertyactivations), modifying your\nDNS to map the origin hostname to the edge hostname ultimately\nenables traffic on the property. For details, see\n[Enable traffic for a new edge hostname](doc:enable-traffic-for-a-new-edge-hostname).\nUse the [Edge Hostname API](https://developer.akamai.com/api/core_features/edge_hostnames/v1.html#getcertificatefortheedgehostname)\n(HAPI) to modify edge hostnames, or delete any that aren't\ncurrently assigned to an active property configuration."
hidden: false
createdAt: "2020-06-05T12:55:45.977Z"
updatedAt: "2020-06-05T21:53:03.171Z"
---
