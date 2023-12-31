resource "google_container_cluster" "gifs-website-cluster" {
  name                     = "gifs-website-cluster"
  location                 = "us-central1-a"
  remove_default_node_pool = true
  initial_node_count       = 1
  network                  = google_compute_network.main.self_link
  subnetwork               = google_compute_subnetwork.private.self_link
  logging_service          = "logging.googleapis.com/kubernetes"
  monitoring_service       = "monitoring.googleapis.com/kubernetes"
  networking_mode          = "VPC_NATIVE"

  node_locations = [
    "us-central1-b"
  ]


  addons_config {
    http_load_balancing {
        disabled = true
    }

    horizontal_pod_autoscaling {
        disabled = false
    }
  }

  release_channel {
    channel = "REGULAR"
  }

  workload_identity_config {
    workload_pool = "devops-v1.svc.id.goog"
  }

  ip_allocation_policy {
    enalbe_private_nodes    = true
    enalbe_private_endpoint = false
    master_ipv4_cidr_block  = "172.16.0.0/28"
  }
}
