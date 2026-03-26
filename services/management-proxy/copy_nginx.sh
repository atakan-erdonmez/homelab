#!/bin/bash

# This scripts allows for constant changes in nginx.conf
# It copies the config and reloads the container

SOURCE_FILE="./nginx.conf"
DEST_FILE="/opt/services/management-proxy/nginx.conf"
CONTAINER_NAME="nginx-proxy"

# 1. Copy the configuration file
if [ -f "$SOURCE_FILE" ]; then
    echo "Copying $SOURCE_FILE to $DEST_FILE..."
    # Using sudo in case /opt requires elevated permissions
    sudo cp "$SOURCE_FILE" "$DEST_FILE"
else
    echo "Error: $SOURCE_FILE not found."
    exit 1
fi

# 2. Reload Nginx inside the Docker container
echo "Reloading Nginx configuration in $CONTAINER_NAME..."
docker exec "$CONTAINER_NAME" nginx -s reload

if [ $? -eq 0 ]; then
    echo "Successfully reloaded Nginx."
else
    echo "Error: Failed to reload Nginx in container $CONTAINER_NAME."
    exit 1
fi