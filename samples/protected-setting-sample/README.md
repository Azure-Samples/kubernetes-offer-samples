---
page_type: sample
languages:
- yaml
- json
products:
- azure-kubernetes-service
- azure-marketplace
---

# Protected settings sample

This sample shows how ISV can create protected settings and input secret values in UIDefinition as well as consume them in ARM Template so that they can be passed to Kubernetes Extension Type as Configuration Protected Settings.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 111a2e5 (document updates)
=======
>>>>>>> 99bc22e (updates)
=======
>>>>>>> 111a2e5 (document updates)
=======
>>>>>>> 99bc22e (updates)
Protected configuration settings help manage sensitive data securely. These settings typically include information such as passwords, API keys, certificates, or connection strings. Protected configuration settings are stored as secrets on the Kubernetes clusters. As a result, the key names of the protected configuration settings should be simple text and special characters should not be included. Protected configuration settings for an extension instance are stored for up to 48 hours in the cluster extension services. As a result, if the cluster remains disconnected during the 48 hours after the extension resource is created in Azure, the extension changes from a Pending state to a Failed state. To prevent this, it is recommended that ISVs bring clusters online regularly. 

For Documentation on Protected Settings and Cluster extensions, please refer to [Cluster Extensions](https://learn.microsoft.com/en-us/azure/azure-arc/kubernetes/conceptual-extensions) and [Deploy and manage cluster extensions by using Azure CLI](https://learn.microsoft.com/en-us/azure/aks/deploy-extensions-az-cli) documentation.

For Documentation on Configurations Protected Settings parameter, please refer to the "--configuration-protected-settings" parameter, located under the "Optional Parameters" Section of [documentation](https://learn.microsoft.com/en-us/azure/aks/deploy-extensions-az-cli#optional-parameters), as well as.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 832b198 (protected setting sample)
=======
Protected configuration settings help manage sensitive data securely. These settings typically include information such as passwords, API keys, certificates, or connection strings. Protected configuration settings are stored as secrets on the Kubernetes clusters. As a result, the key names of the protected configuration settings should be of simple text and special chars should not be included. Protected configuration settings for an extension instance are stored for up to 48 hours in the cluster extension services. As a result, if the cluster remains disconnected during the 48 hours after the extension resource is created in Azure, the extension changes from a Pending state to a Failed state. To prevent this, we recommend that you bring clusters online regularly. For Documentation on Configurations Protected Settings parameter, please refer to the "Optional Parameters" Section of [documentation](https://learn.microsoft.com/en-us/azure/aks/deploy-extensions-az-cli#optional-parameters)

>>>>>>> 66655ef (documentation updates to protected settings sample)
=======
Protected configuration settings help manage sensitive data securely. These settings typically include information such as passwords, API keys, certificates, or connection strings. Protected configuration settings are stored as secrets on the Kubernetes clusters. As a result, the key names of the protected configuration settings should be simple text and special characters should not be included. Protected configuration settings for an extension instance are stored for up to 48 hours in the cluster extension services. As a result, if the cluster remains disconnected during the 48 hours after the extension resource is created in Azure, the extension changes from a Pending state to a Failed state. To prevent this, it is recommended that ISVs bring clusters online regularly. For Documentation on Configurations Protected Settings parameter, please refer to the "--configuration-protected-settings" parameter, located under the "Optional Parameters" Section of [documentation](https://learn.microsoft.com/en-us/azure/aks/deploy-extensions-az-cli#optional-parameters).
>>>>>>> 3002226 (image updates)
=======
>>>>>>> 111a2e5 (document updates)
=======
=======
>>>>>>> 832b198 (protected setting sample)
>>>>>>> 99bc22e (updates)
=======
>>>>>>> d70616f (protected settings sample)
=======
>>>>>>> 832b198 (protected setting sample)
=======
Protected configuration settings help manage sensitive data securely. These settings typically include information such as passwords, API keys, certificates, or connection strings. Protected configuration settings are stored as secrets on the Kubernetes clusters. As a result, the key names of the protected configuration settings should be of simple text and special chars should not be included. Protected configuration settings for an extension instance are stored for up to 48 hours in the cluster extension services. As a result, if the cluster remains disconnected during the 48 hours after the extension resource is created in Azure, the extension changes from a Pending state to a Failed state. To prevent this, we recommend that you bring clusters online regularly. For Documentation on Configurations Protected Settings parameter, please refer to the "Optional Parameters" Section of [documentation](https://learn.microsoft.com/en-us/azure/aks/deploy-extensions-az-cli#optional-parameters)

>>>>>>> 66655ef (documentation updates to protected settings sample)
=======
Protected configuration settings help manage sensitive data securely. These settings typically include information such as passwords, API keys, certificates, or connection strings. Protected configuration settings are stored as secrets on the Kubernetes clusters. As a result, the key names of the protected configuration settings should be simple text and special characters should not be included. Protected configuration settings for an extension instance are stored for up to 48 hours in the cluster extension services. As a result, if the cluster remains disconnected during the 48 hours after the extension resource is created in Azure, the extension changes from a Pending state to a Failed state. To prevent this, it is recommended that ISVs bring clusters online regularly. For Documentation on Configurations Protected Settings parameter, please refer to the "--configuration-protected-settings" parameter, located under the "Optional Parameters" Section of [documentation](https://learn.microsoft.com/en-us/azure/aks/deploy-extensions-az-cli#optional-parameters).
>>>>>>> 3002226 (image updates)
=======
>>>>>>> 111a2e5 (document updates)
=======
=======
>>>>>>> 832b198 (protected setting sample)
>>>>>>> 99bc22e (updates)
## The resulting UI Definition will shows up as follow:

![Alt text](images/UI_Sample.PNG)

# Explanation

## UIDefinition
The following section adjusts the UI Definition to include a PasswordBox UI element
![Alt text](images/UIDefinition.PNG)

For more detail regarding the PasswordBox UI element, please refer to [documentation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/managed-applications/microsoft-common-passwordbox)

## ARM Template
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 99bc22e (updates)
=======
>>>>>>> 99bc22e (updates)
Configuration Protected Setting (PasswordBox in this example) should be passed to the ARM template as follows:
![Alt text](images/main_template.PNG)

The PasswordBox element should also be passed in as a parameter in the ARM template as follows:
![Alt text](images/define_parameters_main_template.PNG)
 The parameter type for the PasswordBox should be a "securestring" to ensure sensitive text data is protected and encrypted properly.

=======
Configuration Protected Setting (PasswordBox in this example) should be passed to the template as follows
 ![Alt text](images/main_template.PNG)
>>>>>>> 832b198 (protected setting sample)
<<<<<<< HEAD
<<<<<<< HEAD
=======
Configuration Protected Setting (PasswordBox in this example) should be passed to the ARM template as follows:
![Alt text](images/main_template.PNG)

The PasswordBox element should also be passed in as a parameter in the ARM template as follows:
![Alt text](images/define_parameters_main_template.PNG)
 The parameter type for the PasswordBox should be a "securestring" to ensure sensitive text data is protected and encrypted properly.

>>>>>>> 66655ef (documentation updates to protected settings sample)
=======
>>>>>>> 99bc22e (updates)
=======
Configuration Protected Setting (PasswordBox in this example) should be passed to the template as follows
 ![Alt text](images/main_template.PNG)
>>>>>>> d70616f (protected settings sample)
=======
Configuration Protected Setting (PasswordBox in this example) should be passed to the template as follows
 ![Alt text](images/main_template.PNG)
>>>>>>> 832b198 (protected setting sample)
=======
Configuration Protected Setting (PasswordBox in this example) should be passed to the ARM template as follows:
![Alt text](images/main_template.PNG)

The PasswordBox element should also be passed in as a parameter in the ARM template as follows:
![Alt text](images/define_parameters_main_template.PNG)
 The parameter type for the PasswordBox should be a "securestring" to ensure sensitive text data is protected and encrypted properly.

>>>>>>> 66655ef (documentation updates to protected settings sample)
=======
>>>>>>> 99bc22e (updates)
In the helm chart, ISVs need to have the corresponding key (password) in values.yaml to take and consume in their application.

## Note
This sample includes only a small subset of the files. The files in this sample folder contains the additional changes required on top of the base sample application '[k8s-offer-azure-vote](../k8s-offer-azure-vote/)'.