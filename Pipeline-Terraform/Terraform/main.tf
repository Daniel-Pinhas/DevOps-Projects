provider "google" {
  project = "lofty-dynamics-393510"
  region  = "us-central1"
  zone    = "us-central1-a"
}

# Create a new network for the GKE cluster
resource "google_compute_network" "gke_network" {
  name = "gke-network"
}

# Create a new subnet in the network
resource "google_compute_subnetwork" "gke_subnet" {
  name          = "gke-subnet"
  ip_cidr_range = "10.0.0.0/24"
  network       = google_compute_network.gke_network.id
  region        = "us-central1"
}

# Create the GKE cluster with node auto-provisioning
resource "google_container_cluster" "gifs-website-cluster" {
  name     = "gifs-website-cluster"
  location = "us-central1-a"

  # Enable node auto-provisioning
  remove_default_node_pool = true
  
  node_config {
    machine_type = "e2-micro"
  }
  node_pool {
    name               = "default-pool"
    initial_node_count = 1

    # Configure auto-provisioning parameters
    autoscaling {
      min_node_count = 1
      max_node_count = 3
    }
    management {
      auto_repair  = true
      auto_upgrade = true
    }
  }
}

# Create a firewall rule to allow specific traffic to the GKE nodes
resource "google_compute_firewall" "gke_cluster_firewall" {
  name    = "gke-cluster-firewall"
  network = google_compute_network.gke_network.id

  allow {
    protocol = "tcp"
    ports    = ["80", "81", "82", "5000", "3306"]
  }

  source_tags = [google_container_cluster.gifs-website-cluster.name]
  target_tags = [google_container_cluster.gifs-website-cluster.name]
}

provider "kubernetes" {
  host = google_container_cluster.gifs-website-cluster.endpoint
}

data "google_client_config" "default" {}

resource "kubernetes_namespace" "example" {
  metadata {
    name = "example-namespace"
  }
}










provider "google" {
  project = "lofty-dynamics-393510"
  region  = "us-central1"
  zone    = "us-central1-a"
}

# Create the firewall rule
resource "google_compute_firewall" "gke-gifs_website_firewall" {
  name    = "gke-gifs-website"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["80", "81", "82", "5000", "3306"]
  }

  source_ranges = ["0.0.0.0/0"] # Allow traffic from any source (you can adjust this as needed)
}

# Create the GKE cluster
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

  # Associate the GKE cluster with the firewall rule
  node_config {
    service_account = google_compute_firewall.gke-gifs_website_firewall.self_link
  }
}

provider "kubernetes" {
  host = google_container_cluster.my_cluster.endpoint
}

data "google_client_config" "default" {}

resource "kubernetes_namespace" "example" {
  metadata {
    name = "example-namespace"
  }
}






