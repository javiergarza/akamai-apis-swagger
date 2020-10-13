---
title: "Activation errors"
slug: "activation-errors"
hidden: false
createdAt: "2020-06-05T21:18:29.698Z"
updatedAt: "2020-06-05T21:18:29.698Z"
---
| Code | Type | Problem |
| :--- | :--- | :--- |
| [400](https://httpstatuses.com/400) | `activation/bad-notifyemails` | Activations require at least one email address specified in the `notifyEmails` array. [Learn more](#postpropertyactivations). |
| [400](https://httpstatuses.com/400) | `activation/cachewipe-error-possible` | The activation failed because an affected hostname migrated from one account to another. The error response provides details for when you can activate the property. |
| [400](https://httpstatuses.com/400) | `activation/missing-compliance-record-info` | For Akamai representatives activating customers' properties, `nonComplianceReason` cannot be `NONE` without having a valid `unitTested`, `peerReviewedBy`, and `customerEmail`. Either provide those values or change to a different `nonComplianceReason`. |
| [400](https://httpstatuses.com/400) | `activation/missing-compliance-record` | Akamai representatives must provide a _compliance record_ before activating a property on customers' behalf on the `production` network. |
| [400](https://httpstatuses.com/400) | `activation/self-peer-review` | Akamai representatives may not peer review their own activations. |
| [400](https://httpstatuses.com/400) | `activation/warnings-not-acknowledged` | Before proceeding, you need to acknowledge the activation warnings listed in the problem response. [Learn more](#postpropertyactivations). |
| [403](https://httpstatuses.com/403) | `property-version/already-activated` | The specified property version has already been activated. To make changes you need to first create a new property version. |
| [404](https://httpstatuses.com/404) | `activation-cancellation/not-found` | The activation you're trying to cancel is unknown. [Learn more](#deletepropertyactivation). |
| [422](https://httpstatuses.com/422) | `activation-cancellation/unprocessable-status` | The activation isn't in a `pending` state, so it can't be canceled. [Learn more](#deletepropertyactivation). |
| [422](https://httpstatuses.com/422) | `activation/already-activated` | The property version has already been activated. |
| [422](https://httpstatuses.com/422) | `activation/still-pending` | The property version is currently pending activation or deactivation. Wait until the operation is complete before starting another activation or deactivation. |
| [422](https://httpstatuses.com/422) | `deactivation/not-active-in-production` | The property isn't active on the `production` network, so you can't deactivate it. |
| [422](https://httpstatuses.com/422) | `deactivation/not-active-in-staging` | The property isn't active on the `staging` network, so you can't deactivate it. |
| [429](https://httpstatuses.com/429) | `rate-limit-exceeded.activations` | You made too many activations in the amount of time allowed for your contract. The problem response provides details on when you can request more activations. [Learn more](#ratelimiting). |
| [500](https://httpstatuses.com/500) | `activation-cancellation/cancel-error` | The platform couldn't cancel the activation. |
| [500](https://httpstatuses.com/500) | `activation/property_activation_failed` | The property activation failed.|
| [500](https://httpstatuses.com/500) | `deactivation/property_deactivation_failed` | The property deactivation failed.|