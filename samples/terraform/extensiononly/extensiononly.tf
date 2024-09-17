resource "azurerm_kubernetes_cluster_extension" "extension" {
  name                  = "example-extension"
  cluster_id = var.cluster_id
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