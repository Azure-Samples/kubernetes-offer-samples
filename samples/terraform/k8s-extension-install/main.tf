resource "azurerm_kubernetes_cluster_extension" "k8sxtension" {
  name                  = var.extension_resource_name
  cluster_id =  "/subscriptions/${var.subscription_id}/resourceGroups/${var.resource_group_name}/providers/Microsoft.ContainerService/managedClusters/${var.cluster_name}"
  extension_type        = var.extension_type
  configuration_settings = var.extension_configuration_settings == null ? {} : var.extension_configuration_settings
  plan {
    name      = var.plan-name
    product   = var.product-id
    publisher = var.publisher
  }
}