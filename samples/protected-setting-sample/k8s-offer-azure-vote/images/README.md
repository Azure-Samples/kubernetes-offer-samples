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

This folder contains samples that shows how ISV can create protected settings and input secret values in UIDefinition as well as consume them in ARM Template so that they can be passed to Kubernetes Extension Type as Configuration Protected Settings.

## The resulting UI Definition will shows up as follow:

![Alt text](images/UI_Sample.PNG)

# Explanation

## UIDefinition
The following section adjusts the UI Definition to include a PasswordBox UI element
![Alt text](images/UIDefinition.PNG)

## ARM Template
Configuration Protected Setting (PasswordBox in this example) should be passed to the template as follows
 ![Alt text](images/main_template.PNG)

## Note
This sample includes only a small subset of the files. The files in this sample folder contains the additional changes required on top of the base sample application '[k8s-offer-azure-vote](../k8s-offer-azure-vote/)'.