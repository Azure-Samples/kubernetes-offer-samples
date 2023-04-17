# Getting Started: Publishing a Kubernetes App on Azure Marketplace

### Introduction
Thank you for joining us in our Kubernetes Apps Marketplace program. We’re delighted to have you participate in our vibrant and ever-growing ecosystem, where you can publish and monetize your Kubernetes application. This document has all the necessary steps to get you started and can enable you to publish your application in 1-2 weeks to the Kubernetes marketplace in Azure.

### Pre-requisites
You must meet the following criteria to be able to participate:
* The Kubernetes application should have a Helm-chart based application that is free of malware and vulnerabilities. We highly recommend doing a [pre-scan and fixing the vulnerabilities](https://github.com/bobmital/kubernetes-offer-samples/blob/05611a5c6485db980fe27fb8999af728382b547d/getting-started/Vulnerability-Scan.md) before you push the application through the pipeline.
* You should have an active publishing tenant or access to a [Partner Center account](https://learn.microsoft.com/en-us/partner-center/overview).
* You should be able to adhere to several of our supported [billing models (licensing options)](https://learn.microsoft.com/en-us/partner-center/marketplace/marketplace-containers). 
* Must be actively engaged. If we notice that your engagement levels have decreased, we may need to give priority to other participants due to the high volume of interest we receive.

### Training
The Following training materials will help accelerate your onboarding onto the Azure Marketplace.
* [Mastering Container offers for Kubernetes Apps](https://microsoft.github.io/Mastering-the-Marketplace/container/)
* [Azure K8s Apps Marketplace Demo Walkthrough](https://www.youtube.com/watch?v=_6yGXUND43s)


### Steps to follow
#### Step 1: Package your application
This step allows you to package your helm chart-based application and other artifacts such as Azure Resource Manager (ARM) template, manifest file, Helm chart and createUIDef into a Cloud Native Application Bundles (CNAB) package. Please refer to the links below:
* [Prepare your Kubernetes Apps offer](https://learn.microsoft.com/en-us/partner-center/marketplace/azure-container-technical-assets-kubernetes?tabs=windows)

At the end of this step, you will be able to create a CNAB bundle.

#### Step 2: Create the Kubernetes offer
This step allows you to create an Azure Container offer within Partner Center. You can preview and test the offer before publishing it on the Azure Marketplace.
* [Create an Azure Container offer](https://learn.microsoft.com/en-us/partner-center/marketplace/azure-container-offer-setup)

In order to simplify the process of Vulnerability scanning and certification, Microsoft strongly recommends you follow the steps in the Vulnerability Scan-Microsoft Defender document to understand the vulnerabilities flagged. Please take action to resolve them before pushing the offer through the pipeline.
* [Vulnerability Scan-Microsoft Defender](https://github.com/bobmital/kubernetes-offer-samples/blob/main/getting-started/Vulnerability-Scan.md)

#### Step 3: Purchase/Deploy your application
This step walks through the process that an end consumer would go through to deploy the application onto their Kubernetes cluster.
* [Deploy a container offer from Azure Marketplace (preview)](https://learn.microsoft.com/en-us/azure/aks/deploy-marketplace)

#### Step 4: If you plan to stop activity on your offer, you can proceed by Stop selling the app. The "Stop Sell" of an offer/plan means no future acquisitions of the offer/plan are possible via Azure Marketplace. Since these are consumption-based plans for now, the existing deployments will continue to emit usage till customers uninstall the extension.
* [Stop distribution of an offer or plan](https://learn.microsoft.com/en-us/partner-center/marketplace/update-existing-offer#stop-distribution-of-an-offer-or-plan)

### Troubleshooting
If you have encountered any issues or failures in packaging, deploying, or publishing your application, please follow the guide in the relevant troubleshotting documentation below.
* [Troubleshoot issues while packaging a Kubernetes application-based Container offer](https://learn.microsoft.com/en-us/partner-center/marketplace/azure-container-packaging-troubleshoot)
* [Troubleshoot issues while publishing a Kubernetes application-based Container offer](https://learn.microsoft.com/en-us/partner-center/marketplace/azure-container-troubleshoot)
* [Troubleshoot the failed deployment of a Kubernetes application offer](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/troubleshoot-failed-kubernetes-deployment-offer)

### Microsoft contacts
For any additional questions not covered by this guide, feel free to reach out to the Microsoft Azure Kubernetes Service (AKS) Ecosystem product team at tcontainerpreview@service.microsoft.com.

### Glossary of terms
**Kubernetes Application**: A Kubernetes Application on Azure Marketplace refers to a software application that is packaged and available for purchase and deployment through Azure Marketplace and is designed to be deployed and managed on a Kubernetes cluster running on AKS.
**Azure Container Offer**: A transactable offer type in the Microsoft commercial marketplace that enables running containers on AKS in the customer’s tenant.
