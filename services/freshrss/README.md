# 📰 Automated FreshRSS Deployment

A lightweight, containerized FreshRSS deployment using Ansible and Docker, designed for simple, reproducible self-hosted RSS aggregation.

# ⚙️ Architecture & Design

This service runs on a Debian VM (**debiandocker**) inside the Proxmox cluster.
The setup is intentionally minimal, focusing on reliability and low operational overhead.

## Core Components

* **Docker Compose**: Runs FreshRSS with persistent volumes (`data`, `extensions`)
* **SQLite**: Embedded database, no external DB required
* **Ansible**: Handles provisioning and deployment
* **Headless Setup**: Initial configuration is fully automated via environment variables

## Project Structure

```
services/freshrss/
├── deploy.yaml
├── compose.yaml
├── .env
├── .env.example
└── README.md
```

## Design Decisions

* **SQLite for Simplicity**: SQLite is used instead of PostgreSQL/MySQL since this is a single-user setup. It removes unnecessary complexity while still being more than sufficient.

* **Automated (Headless) Installation**: FreshRSS is configured on first run using `FRESHRSS_INSTALL` and `FRESHRSS_USER`. This skips the web UI setup and makes the deployment fully reproducible.

* **Consistent Permissions (`root:www-data`)**: Data directories match the container’s expected ownership model. This avoids permission issues between host and container.

* **Local Storage**: Data is stored locally on the VM for simplicity. Backup is handled separately.

## Roadmap

- **Restic Backups to NAS**: Incremental, encrypted snapshots of `data/` and `extensions/` with 7 day retention policy. Run with a systemd timer or cron.

# ⚡ Quick Start

Deploy or update the service:

```
ansible-playbook deploy.yaml
```

### Access

* Local: `http://<VM-IP>:${FRESHRSS_PORT}`
* External: via reverse proxy

### Management

**Logs**

```
docker logs -f freshrss
```

**Restart**

```
docker compose -f /opt/services/freshrss/compose.yaml restart
```

**Update**

```
docker compose -f /opt/services/freshrss/compose.yaml pull
docker compose -f /opt/services/freshrss/compose.yaml up -d
```

---

## 🔗 Integration

Exposed through the centralized reverse proxy layer (`app_proxy`).

[Added to the services.yaml in app_proxy](https://github.com/atakan-erdonmez/homelab/tree/main/infrastructure/app_proxy/vars/services.yaml)

---
