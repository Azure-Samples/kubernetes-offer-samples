---
page_type: sample
languages:
- yaml
- json
products:
- azure-kubernetes-service
- azure-marketplace
---

# Dynamic configuration settings sample

This folder contains samples that shows how ISV can combinee dynamic and mandatory settings in UIDefinition and consume them in ARM Template so that they can be passed to Kubernetes Extension Type as Configuration Settings.

## The resulting UI Definition will shows up as follow:

![Alt text](images/LabelExample.PNG)

## Resulting Pod Label

![Alt text](images/DeploymentResult.PNG)

## Configuration Settings

![Alt text](images/ConfigurationSettingResult.PNG)

# Explanation

## Helm chart

For Azure-vote to take labels setting to the pods, the following changes are required:

### deployments.yaml

![Alt text](images/Deployments.yaml.PNG)

### values.yaml

![Alt text](images/Values.yaml.PNG)


## UIDefinition
The following section creates an array of key value pairs
![Alt text](images/UIDefinition.PNG)

Which will generate the following output based on above example:
![Alt text](images/DynamicSettingResults.PNG)


## ARM Template
A few variables are required to use to construct the final configuration settings that can be consumed by k8s extension type

- Convert dynamic settings array to json
 ![Alt text](images/ARMTemplate-convertArrayToJson.PNG)

- Check if dynamic settings is not set, so we don't need to combine the values with mandatory settings
 ![Alt text](images/ARMTemplate-checkDynamicSettingIsNotSet.PNG)

- Combine mandatory values as json          
 ![Alt text](images/ARMTemplate-combineMandatoryValuesAsJson.PNG)

- Union mandatory values and dynamic settings if it is set as json
 ![Alt text](images/ARMTemplate-constructFinalConfigurationSettingAsJson.PNG)



# Note
Please note this sample includes only a small subset of the files. The files in this sample folder contains the additional changes required on top of the base sample application '[k8s-offer-azure-vote](../k8s-offer-azure-vote/)'.