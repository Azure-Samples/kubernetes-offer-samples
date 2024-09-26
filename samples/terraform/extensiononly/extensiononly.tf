resource "azurerm_kubernetes_cluster_extension" "clickhouse" {
  name                  = "clickhouse"
  cluster_id = var.cluster_id
  extension_type        = var.extension_type
  configuration_settings = {
    resourcesPreset = "large"
  }
  plan {
    name      = var.plan-name
    product   = var.product-id
    publisher = var.publisher
  }
}