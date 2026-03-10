# Guacamole IaC Deployment

This is an automated setup for Apache Guacamole, a clientless remote desktop gateway. It’s designed to give you RDP, SSH, and VNC access through a browser without needing to install anything on the client side.

## Architecture and Design

The stack is containerized for portability and managed via Ansible for idempotent configuration.

### Core Components

- guacd: The proxy daemon handling the translation of desktop protocols.
- guacamole: Java-based web frontend.
- MariaDB 11: Persistent storage backend for user authentication and connection mapping.

### Automation Logic (Ansible)

The playbook handles the end-to-end lifecycle of the service:

- **Environment Preparation:** Provisions the /opt/services directory structure and enforces 0600 permissions on secret files.
- **Schema Initialization:** Automatically generates the required MySQL schema from the Guacamole image, eliminating manual database setup.
- **Orchestration:** Deploys the Docker Compose stack and ensures service health.

## Personal Note

I built this to see if it could be a "universal gateway" for my homelab management.

**The Verdict:** Guacamole is great for RDP and SSH, but it’s not a web proxy. Since most of my lab (Proxmox, etc.) uses web GUIs, I’ve moved those over to Nginx. I'm keeping this repo as a reference for whenever I need a dedicated RDP/SSH jump-box.

# Quick Start
1- **Prerequisites:** Install the required Ansible collection
`ansible-galaxy collection install community.docker`

2- **Setup:** Define your inventory in `ansible/inventory.ini` and put your database password in `.env`.

3- **Deploy**:
`ansible-playbook -i your_inventory.ini deploy.yaml`

### Accessing the UI
Once deployed, the interface is at:
`http://<your_ip>:8080/guacamole

**Note:** You must include the `/guacamole/` suffix, otherwise the server will return 404

### Default Credentials
Username: guacadmin
Password: guacadmin
(Be sure to change these immediately after your first login!)