resource "random_id" "aks_rg_suffix" {
  keepers = {
    # Generate a new id each time we switch to a new AMI id
    ami_id = var.clustername
  }

  byte_length = 8
}
resource "azurerm_resource_group" "aks_rg" {
  name     = "${var.resource_group_name_prefix}-${random_id.aks_rg_suffix.hex}"
  location = var.resource_group_location
}
resource "azurerm_kubernetes_cluster" "aks" {
  name                = var.clustername
  location            = var.resource_group_location
  resource_group_name = azurerm_resource_group.aks_rg.name
  dns_prefix          = "aks"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_DS2_v2"
    os_sku     = "AzureLinux"
    fips_enabled = true
  }

  identity {
    type = "SystemAssigned"
  }

  network_profile {
    network_plugin = "azure"
    load_balancer_sku = "standard"
  }
}

resource "azurerm_kubernetes_cluster_node_pool" "userpool" {
  name                  = "internal"
  kubernetes_cluster_id = azurerm_kubernetes_cluster.aks.id
  vm_size               = "Standard_DS2_v2"
  node_count            = 1
  max_pods              = 110
  os_disk_size_gb       = 30
  os_type               = "Linux"
  os_sku                = "AzureLinux"
  fips_enabled          = true
  mode                  = "User"
}

resource "azurerm_kubernetes_cluster_extension" "extension" {
  name                  = "example-extension1"
  cluster_id = azurerm_kubernetes_cluster.aks.id
  extension_type        = "ContosoJ.PrivateAzureVotePerEveryNode"
  release_train         = "preview"
  configuration_settings = {
    title = "Azure Vote App 2"
    value1 = "BMW"
    value2 = "Mercedes"
  }
  plan {
    name      = "pereverynodeincluster"
    product   = "prasannatestcontaineroffer1"
    publisher = "test_test_mix3pptest0011614206850774"
  }
}