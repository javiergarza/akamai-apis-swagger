---
title: "standardTLSMigration"
slug: "standardtlsmigration"
hidden: false
createdAt: "2020-06-15T22:04:15.638Z"
updatedAt: "2020-06-15T22:04:15.638Z"
---
__Property Manager name__: [Standard TLS Migration](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0200)

Migrates traffic to Standard TLS. Apply this behavior within the default rule or any [`hostname`](#hostname) match.  In some cases you may need to apply this along with the [`standardTLSMigrationOverride`](#standardtlsmigrationoverride) behavior.

__Options__:

<div class="option" markdown="1" id="standardTLSMigration.enabled" >

- `enabled` (_boolean_): Allows migration to Standard TLS.

</div>

<div class="option" markdown="1" id="standardTLSMigration.migrationFrom" >

- `migrationFrom` (_enum string_): Whether you are migrating traffic from `ENHANCED_SECURE` TLS, from a `SHARED_CERT`, or `NON_SECURE` traffic.

</div>

<div class="option" markdown="1" id="standardTLSMigration.allowHTTPSUpgrade" >

- `allowHTTPSUpgrade` (_boolean_): With `migrationFrom` set to `NON_SECURE`, allows temporary upgrade of HTTP traffic to HTTPS.

</div>

<div class="option" markdown="1" id="standardTLSMigration.allowHTTPSDowngrade" >

- `allowHTTPSDowngrade` (_boolean_): With `migrationFrom` set to `NON_SECURE`, allow temporary downgrade of HTTPS traffic to HTTP. This removes various `Origin`, `Referer`, `Cookie`, `Cookie2`, `sec-*` and `proxy-*` headers from the request to origin.

</div>

<div class="option" markdown="1" id="standardTLSMigration.migrationStartTime" >

- `migrationStartTime` (_ISO 8601 format date/time string_): With either `allowHTTPSUpgrade` or `allowHTTPSDowngrade` enabled, specifies when to start migrating the cache.

</div>

<div class="option" markdown="1" id="standardTLSMigration.migrationDuration" >

- `migrationDuration` (_number_): With either `allowHTTPSUpgrade` or `allowHTTPSDowngrade` enabled, specifies the number of days to migrate the cache.

</div>

<div class="option" markdown="1" id="standardTLSMigration.cacheSharingStartTime" >

- `cacheSharingStartTime` (_ISO 8601 format date/time string_): With `migrationFrom` set to `ENHANCED_SECURE`, specifies when to start cache sharing.

</div>

<div class="option" markdown="1" id="standardTLSMigration.cacheSharingDuration" >

- `cacheSharingDuration` (_number_): With `migrationFrom` set to `ENHANCED_SECURE`, specifies the number cache sharing days.

</div>

<div class="option" markdown="1" id="standardTLSMigration.isCertificateSNIOnly" >

- `isCertificateSNIOnly` (_boolean_): With `migrationFrom` set to `ENHANCED_SECURE`, sets whether your new certificate is SNI-only.

</div>

<div class="option" markdown="1" id="standardTLSMigration.isTieredDistributionUsed" >

- `isTieredDistributionUsed` (_boolean_): With `migrationFrom` set to `NON_SECURE`, allows you to align traffic to various [`tieredDistribution`](#tiereddistribution) areas.

</div>

<div class="option" markdown="1" id="standardTLSMigration.tdLocation" >

- `tdLocation` (_enum string_): With `isTieredDistributionUsed` enabled, specifies the [`tieredDistribution`](#tiereddistribution) location, either `EUROPE`, `APAC` (Asia and Pacific), `AUSTRALIA`, `US_WEST`, `US_CENTRAL`, `US_EAST`, `GLOBAL`, or `GLOBAL_LEGACY`.

</div>

</div>

<div class="feature" data-feature="standardTLSMigrationOverride" markdown="1">
