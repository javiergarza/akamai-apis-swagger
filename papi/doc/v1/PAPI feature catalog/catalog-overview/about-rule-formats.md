---
title: "About rule formats"
slug: "about-rule-formats"
hidden: false
createdAt: "2020-06-15T22:34:55.600Z"
updatedAt: "2020-06-15T22:34:55.600Z"
---
Akamai often modifies PAPI features, each time deploying a new
internal version of the feature. If you are using the Property Manager
interface in [Akamai Control Center](http://control.akamai.com), you
may be prompted to upgrade to new feature versions as they become
available. PAPI does not support this system of selective updates for
each feature. Instead, PAPI's rule objects are simply versioned as a
whole. These versions, which update infrequently, are known as _rule
formats_.

Rule formats are versioned by date, for example, `v2017-06-19`, or the
most recent rule format titled `latest`.  When you specify a feature
within a rule tree assigned with the `v2017-06-19` rule format, PAPI
uses the most recent version of the feature that rule format supports.
Only by updating to a newer rule format such as `v2018-02-27` do you
upgrade to new versions of various features, which often allow an
expanded set of options and enumerations.

PAPI users should assign the most recent dated rule format to freeze
the set of features. Otherwise if you assign the `latest` rule format,
features update automatically to their most recent version. This may
abruptly result in errors if JSON objects your rules specify no longer
comply with the most recent feature's set of requirements.  PAPI
provides a more stable path to update rule formats that fixes these
requirements for you.  For more information, see
[Update rules to a newer set of features](https://learn.akamai.com/en-us/api/core_features/property_manager/v1.html#updaterf).

See
[Understanding rule formats](https://learn.akamai.com/en-us/api/core_features/property_manager/v1.html#understandingruleformats)
for more information on PAPI's rule format versioning system.