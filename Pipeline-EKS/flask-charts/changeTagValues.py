import yaml
import docker

def get_local_latest_tag(repository):
    client = docker.from_env()
    try:
        image = client.images.get(repository)
        return image.tags[0] if image.tags else None
    except docker.errors.ImageNotFound:
        return None

def extract_number_from_tag(tag):
    # This function will extract the number from the tag using string manipulation.
    # You can modify this function according to the format of your tags.
    # For example, if your tags are in the format "2.0" or "v2.0", this function will extract "2.0".
    return tag.split(":")[-1]

def update_values_file(values_file, tags):
    with open(values_file, "r") as file:
        data = yaml.safe_load(file)

    for service in data:
        if service.startswith("flask"):
            repo_tag = tags.get(service, "latest")
            tag_number = extract_number_from_tag(repo_tag)
            data[service]["image"]["tag"] = tag_number

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
        latest_tag = get_local_latest_tag(repository)
        if latest_tag:
            latest_tags[service] = latest_tag

    if latest_tags:
        update_values_file("values.yml", latest_tags)
        print("Tag values updated successfully.")
    else:
        print("Failed to retrieve Docker image tags.")

if __name__ == "__main__":
    main()
