resource "google_compute_firewall" "gifs-website" {
    name    = "gifs-website"
    network = google_compute_network.main.name

    allow {
        protocol = "tcp"
        ports = ["22", "80", "81", "82", "3306", "5000"]
    }

    source_ranges = ["0.0.0.0/0"]
}