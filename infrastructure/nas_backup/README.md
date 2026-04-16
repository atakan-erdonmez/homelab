# ☁️ NAS to Google Drive Backup (Restic + Rclone)

A minimal backup solution that syncs local NAS data to Google Drive using Restic with an Rclone backend, automated via Ansible and scheduled with systemd timers.

# ⚙️ Architecture & Design

Runs on a dedicated Debian VM (backup01) inside the Proxmox cluster.

Core components:
- NFS mounts under `/mnt/backup/*`
- Restic for encrypted, incremental backups
- Rclone as Google Drive backend
- Systemd timer for scheduling
- Ansible for provisioning

# 📁 Project Structure

```
infrastructure/nas_backup/
├── deploy.yaml
├── activation.yaml
├── templates/
│   ├── backup.sh.j2
│   ├── backup.service.j2
│   └── backup.timer.j2
└── README.md
```

# 🧠 Design Decisions

- **Two-phase deployment**
  - `deploy.yaml`: prepares system, installs tools, deploys configs (not enabled)
  - `activation.yaml`: validates config, initializes repo, enables timer

- **Restic over sync**
  - Snapshot-based, deduplicated, encrypted backups instead of raw file sync

- **Read-only NAS access**
  - Backup host only reads from NAS, writes to cloud

- **Manual OAuth**
  - Rclone configured manually to avoid embedding credentials in automation

# 🚀 Deployment Flow

1. Run initial deployment:
   ```bash
   ansible-playbook deploy.yaml
   ```

2. Configure Rclone:
   ```bash
   rclone config
   ```

3. Copy config to root:
   ```bash
   mkdir -p /root/.config/rclone
   cp ~/.config/rclone/rclone.conf /root/.config/rclone/rclone.conf
   chmod 600 /root/.config/rclone/rclone.conf
   ```

4. Activate:
   ```bash
   ansible-playbook activation.yaml
   ```

# 🔁 Backup Behavior

- Source: `/mnt/backup/`
- Repo: `rclone:gdrive:Backup/nas_backup`

Each run:
- Performs incremental backup
- Applies retention policy

# ⚠️ Notes

- Runs as root
- Ensure permissions:
  - `/root/.config/rclone/rclone.conf`
  - `/etc/restic/password`
- NFS mounts handled via systemd automount

# 🛣️ Roadmap

- Logging and alerting
- Service account-based authentication
- Config-driven backup sources
