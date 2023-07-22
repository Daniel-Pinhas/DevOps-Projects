import docker
import subprocess
import yaml

client = docker.from_env()
images = client.images.list()
existing_versions = [
    float(image.tags[0].split(":")[1])
    for image in images
    if image.tags and any(tag.startswith("danielpinhas/flask") for tag in image.tags)
]

latest_tag = str(max(existing_versions))

def upgrade_flask(flask_name, tag):
    cmd = f"helm upgrade --install flask-app . --set {flask_name}.tag={tag}"
    subprocess.run(cmd, shell=True, check=True)

upgrade_flask("flask", latest_tag)
upgrade_flask("flask2", latest_tag)
upgrade_flask("flask3", latest_tag)
