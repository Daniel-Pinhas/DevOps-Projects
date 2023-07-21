import docker
import subprocess

def get_latest_tag(repository):
    client = docker.from_env()
    images = client.images.list(name=repository)

    latest_tag = None
    for image in images:
        tags = image.tags
        for tag in tags:
            if tag.startswith(repository + ":"):
                tag_version = tag.split(":")[1]
                if not latest_tag or tag_version > latest_tag:
                    latest_tag = tag_version

    return latest_tag

def main():
    repositories = ["danielpinhas/flask-k8s", "danielpinhas/flask2-k8s", "danielpinhas/flask3-k8s"]

    for repository in repositories:
        latest_tag = get_latest_tag(repository)
        if latest_tag:
            cmd = f"helm upgrade --install flask-app . --set {repository.split('/')[1]}.tag={latest_tag}"
            subprocess.run(cmd, shell=True, check=True)

if __name__ == "__main__":
    main()
