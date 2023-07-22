import docker
import subprocess
import yaml

client = docker.from_env()
images = client.images.list()
existing_versions = [
    float(image.tags[0].split(":")[1])
    for image in images
    if image.tags and image.tags[0].startswith("danielpinhas/flask-k8s")
]

# Function to run the Helm upgrade command for each Flask service
def upgrade_flask(flask_name, tag, nodePort):
    cmd = f"helm upgrade --install flask-app . --set {flask_name}.tag={tag} --set {flask_name}.nodePort={nodePort}"
    subprocess.run(cmd, shell=True, check=True)

# Assuming you want the latest tag for each Flask service
latest_tag = "latest"

# Load the values.yml file and merge it into a single dictionary
with open("values.yml", "r") as f:
    all_values = list(yaml.load_all(f, Loader=yaml.SafeLoader))
    values = {}
    for v in all_values:
        values.update(v)

# Update the tag values for each Flask service
values["flask1"]["tag"] = latest_tag
values["flask2"]["tag"] = latest_tag
values["flask3"]["tag"] = latest_tag

# Run the Helm upgrade for each Flask service with the latest tag
upgrade_flask("flask1", values["flask1"]["tag"], values["flask1"]["nodePort"])
upgrade_flask("flask2", values["flask2"]["tag"], values["flask2"]["nodePort"])
upgrade_flask("flask3", values["flask3"]["tag"], values["flask3"]["nodePort"])
