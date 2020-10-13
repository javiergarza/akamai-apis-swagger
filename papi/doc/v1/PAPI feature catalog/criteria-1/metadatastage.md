---
title: "metadataStage"
slug: "metadatastage"
hidden: false
createdAt: "2020-06-15T22:22:31.957Z"
updatedAt: "2020-06-15T22:22:31.957Z"
---
__Property Manager name__: [Metadata Stage](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches how the current rule corresponds to low-level syntax elements in translated XML metadata, indicating progressive stages as each edge server handles the request and response.  To use this match, you need to be thoroughly familiar with how Akamai edge servers process requests. Contact your Akamai Technical representative if you need help, and test thoroughly on staging before activating on production.

__Options__:

- `matchOperator` (_enum string_): Tests whether the current rule `IS` or `IS_NOT` at the specified metadata stage.

- `value` (_enum string_): Specifies the metadata stage, one of the following:

    - `content-policy`: This stage calculates whether there is a     property configuration for this request.

    - `client-request`: When the Akamai server receives the request.

    - `client-request-body`: The Akamai server inspects the contents     of the request as a security check.

    - `ipa-response`: Occurs of a response is received from an     intermediate processing agent (IPA) server.

    - `cache-hit`: Content is cacheable and is already cached, but not     yet tested for freshness.

    - `forward-start`: A brief transitory stage while the Akamai     server selects a forward server or persistent connection.

    - `forward-request`: Immediately before the Akamai server tries to     connect to a forward server.

    - `forward-response`: After the forward server responds. Occurs     for content received from an origin server, for example when not     caching it.

    - `client-response`: Occurs prior to constructing a response.

    - `client-done`: Occurs after the response completes.
