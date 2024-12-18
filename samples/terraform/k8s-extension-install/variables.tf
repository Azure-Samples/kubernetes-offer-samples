variable "cluster_name" {
  type        = string
  description = "The name of the Kubernetes cluster."
}

variable "resource_group_name" {
  type        = string
  description = "The name of the resource group."
}

variable "subscription_id" {
  type        = string
  description = "The subscription ID."
  
}

variable "extension_type" {
  type        = string
  description = "The type of the extension."
}

variable "extension_resource_name" {
  type        = string
  description = "The name of the extension resource." 
}

variable "publisher" {
  type        = string
  description = "The publisher of the extension."
}

variable "product-id" {
  type        = string
  description = "The product ID of the extension."
}

variable "plan-name" {
  type        = string
  description = "The plan name of the extension."
}

variable "extension_configuration_settings" {
  type        = map(string)
  nullable   = true
  description = "The configuration settings for the extension."
}

