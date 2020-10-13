---
title: "JSON request schema"
slug: "json-request-schema"
hidden: false
createdAt: "2020-06-05T21:12:26.489Z"
updatedAt: "2020-06-05T21:12:26.490Z"
---
Errors about malformed data typically reference _schema_ objects that
describe whichever resource you're trying to interact with. PAPI
provides a separate [Request schema interface](#schemasgroup) for
these objects that reference specific schema files. For example, this
schema describes the expected data structure when creating a new edge
hostname:

```
GET /papi/v1/schemas/request/EdgeHostnamesPostRequestV0.json
```