provider "google" {
  project     = "lofty-dynamics-393510"
  region      = "us-central1"
  zone        = "us-central1-a"
}

resource "google_container_cluster" "my_cluster" {
  name               = "gifs-website-cluster"
  location           = "us-central1-a"
  initial_node_count = 1
  node_config {
    machine_type = "e2-micro"
  }
  node_pool {
    name       = "default-pool"
    autoscaling {
      min_node_count = 1
      max_node_count = 3
    }
  }
  tags = ["gifs-website"]
}

provider "kubernetes" {
  host = google_container_cluster.my_cluster.endpoint
}

data "google_client_config" "default" {}

provider "kubernetes" {
  host     = google_container_cluster.my_cluster.endpoint
}

resource "kubernetes_namespace" "example" {
  metadata {
    name = "example-namespace"
  }
}