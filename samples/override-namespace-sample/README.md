---
page_type: sample
languages:
- yaml
- json
products:
- azure-kubernetes-service
- azure-marketplace
---

# override namespace settings sample

This folder contains samples that shows how ISV can provide the ability to override namespace settings in UIDefinition and consume them in ARM Template so that they can be passed to Kubernetes Extension Type as Configuration Settings.

## ARM Template change
First you will need to add the parameter 'namespace' in the parameters section of the ARM template. This parameter will be used to override the namespace settings in kubneretes extension type, and value can be passed in from UIDefinition.
```json
"namespace": {
    "type": "string",
    "defaultValue": "azure-vote"
}
```
Set the default value to be the same as default in manifest file (if any) and the default value in UIDefinition to ensure consist experience for both ARM template, Portal and CLI installation.

In cluster scope setting, the additional properties you will need to add in ARM template are:
```json
"scope": {
    "cluster": {
        "releaseNamespace": "[parameters('namespace')]"
    }
}
```
sample file: [clusterscope-mainTemplate.json](./clusterscope-mainTemplate.json)

In namespace scope setting, the default behavior of the namespace would be using the extension type resource name. If you want to override the namespace settings to a different value, you will need to add the additional properties in ARM template:
```json
"scope": {
    "namespace": {
        "targetNamespace": "[parameters('namespace')]"
    }
}
```
sample file: [namespacescope-mainTemplate.json](./namespacescope-mainTemplate.json)

## Note
- The manifest file default scope should match the scope in the ARM template.
- This sample includes only a small subset of the files. The files in this sample folder contains the additional changes required on top of the base sample application '[k8s-offer-azure-vote](../k8s-offer-azure-vote/)'.