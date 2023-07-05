import docker

client = docker.from_env()

images = client.images.list()

existing_versions = [float(image.tags[0].split(":")[1]) for image in images if image.tags and image.tags[0].startswith("danielpinhas/flask-compose:")]

if existing_versions:
    latest_version = max(existing_versions)
    next_version = latest_version + 0.1
else:
    next_version = 1.0

# Format the version number to one decimal place
next_version = f"{next_version:.1f}"
image_name = f"danielpinhas/flask-compose:{next_version}"

client.images.build(path=".", tag=image_name, rm=True, pull=True)
print(f"Successfully built image: {image_name}")

# Push the image to Docker Hub
client.images.push(repository="danielpinhas/flask-compose", tag=next_version)
print(f"Successfully pushed image: {image_name}")

# Remove the latest version image
latest_image_name = "danielpinhas/flask-compose:latest"
existing_latest_image = client.images.get(latest_image_name)
if existing_latest_image:
    client.images.remove(image=latest_image_name, force=True)
    print(f"Successfully removed existing image: {latest_image_name}")

# Tag the next version as "latest"
client.images.get(image_name).tag(latest_image_name)
print(f"Successfully tagged image as latest: {latest_image_name}")

# Push the latest image to Docker Hub
client.images.push(repository="danielpinhas/flask-compose", tag="latest")
print(f"Successfully pushed latest image: {latest_image_name}")
