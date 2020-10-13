---
title: "Metadata errors"
slug: "metadata-errors"
hidden: false
createdAt: "2020-06-05T21:21:37.277Z"
updatedAt: "2020-06-05T21:21:37.277Z"
---
These errors may be listed within [Rule](#rule) objects, and
may prevent you from activating the property version:

| Type | Description |
| :--- | :--- |
| `advanced_override_badly_formatted_xml` | The advanced override metadata features invalid XML. |
| `advanced_override_metadata_enabled` | A rule specifies advanced metadata that potentially overrides other configurations specified in previous rules. |
| `badly_formatted_xml` | The behavior specifies invalid XML metadata. |
| `conflicting_xml` | A behavior may not work as expected because [`advanced`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#advanced) metadata may cause conflicts. |