---
page_type: sample
languages:
- yaml
- json
products:
- azure-kubernetes-service
- azure-marketplace
---

# Connected and Managed Cluster sample

This folder contains samples that show how an ISV can prepare a Kubernetes application that can be installed on Azure Kubernetes Service (AKS) clusters or Azure Arc-enabled Kubernetes Clusters.

Note:
  - Throughout this sample:
      - The terms  "connectedClusters" and "connected clusters" denote Azure Arc-enabled Kubernetes clusters.
      - The terms  "managedClusters" and "managed clusters" denote Azure Kubernetes Service (AKS) clusters.      

## Artifact changes

The following changes are required to enable support for connected and managed clusters.

### Manifest

Add 'supportedClusterTypes' under extensionRegistrationParameters.

Sample below indicates all distributions of connectedClusters type and all ditributions of managedClusters type are supported.

![Alt text](images/Manifest_changes.png)

Following is the guidance on the supportedClusterTypes:

| Property      | Description |
| -----------   | ----------- |
| supportedClusterTypes       | Contains an object for each top-level cluster-type. Allowed types are – “managedClusters”, “connectedClusters”. "managedClusters" denotes Azure Kubernetes Service (AKS) clusters. "connectedClusters" denotes Azure Arc-enabled Kubernetes clusters. For each of these cluster types, specify distributions and unsupported Kubernetes versions for these distributions. If supportedClusterTypes is not provided, all distributions of ‘managedClusters’ will be supported by default. If supportedClusterTypes is provided, and a given top level cluster type is not provided, then all distributions and Kubernetes versions for that cluster type will be treated as unsupported. |
| distribution   | An array of distributions  corresponding to the cluster type. Provide name(s) of specific distributions. Set the value to [“All”]  to indicate all distributions are supported. |
| distributionSupported  | A boolean value representing whether the specified distribution(s) are supported. If false, providing a value for UnsupportedVersions will cause an error. |
| unsupportedVersions  | A list of versions for the specified distribution(s) which are unsupported. Supported operators are decribed below: |

                        •	"=" Given version is not supported. E.g.: “=1.2.12”

                        •	">" All versions greater than the given version are not supported. E.g.: “>1.1.13”

                        •	"<" All versions less than the given version are not supported. E.g.: “<1.3.14”

                        •	"..." All versions in range are unsupported. E.g.: ” 1.1.2...1.1.15”  (includes right-side value and excludes left-side value)

#### More samples of supportedClusterTypes:
Only the "AKS" distribution of connectedClusters type is supported with restriction on some versions. All distributions of managedClusters is supported with no restriction on versions.

``` yaml
  supportedClusterTypes:
    connectedClusters:
      - distribution: ["AKS"]
        distributionSupported: true
        unsupportedVersions: ["=1.2.0"]
    managedClusters:
      - distribution: ["All"]
        distributionSupported: true
        unsupportedVersions: null
```

Only the "AKS" distribution of connectedClusters type is supported with restriction on some versions. Only the "AKS" distribution of managedClusters is supported with restriction on some versions.

``` yaml
  supportedClusterTypes:
    connectedClusters:
      - distribution: ["AKS"]
        distributionSupported: true
        unsupportedVersions: ["1.10.0...1.20.0", ">1.21.1"]
    managedClusters:
      - distribution: ["AKS"]
        distributionSupported: true
        unsupportedVersions: [ ">1.23.0" ]
```

### CreateUIDefinition

Following are the important changes to be made in the CreateUIDefinition file. For a complete list of all changes and UI elements, please refer the CreateUIDefinition.json in the sample folder.

Add a control to choose the cluster type

![Alt text](images/UIDefinition_ClusterTypeControl.png)

Add a section for looking up Azure Kubernetes Service (AKS) cluster resources. Set the visibility of this section to 'true' only if the cluster type is 'managedClusters'.

![Alt text](images/UIDefinition_AKSClusterLookup.png)

Add a section for looking up Azure Arc-enabled Kubernetes cluster resources. Set the visibility of this section to 'true' only if the cluster type is 'connectedClusters'.

![Alt text](images/UIDefinition_ArcClusterLookup.png)

Add 'clusterType' propert to the outputs that will be passed as parameters to the ARM template

![Alt text](images/UIDefinition_Outputs.png)

### ARM Template

Following are the important changes to be made in the ARM template file. For a complete list of all changes, please refer the mainTemplate.json in the sample folder.

The ARM template needs to deploy the resources based on the cluster type selected by the user. When cluster type is 'managedCluster', the user chooses to create a new AKS cluster, the template will deploy a new cluster resource.

Add a new parameter for 'clusterType':

![Alt text](images/ARMTemplate_ClusterType_NewParameter.png)

For creating the new AKS cluster resource, set the condition that clusterType should be 'managedCluster' and user chooses to create new dev cluster:

![Alt text](images/ARMTemplate_ManagedCluster_Condition.png)

For the extension resource, set the scope based on the cluster type selected:

![Alt text](images/ARMTemplate_Extension_Scope.png)

Note: The 'dependsOn' property on the extension resource is applicable only when a new managed cluster resource is being deployed.

## End-user experience when creating the extension

The resulting UI Definition will shows up as follows when the end-user creates an extension using Azure Portal:

### Choosing cluster type

Select Azure Kubernetes Service (AKS) cluster type and use an existing cluster:

![Alt text](images/Create_Extension_Basics_ManagedClusterType_Existing.png)

Select Azure Kubernetes Service (AKS) cluster type and create a new cluster:

![Alt text](images/Create_Extension_Basics_ManagedClusterType_New.png)

Select Azure Arc-enabled Kubernetes cluster type:

![Alt text](images/Create_Extension_Basics_ConnectedClusterType.png)

### Configuring cluster resource

Select an existing Azure Kubernetes Service (AKS) cluster resource:

![Alt text](images/Create_Extension_ClusterDetails_SelectExistingManagedCluster.png)

Providing inputs for creating a new Azure Kubernetes Service (AKS) cluster resource:

 ![Alt text](images/Create_Extension_ClusterDetails_CreateNewManagedCluster.png)

Select an existing Azure Arc-enabled Kubernetes cluster resource:

![Alt text](images/Create_Extension_ClusterDetails_SelectExistingConnectedCluster.png)

### Configuring application/extension:

![Alt text](images/Create_Extension_ApplicationDetails_ConnectedManaged.png)

## Note
This sample includes only a small subset of the files. The files in this sample folder contains the additional changes required on top of the base sample application '[k8s-offer-azure-vote](../k8s-offer-azure-vote/)'.