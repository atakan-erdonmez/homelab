# 📚 Automated Kavita E-book Server & Backup Solution

A containerized deployment of the Kavita e-book reader & library, integrated with high-availability NAS storage and automated Restic snapshots.

# ⚙️ Architecture & Design

This service is hosted on a dedicated Debian VM (**debiandocker**) within the Proxmox cluster. It leverages a hybrid storage model where application logic remains local to the compute node, while the library data and backup repository reside on a centralized QNAP NAS.

The solution is designed with a "Safety-First" mentality, ensuring that even if the compute node fails, the entire application state and library can be recovered from the NAS.

## Core Components

- **Docker Compose**: Manages the Kavita application lifecycle and its associated data volumes (`config`, `data`).
    
- **NFS (QNAP NAS)**: Provides the primary storage backend for the e-book library and the destination for encrypted backups.
    
- **Restic**: Handles incremental, deduplicated, and encrypted backups of the entire application directory.
    
- **Systemd**: Orchestrates the backup schedule via a dedicated service and timer, ensuring consistency without manual intervention.
    
- **Ansible Vault**: Secures the Restic repository credentials, keeping sensitive passwords encrypted within the version control system.
    

## Project Structure

Plaintext
```
homelab/
├── ansible.cfg              # Global settings (Points to vault_pass.txt)
├── ansible/
│   ├── inventory.ini        # Defines [debiandocker] host
│   └── group_vars/all/
│       └── secrets.yaml     # Encrypted Restic/Kavita credentials
└── services/kavita/         # <--- You are here
    ├── deploy.yaml          # Main Playbook (Orchestrator)
    ├── compose.yaml         # Docker service definition
    ├── README.md            # Service documentation
    └── templates/           # Automation Blueprints
        ├── kavita-backup.sh.j2
        ├── kavita-backup.service.j2
        └── kavita-backup.timer.j2
```
## Design Decisions

- **Decoupled Storage (NFS)**: By mounting the QNAP NAS via NFS, the library data is isolated from the VM's OS disk. This allows for easy scaling of storage without resizing VM virtual disks.
    
- **Infrastructure as Code (IaC)**: Every component—from the NFS mount in `/etc/fstab` to the systemd timers—is defined in Ansible. This ensures the environment is reproducible and documented.
    
- **Automated Snapshotting**: Instead of simple file copies, Restic creates point-in-time snapshots. The `restic forget` policy is configured to retain 7 days of backups, balancing protection with storage efficiency.
    
- **Systemd-Managed Scheduling**: Moving away from standard `cron`, systemd timers provide better logging through `journalctl` and ensure that the backup service only triggers if the network and NFS mounts are online.
    
- **Security-Hardened Backups**: The backup script is deployed with strict permissions (`0700`), and Ansible uses `no_log` during deployment to prevent the Restic password from appearing in logs or terminal diffs.
    

## Security

- **Vaulted Credentials**: The master backup password is encrypted using AES-256 via Ansible Vault.
    
- **Root Squash Compatibility**: The deployment logic accounts for NFS `root_squash` settings, ensuring directory existence without failing on permission-restricted `chown` operations.
    
- **Encrypted Offsite-Ready Data**: Restic snapshots are encrypted at rest on the NAS, making them safe for potential future syncing to a public cloud (S3/B2).
    

# ⚡ Quick Start

To deploy or update Kavita and its backup system, navigate to this directory and run:

`ansible-playbook deploy.yaml`

### Management & Monitoring

**Manual Backup Trigger:** `sudo /usr/local/bin/kavita-backup.sh`

**Check Backup History:** `sudo -E bash -c 'source /usr/local/bin/kavita-backup.sh && restic snapshots'`

**Monitor Automation Logs:** `sudo journalctl -u kavita-backup.service -f`

**Verify Timer Schedule:** `systemctl status kavita-backup.timer`