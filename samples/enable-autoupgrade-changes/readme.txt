This sample illustrates changes required to provide autoupgrade of Minor version as a choice to the end user.
It involves two steps
    1) Take Autoupgrade as an input in the CreateUIDef.-so autoUpgradeMinorVersion is taken as input in the CreateUIDef.
    2) Pass the value provided in the CreateUIDef to the Extension resource in the ARM template. Extension resource property -autoUpgradeMinorVersion is being updated as parameter.

