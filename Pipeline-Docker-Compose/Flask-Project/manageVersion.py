import docker

client = docker.from_env()

images = client.images.list()

existing_versions = [float(image.tags[0].split(":")[1]) for image in images if image.tags and image.tags[0].startswith("danielpinhas/flask-compose:")]

if existing_versions:
    latest_version = max(existing_versions) 
    next_version = latest_version + 0.1 
    # Delete the previous version image
    previous_version = latest_version
    previous_image_name = f"danielpinhas/flask-compose:{previous_version}"
    client.images.remove(image=previous_image_name, force=True)
    print(f"Successfully deleted image: {previous_image_name}")
else:
    next_version = 1.0
    
# Format the version number to one decimal place
next_version = f"{next_version:.1f}"
image_name = f"danielpinhas/flask-compose:{next_version}"

# Build the new version image
client.images.build(path=".", tag=image_name, rm=True, pull=True)
print(f"Successfully built image: {image_name}")

# Push the image to Docker Hub
client.images.push(repository="danielpinhas/flask-compose", tag=next_version)
print(f"Successfully pushed image: {image_name}")

# Tag the new version as "latest"
latest_image_name = "danielpinhas/flask-compose:latest"
client.images.get(image_name).tag(latest_image_name)
print(f"Successfully tagged image as latest: {latest_image_name}")

# Push the latest image to Docker Hub
client.images.push(repository="danielpinhas/flask-compose", tag="latest")
print(f"Successfully pushed latest image: {latest_image_name}")
