This sample illustrates Namespace scoped application relevant changes in the manifest.
so it has following changes compared to the azure vote sample
1) Scope is "namespace" in the manifest.
2) CreateUIDef takes targetnamespace as input.
3) ARM template Extension resource uses the namespace.