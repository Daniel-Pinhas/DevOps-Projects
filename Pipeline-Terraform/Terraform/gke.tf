provider "google" {
  credentials = file("/var/lib/jenkins/.ssh/gcp-key.json")
  project     = "lofty-dynamics-393510"
  region      = "us-central1"
}

resource "google_container_cluster" "gifs-website-cluster" {
  name               = "gifs-website-cluster"
  location           = "us-central1-a"
  initial_node_count = 1
  min_master_version = "latest"
  node_version       = "latest"

  node_pool {
    name           = "default-node-pool"
    initial_node_count = 1
    autoscaling {
      min_node_count = 1
      max_node_count = 3
    }

    config {
      machine_type = "e2-micro"
      tags         = ["gifs-website"]
    }
  }
}














