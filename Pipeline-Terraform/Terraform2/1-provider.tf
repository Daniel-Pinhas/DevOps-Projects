provider "google" {
  project = "devops-v1"
  region  = "us-central1"
}

terraform {
    backend "gcs" {
        bucket = "gifs-website-bucket"
        prefix = "terraform/state"
  }
}
