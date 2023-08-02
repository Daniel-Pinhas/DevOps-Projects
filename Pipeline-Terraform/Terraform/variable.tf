variable "project_id" {
  description = "lofty-dynamics-393510"
}
variable "cluster_name" {
  description = "gifs-website-cluster-test"
  default     = "gke-terraform"
}
variable "env_name" {
  description = "The environment for the GKE cluster"
  default     = "Testing"
}
variable "region" {
  description = "The region to host the cluster in"
  default     = "us-central1"
}
variable "zones" {
  description = "Cluster zone"
  default     = "us-central1-a"
}
variable "network" {
  description = "The VPC network created to host the cluster in"
  default     = "gke-network-test"
}
variable "subnetwork" {
  description = "The subnetwork created to host the cluster in"
  default     = "gke-subnet-test"
}
variable "ip_range_pods_name" {
  description = "The secondary ip range to use for pods"
  default     = "ip-range-pods-test"
}
variable "ip_range_services_name" {
  description = "The secondary ip range to use for services"
  default     = "ip-range-services-test"
}

variable "service-account-id" {
  description = "The ID of service account of GCP"
  default     = "107205774763160183417"
}
variable "cpus" {
  description = "Number of cpus"
  default     = "2"
}

variable "minnode" {
  description = "Minimum number of node pool"
  default     = 1
}
variable "maxnode" {
  description = "Maximum number of node pool"
  default     = 2
}

variable "disksize" {
  description = "Disk Size in GB"
  default     = 10
}