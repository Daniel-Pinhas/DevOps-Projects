import yaml
import requests
from bs4 import BeautifulSoup

def get_latest_tag(repository):
    url = f"https://hub.docker.com/repository/docker/{repository}/general"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    tag_elements = soup.select(".Repository__tag a span")
    if tag_elements:
        return tag_elements[0].text
    return None

def update_values_file(values_file, tags):
    with open(values_file, "r") as file:
        data = yaml.safe_load(file)

    data["flask1"]["image"]["tag"] = tags.get("flask1", "latest")
    data["flask2"]["image"]["tag"] = tags.get("flask2", "latest")
    data["flask3"]["image"]["tag"] = tags.get("flask3", "latest")

    with open(values_file, "w") as file:
        yaml.dump(data, file)

def main():
    repositories = {
        "flask1": "danielpinhas/flask-k8s",
        "flask2": "danielpinhas/flask2-k8s",
        "flask3": "danielpinhas/flask3-k8s"
    }

    latest_tags = {}
    for service, repository in repositories.items():
        latest_tag = get_latest_tag(repository)
        if latest_tag:
            latest_tags[service] = latest_tag

    if latest_tags:
        update_values_file("values.yml", latest_tags)
        print("Tag values updated successfully.")
    else:
        print("Failed to retrieve Docker image tags.")

if __name__ == "__main__":
    main()
