---
page_type: sample
languages:
- yaml
products:
- azure-kubernetes-service
- azure-marketplace
---

# Azure Marketplace Kubernetes App samples

This repository contains samples for creating Kubernetes Applications in Azure Marketplace.

## Samples in this repo

| Sample | Description |
|--------|-------------|
|[k8s-offer-azure-vote](samples/k8s-offer-azure-vote/) | The Azure Vote application is a simple sample used throughout the Kubernetes Applications Marketplace documentation. The application consists of two pods, one running a flask web form, and the second a redis instance for temporary data storage. |
|[k8s-existing-cluster-only-sample](samples/k8s-existing-cluster-only-sample/) | This sample shows how ISV can use only existing cluster option in their create ui definition. |
|[k8s-offer-azure-vote-custom-meters](samples/k8s-offer-azure-vote-custom-meters/) | The Azure Vote custom meters application is a simple sample to demonstrate custom meters usage in a Kubernetes application. The application consists of two pods, one running a flask web form, and the second a redis instance for temporary data storage. The application submits usage data to Azure Commerce Metering API for every vote casted per hour. |
|[select-auto-upgrade-minor-version](samples/select-auto-upgrade-minor-version) | Automatic Extension Upgrade is available for Marketplace Kubernetes applications (extensions) for minor and patch version upgrades. This sample illustrates changes required to provide auto upgrade of minor version as a choice to the end user at deployment time. When 'autoUpgradeMinorVersion' setting is enabled, the application is upgraded automatically whenever the application publisher releases a new minor or patch version for that application. |
|[dynamic-configuration-settings-sample](samples/dynamic-configuration-settings-sample/) | This sample demonstrate UI definition and ARM template adjustment that is required to consume dynamic list from the UI, and combine with other predefined settings as one list to be passed into the helm chart through ARM template. |
|[k8s-cluster-condition-sample](samples/k8s-cluster-condition-sample/) | This sample shows how ISV can create or select existing Kubernetes cluster with specific k8s version in Azure Marketplace. Same idea can be applied to filter other cluster properties like size, node count, etc. |

## Getting started guide

- [Getting Started: Publishing a Kubernetes App on Azure Marketplace](getting-started/GettingStarted.md)
- [Microsoft Defender: Vulnerability Pre-Scan Check](getting-started/Vulnerability-Scan.md)
