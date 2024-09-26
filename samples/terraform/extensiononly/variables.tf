variable "cluster_id" {
  type        = string
  description = "The ID of the Kubernetes cluster. /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/example-resource-group/providers/Microsoft.ContainerService/managedClusters/managedClusterValue"
}

variable "extension_type" {
  type        = string
  default = "Bitnami.ClickhouseMain"
  description = "The type of the extension."
}

variable "publisher" {
  type        = string
  default = "bitnami"
  description = "The publisher of the extension."
}

variable "product-id" {
  type        = string
  default = "clickhouse-cnab"
  description = "The product ID of the extension."
}

variable "plan-name" {
  type        = string
  default = "main"
  description = "The plan name of the extension."
}

