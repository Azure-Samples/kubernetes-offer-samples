---
page_type: sample
languages:
- yaml
- json
products:
- azure-kubernetes-service
- azure-marketplace
---

# Array input sample for Kubernetes Marketplace Offer

This sample demonstrates how to override array inside values.yaml for Kubernetes Marketplace Offer

In helm, there are 2 different ways to override array inside values.yaml
- --set cpuLimit='{1,1.5}'
- --set memoryLimit[0]=512Mi --set memoryLimit[1]=0.75Gi


Both ways can be used in Kubernetes Marketplace Offer. However, the first way is preferred if you want to provide more flexibility to number of elements.

## ARM Template

The following code snipnet shows how the values are passed as configuration settings:

```json
"configurationSettings": {
    "title": "[parameters('app-title')]",
    "value1": "[parameters('app-value1')]",
    "value2": "[parameters('app-value2')]",
    "cpuLimit": "[parameters('app-cpuLimit')]",
    "memoryLimit[0]": "[parameters('app-memoryLimit0')]",
    "memoryLimit[1]": "[parameters('app-memoryLimit1')]"
},
```

## UI Definition

The following code snippet shows how the inputs can be defined in the UI definition:

```json
{
    "name": "cpuLimit",
    "type": "Microsoft.Common.TextBox",
    "label": "CPU Limit",
    "toolTip": "This will replace the cpuLimit's value inside your values.yaml",
    "defaultValue": "{0.5, 1.0}",
    "constraints": {
        "required": true,
        "regex": "^{[0-9.]+, [0-9.]+}$",
        "validationMessage": "Must be in the format for {#.#, #.#}"
    }
},
{
    "name": "memoryLimit0",
    "type": "Microsoft.Common.TextBox",
    "label": "Memory Request",
    "toolTip": "This will replace the memoryLimit's array index 0 value inside your values.yaml",
    "defaultValue": "0.25Gi",
    "constraints": {
        "required": true,
        "regex": "^[0-9.]+[EPTGMK]i$",
        "validationMessage": "Must be in the format for #.#[EPTGMK]i"
    }
},
{
    "name": "memoryLimit1",
    "type": "Microsoft.Common.TextBox",
    "label": "Memory Limit",
    "toolTip": "This will replace the memoryLimit's array index 1 value inside your values.yaml",
    "defaultValue": "0.5Gi",
    "constraints": {
        "required": true,
        "regex": "^[0-9.]+[EPTGMK]i$",
        "validationMessage": "Must be in the format for #.#[EPTGMK]i"
    }
}
```

## Helm chart

To have azure-vote to consume the changes made in this sample, the following code snippet shows how the values are used in the helm chart:

deployments.yaml
```yaml
requests:
cpu: {{ index .Values.cpuLimit 0}}
memory: {{ index .Values.memoryLimit 0}}
limits:
cpu: {{ index .Values.cpuLimit 1}}
memory: {{ index .Values.memoryLimit 1}}
```

values.yaml
```yaml
# CPU request and limit array
cpuLimit:
  - 0.25
  - 0.5

# Memory request and limit array
memoryLimit:
  - 128Mi
  - 256Mi
```


## Note
This sample includes only a small subset of the files. The files in this sample folder contains the additional changes required on top of the base sample application '[k8s-offer-azure-vote](../k8s-offer-azure-vote/)'.