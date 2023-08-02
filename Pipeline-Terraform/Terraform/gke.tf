provider "google" {
  credentials = file("/var/lib/jenkins/.ssh/gcp-key.json")
}

module "gke_auth" {
  source       = "terraform-google-modules/kubernetes-engine/google//modules/auth"
  depends_on   = [module.gke]
  project_id   = "lofty-dynamics-393510"
  location     = "us-central1-a"
  cluster_name = "gifs-website-cluster-test"
}

resource "local_file" "kubeconfig" {
  content  = module.gke_auth.kubeconfig_raw
  filename = "kubeconfig-test"
}

module "gcp-network" {
  source       = "terraform-google-modules/network/google"
  project_id   = "lofty-dynamics-393510"
  network_name = "gcp-network-test"
  subnets = [
    {
      subnet_name   = "gcp-subnetwork-test"
      subnet_ip     = "10.10.0.0/16"
      subnet_region = "us-central1"
    },
  ]
  secondary_ranges = {
    "gcp-subnetwork-dev" = [
      {
        range_name    = "ip-range-pods-test"
        ip_cidr_range = "10.20.0.0/16"
      },
      {
        range_name    = "ip-range-services-test"
        ip_cidr_range = "10.30.0.0/16"
      },
    ]
  }
}

module "gke" {
  source            = "terraform-google-modules/kubernetes-engine/google//modules/private-cluster"
  project_id        = "lofty-dynamics-393510"
  name              = "gifs-website-cluster-test"
  regional          = false
  region            = "us-central1"
  zones             = ["us-central1-a"]
  network           = module.gcp-network.network_name
  subnetwork        = module.gcp-network.subnets_names[0]
  ip_range_pods     = "ip-range-pods-test"
  ip_range_services = "ip-range-services-test"
  node_pools = [
    {
      name           = "node-pool"
      machine_type   = "e2-micro"
      node_locations = ["us-central1-a"]
      min_count      = 1
      max_count      = 3
      disk_size_gb   = 100
      preemptible    = false
      auto_repair    = false
      auto_upgrade   = true
    },
  ]
}

resource "google_compute_firewall" "allow_ports" {
  name    = "gifs-website-cluster-test"
  network = module.gcp-network.network_name

  allow {
    protocol = "tcp"
    ports    = ["80", "81", "82", "3306", "5000"]
  }
}

output "cluster_name" {
  description = "gifs-website-cluster-test"
  value       = module.gke.name
}
