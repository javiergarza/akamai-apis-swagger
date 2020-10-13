---
title: "Basic workflow"
slug: "basic-workflow"
hidden: false
createdAt: "2020-06-05T16:06:33.654Z"
updatedAt: "2020-06-10T03:12:21.181Z"
---
This section summarizes PAPI's high-level workflow patterns.  See the [API summary](#apisummary) for details on all of PAPI's operations.

Before running many other operations, you need a set of [contract](#getcontracts) and [group](#getgroups) identifiers. Before creating new objects, you also need a relevant [product](#getproducts) identifier.  The ID values allow you to access these interfaces:

- Use the [CP codes](#cpcodesgroup) interface if you want to generate CP codes, which you assign to a property's rule tree, or to find out which products existing CP codes are assigned to.

- Use the [Edge hostnames](#edgehostnamesgroup) interface to deploy new hostnames on Akamai edge servers before assigning them to properties.

- Use the [Properties](#propertiesgroup) interface if you want to list available properties or create new properties.

Once you have a _property_ identifier, you can run many operations with no need for contract and group identifiers. You may be able to design client code to avoid running other operations to derive those values. You may also be able to flexibly change how your properties are provisioned, independent of your client code. With a property identifier available, you can access these interfaces:

- Use the [Properties](#propertiesgroup) interface to view or remove specific properties.

- Use the [Property versions](#propertyversionsgroup) interface if you want to create or access versioned property instances.

- Use [Property activations](#propertyactivationsgroup) to deploy property versions to make your content available on Akamai's edge network.

- Use [Property version rules](#propertyversionrulesgroup) if you want to access or modify the property's rule tree.

- Use [Property version hostnames](#propertyversionhostnamesgroup) if you want to assign or reassign any set of available edge hostnames.

- If you want to know which features you can assign within a rule tree, run the [List available behaviors](#getavailablebehaviors) and [List available criteria](#getavailablecriteria) operations.

PAPI also provides these additional features:

- Use [Search properties](#postfindbyvalue) as a quick way to identify currently active property versions.

- If you want more details about the underlying features that are applied as part of a property's rule tree, run [List rule formats](#getruleformats) to get available versions for each feature set, and [Get a rule format's schema](#getruleformatschema) to validate a rule tree against a specific rule format's supported features.

- To control which rule format is assigned to a property, see [Freeze a rule tree's feature set](#freezerf) and [Update rules to a newer set of features](#updaterf), both of which are based on the operations that read and write rule trees. See [Update client settings](#putclientsettings) to set the default rule format for new properties.

- If you want to apply a common set of customized XML metadata to more than one property, see the [Custom behaviors](#custombehaviorsgroup) and [Custom overrides](#customoverridesgroup) interfaces.

See [PAPI concepts](#papiconcepts) to learn more about how these resources relate to each other. For information on specific operations, see the [API summary](#apisummary).