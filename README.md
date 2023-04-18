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

- k8s-offer-azure-vote: The Azure Vote application is a simple sample used throughout the Kubernetes Applications Marketplace documentation. The application consists of two pods, one running a flask web form, and the second a redis instance for temporary data storage.
- k8s-offer-azure-vote-custom-meters: The Azure Vote custom meters application is a simple sample to demonstrate custom meters usage in a Kubernetes application. The application consists of two pods, one running a flask web form, and the second a redis instance for temporary data storage. The application submits usage data to Azure Commerce Metering API for every vote casted per hour.

## Getting started guide

- [Getting Started: Publishing a Kubernetes App on Azure Marketplace](getting-started/GettingStarted.md)
- [Microsoft Defender: Vulnerability Pre-Scan Check](getting-started/Vulnerability-Scan.md)
