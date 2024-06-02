# Getting Started: Test Parameter file

### Overview
For offers that are to be deployed on managed clusters (such as Azure Kubernetes Service) we require a test parameter file to be added to your CNAB bundle. This is to allow us to test your deploy your offer to a cluster to confirm it would actually work. To get started on this process please follow steps below

### Get tools to assist in parameter file creation
Azure provides ARM tools which is a VS code extension that makes it easier to catch issues and validate your arm template and parameter file. 
* [Arm Tools Download] (https://marketplace.visualstudio.com/items?itemName=msazurermtools.azurerm-vscode-tools)
* [Creating a Arm Template with VS Code Extension](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/quickstart-create-templates-use-visual-studio-code?tabs=CLI)

### Use VS code extension to generate parameter file
ARM tools VS code extension can be used to generate a parameter file for your ARM template. To do this open your ARM template in a VS code editor and use the "Azure Resource Manager Tools: Select/Create Parameter File" command This will give you the option to generate a parameter file with only required parameters or all parameters. We recommend required parameters as those are the parameters needed to test the deployment.

To learn more about the command pallete [VS Code command pallete](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette)

After generating your parameter file, fill in the value of your required parameters. These should be valid values that can be used to deploy the application(Any valid value can be used).

### Testing parameter file is valid
There are a couple ways to test the validatity of your parameter file.

# * [ARM Template test tool kit](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/test-toolkit)

The ARM template test tool kit is a CLI tool that can be used to test your arm template and parameter file.

# az group deployment with what-if
az group deployment is an az cli command that can be used to create arm template deployments. If you were to run this command with the what-if flag, it will validate your deployment without actually deploying anything. This can be used to validate your arm template and test parameter file.
[az group deployment create](https://learn.microsoft.com/en-us/cli/azure/deployment/group?view=azure-cli-latest#az-deployment-group-create)

# Adding test parameter file to CNAB manifest
After validating the contents of your arm template and parameter file, you would need to add the testParameterFile along with the relative path to your parameter (similar to the main arm template)