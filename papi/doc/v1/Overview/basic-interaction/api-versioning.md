---
title: "API versioning"
slug: "api-versioning"
hidden: false
createdAt: "2020-06-05T16:08:02.785Z"
updatedAt: "2020-06-10T13:58:03.101Z"
---
The API exposes several different versioning systems:

- The version of the API is specified as part of the URL path. The current API version is `v1`.

- The API supports different dated versions for the set of features available within a property's rule tree. For example, the most recent version is `v2020-03-04`. You can [freeze](#freezerf) and smoothly [update](#updaterf) the set of features that a property's rules apply to your content. Each behavior and criteria you invoke within your rules may independently increment versions from time to time, but the API only allows you to specify the snapshot version for the entire set of features.

    Reference documentation for the latest set of features is available in the [PAPI Feature Catalog Reference](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html). For information on features specified by older rule formats, see:

    - [PAPI Feature Catalog Reference, v2015-08-17](https://learn.akamai.com/en-us/api/core_features/property_manager/v2015-08-17.html)
    - [PAPI Feature Catalog Reference, v2016-11-15](https://learn.akamai.com/en-us/api/core_features/property_manager/v2016-11-15.html)
    - [PAPI Feature Catalog Reference, v2017-06-19](https://learn.akamai.com/en-us/api/core_features/property_manager/v2017-06-19.html)
    - [PAPI Feature Catalog Reference, v2018-02-27](https://learn.akamai.com/en-us/api/core_features/property_manager/v2018-02-27.html)
    - [PAPI Feature Catalog Reference, v2018-09-12](https://learn.akamai.com/en-us/api/core_features/property_manager/v2018-09-12.html)
    - [PAPI Feature Catalog Reference, v2019-07-25](https://learn.akamai.com/en-us/api/core_features/property_manager/v2019-07-25.html)
    - [PAPI Feature Catalog Reference, v2020-03-04](https://learn.akamai.com/en-us/api/core_features/property_manager/v2020-03-04.html)

- The API's [Build interface](#buildgroup) also provides details on the current software release and its accompanying _catalog_ of behaviors and criteria. These include version numbers and extraneous commit and build dates, which bear no relation to dated rule format versions. Don't rely on any of the internal version numbers this interface makes available.

Expect internal catalog release versions to update the most frequently, followed by less frequent rule format versions, followed by infrequent new API versions.