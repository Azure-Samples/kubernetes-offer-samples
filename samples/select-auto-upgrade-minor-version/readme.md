# Azure Marketplace Kubernetes App- select autoupgrade changes

Automatic Extension Upgrade is available for Marketplace Kubernetes applications (extensions) for minor and patch version upgrades.
When 'autoUpgradeMinorVersion' setting is enabled, the application is upgraded automatically whenever the application publisher releases a new minor or patch version for that application.
This sample illustrates changes required to provide auto upgrade of minor version as a choice to the end user at deployment time.

It involves two steps
    1) Take Autoupgrade as an input in the CreateUIDef.-so autoUpgradeMinorVersion is taken as input in the CreateUIDef.
<p align="center"><img src="images/auto-upgrade-minor-version-createuidef-change.JPG" alt="AutoUpgradeasInput" width="800"/>

    2) Pass the value provided in the CreateUIDef to the Extension resource in the ARM template. Extension resource property -autoUpgradeMinorVersion is being updated as parameter.

<p align="center"><img src="images/auto-upgrade-minor-version-armtemplate-change1.JPG" alt="Autoupgrade as ARM Parameter" width="800"/>

here the paramter is being used as resource input
<p align="center"><img src="images/auto-upgrade-minor-version-armtemplate-change2.JPG" alt="Autoupgrade as Resource Input" width="800"/>

Please note this sample includes only a small subset of the files. The files in this sample folder contains the additional changes required on top of the base sample application '[k8s-offer-azure-vote](link here)'.
