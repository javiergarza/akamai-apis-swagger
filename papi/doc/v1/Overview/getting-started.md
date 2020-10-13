---
title: "Get started with PAPI"
slug: "getting-started"
excerpt: "Use PAPI to manage how Akamai handles requests, objects, and responses for your website."
hidden: false
createdAt: "2020-05-06T17:19:11.431Z"
updatedAt: "2020-06-11T13:01:58.097Z"
---
The Property Manager API (_PAPI_) offers a programmatic interface to manage how Akamai's edge servers process requests, responses, and objects over the Akamai platform. A distributed _property_ configuration collects all the rules for how to process end-user requests for your web assets. Like Property Manager in [Akamai Control Center](https://control.akamai.com), this API lets you modify your property configurations and activate them on Akamai staging or production networks. The API allows you to access the same features rapidly and flexibly using your own tools. PAPI allows you to generate properties dynamically, associate them with generated hostnames, and create new CP codes to report on your content's traffic. This most recent PAPI release provides _bulk update_ capabilities, allowing you to modify and activate many properties at once.