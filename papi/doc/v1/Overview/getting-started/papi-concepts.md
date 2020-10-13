---
title: "PAPI concepts"
slug: "papi-concepts"
hidden: false
createdAt: "2020-06-05T16:05:25.206Z"
updatedAt: "2020-06-10T03:12:21.188Z"
---
This section provides a road map of all the conceptual objects you deal with when interacting with PAPI and provides pointers to where you can learn more.

- __Accounts__. Akamai customers access all their services with an _account_ key. While administrators may have access to more than one account, in general they provision all their web assets under a single account within [Control Center](http://control.akamai.com). PAPI responses often return details about the account a client's authorization token is assigned to.

- __Groups__. Each account features a hierarchy of _groups_, which control access to properties and help consolidate reporting functions, typically mapping to an organizational hierarchy. Using either Control Center or the [Identity Management: User Administration API](https://learn.akamai.com/en-us/api/core_features/identity_management_user_admin/v2.html), account administrators can assign properties to specific groups, each with its own set of _users_ and accompanying _roles_. Your access to any given property depends on the role set for you in its group. Along with information about the _contract_, you need the group identifier to access virtually all of PAPI's resources.

- __Contracts__. Each account features one or more _contracts_, each of which has a fixed term of service during which specified Akamai _products_ and _modules_ are active. Along with information about the _group_, you need the contract identifier to access virtually all of PAPI's resources.

- __Products__. Each contract enables one or more _products_, each of which allows you to deploy web properties on the Akamai edge network and receive associated support from Akamai Professional Services. Products allow you to create new properties, CP codes, and edge hostnames. They also determine the baseline set of a property's rule behaviors.

- __Modules__. Modules are add-ons to products that may enable additional rule behaviors. Different products support different sets of modules. Your ability to specify any given rule behavior depends on the currently active product and associated modules. PAPI doesn't provide information directly about your selected modules, but it does allow you to determine the currently available [behaviors](#getavailablebehaviors) and [criteria](#getavailablecriteria) they enable.

These inputs allow you to deploy _properties_:

- __Properties__. Akamai's edge network caches your web assets near to servers that request them. A _property_, sometimes also referred to as a _configuration_, provides the main way to control how edge servers respond to various kinds of requests for those assets. Properties apply _rules_ to a set of _hostnames_, and you can only apply one property at a time to any given hostname. Each property is assigned to a product, which determines which rule _behaviors_ you can use. Each property's default rule needs a valid _CP code_ assigned to bill and report for the service.

- __Versions__. Each property has snapshot versions, which allows you to modify one instance of a property while another is activated. You can freely modify a property version, along with its component hostnames and rules, up until the point at which it's activated. Following activation, you need to create a new version to modify it further. You don't need to create a new property version for each modification you make. Each version uses an ascending integer as an ID, and features a time stamp, the username who modified it, and a log message.

- __Activations__. Once you're satisfied with any version of a property, an _activation_ deploys it, either to the Akamai staging or production network. You activate a specific version, but the same version can be activated separately more than once. You can either cancel an activation shortly after requesting it, or in many cases, use a _fast fallback_ feature within a matter of seconds to roll back a live activation to the previous activated version.

- __Metadata__. Once activated, each property is distributed to the Akamai network as an XML configuration file known as Akamai _metadata_. This low-level XML format combines information about the property's rules and hostnames. You can view metadata for each version regardless of activation, but you can only modify it indirectly.

- __Messages__. When you modify different aspects of a property, responses may include errors or warnings. An _error_ prevents you from activating a property version, but you can activate versions that yield less severe _warnings_. You may need to acknowledge each warning when you activate a version, but there's an option to skip this.

Properties include _rules_:

- __Rules__. Properties allow you to design _rules_ to respond to different kinds of requests. A rule consists of _criteria_ that identify which requests to process, and the _behaviors_ to apply to those requests. In addition to a top-level _default rule_ that determines overall behavior, you may include any number of your own rules, arranged in a tree structure up to five levels deep. The API provides an interface to the entire _rule tree_, not to each component rule. The API also doesn't support the _rule templates_ feature available in the Property Manager interface, since programming tools allow you to build your own rule templating system more flexibly.

- __Criteria__. Rules may specify an optional set of _criteria_, often referred to as _conditions_ or _matches_, based on which accompanying _behaviors_ execute. The [PAPI Feature Catalog Reference](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html) provides details on all criteria the API makes available. The [Rule Trees](#ruletrees) section clarifies how to arrange them within JSON payloads.

- __Behaviors__. Also referred to as _features_, these objects embedded within the rule tree instruct edge servers how to respond to requests. Your available set of behaviors depends on the selected product that enables the property. The [PAPI Feature Catalog Reference](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html) provides details on all behaviors the API makes available. The [Rule Trees](#ruletrees) section clarifies how to arrange them within JSON payloads.

- __Options__. Most rule behaviors and criteria specify a set of options that determine how they operate. For example, most criteria check for a specific `value` option, and most behaviors feature an `enabled` option that turns them on or off. Despite the name, some options are actually required, often depending on values set by other options.

- __Variables__. Many behavior and criteria options allow you to inject variable text that interprets at runtime on edge servers, typically based on details about the client request. PAPI allows you to reference a set of built-in system variables, and create your own set of variables based on various inputs. The section on [Variables](#variables) clarifies how to insert variables within a rule tree, and how to declare and modify your own variables.

- __Advanced features__. Most PAPI features translate to edge metadata in clearly prescribed ways. Functionality that falls outside what these predefined _behaviors_ and _criteria_ can do may be implemented as customized metadata. Advanced features are read-only, and require Akamai Professional Services to configure for you. In addition, you may request any feature with sensitive data to be _locked_ for you. See [Advanced and locked features](#advancedfeatures).

- __Custom behaviors__. Custom behaviors are read-only, like advanced features, but they're designed so that you can apply the same customized XML metadata to many properties at a time. See [Custom behaviors and overrides](#custombehaviors).

- __Custom overrides__. Like custom behaviors, custom overrides offer read-only access to XML metadata. They provide a final postprocessing step that executes at the end of the metadata, useful for restoring state modified within the rule tree.

- __CP codes__. You need a _content provider code_ to track any web traffic handled by Akamai servers. Akamai provides a CP code when you purchase a product, and you need it to activate any associated properties. You can generate additional CP codes, typically to implement more detailed billing and reporting functions, and to assign to customized properties. Each property requires at least one [`cpCode`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#cpcode) behavior as part of its default rule.

- __Schemas__. Some errors may result when a request isn't in the expected format. In that case, errors reference _request schemas_ that represent the expected structure formatted as a [JSON Schema](http://json-schema.org) object.

- __Rule formats__. You use rule formats to [freeze](#freezerf) or [update](#updaterf) the versioned set of behaviors and criteria a rule tree invokes. (Without this mechanism, behaviors and criteria would update automatically and generate unexpected errors.) PAPI tracks rule formats in a database keyed by _rule format version_ date strings. These reference _rule format schema_ objects, which specify the full set of behaviors and criteria available for a given product and the set of modules it may enable, as well as their allowed options and option values.

- __Client settings__. This API resource collects various configuration parameters for clients keyed to an authorization token.

Properties also include _hostnames_:

- __Hostnames__. Each property version applies its rules to requests for a set of hostnames under your control, such as `www.example.com` and `m.example.com`. This API interface specifies that set of hostnames. You also use this interface to specify whether each hostname only uses IPv4, or whether it also allows dual-stack IPv6 traffic.

- __Edge hostnames__. Each hostname assigned to a property corresponds to an _edge hostname_. Akamai uses DNS to map end-user requests from the hostname over to the edge hostname, then on to the most optimal edge server.  Akamai supports three types of edge hostname, depending on the level of security you need for your traffic: Standard TLS, Enhanced TLS, and Shared Certificate.  See [Create edge hostnames](#createedgehostnames) for guidance on deploying each type.  This interface specifies the full set of edge hostnames under your control, regardless of how they're assigned to various properties. Use PAPI to create and assign the edge hostnames. Use the [Edge Hostname API](https://developer.akamai.com/api/core_features/edge_hostnames/v1.html#getcertificatefortheedgehostname) (HAPI) to modify edge hostnames, or delete any that aren't referenced by an active property configuration.

- __Use cases__. When creating an edge hostname, you may have the option to assign a _use case_ to better optimize the traffic it will serve.  Use cases are read-only scenarios that Akamai provides for each product to help map different types of traffic across the Akamai edge network.  By default, edge hostnames are configured to deploy the same type of traffic for any Akamai product.  Assigning any available use case allows you to optimize different types of traffic. For example, if an edge hostname is deployed for the Download Delivery product, you can distinguish high-priority files that download in the foreground from low-priority background downloads.

- __CNAME__. For a property to serve live traffic, you need to first configure your DNS server so that requests for each hostname resolves to a corresponding edge hostname, the latter referred to as the _canonical name_. In turn, servers across the Akamai network use their own CNAME records to resolve these edge hostnames to more specific local server names and ultimately their IP addresses.

This most recent PAPI release supports a set _bulk_ operations to manage many properties' rule trees at once. See the [Bulk Search and Update](#bulksearchandupdate) section for details on this feature.

- __Bulk searches__. Bulk searches use a flexible JSON path-based query syntax to search across all your activated property versions' rule trees. After your search request, search results become available asynchronously for all matching property versions. They include JSON path expressions that locate all the rule tree behaviors and criteria you searched on, for use in a subsequent bulk patch operation.

- __Bulk versions__. You feed the results of a bulk search into another operation that creates new versions for the entire set of properties. This new set of versions becomes available asynchronously.

- __Bulk patches__. In a bulk patch operation, you use the JSON path locators in conjunction with JSON Patch operators to form a set of customized instructions to modify each property's rule tree. The results become available asynchronously.

- __Bulk activations__. After batch-updating a set of properties, you can asynchronously bulk activate them to the staging or production network.