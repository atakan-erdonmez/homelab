# restic_backup

Deploys Restic-based backups for service data stored on NFS.

## Required variables on the playbook

- `base_dir`
- `nfs_server`
- `nfs_path`
- `mount_point`
- `restic_password`

#### Suggested use:
- `base_dir: "/opt/services/<service>`
- `nfs_server: "192.168.10.103"`
- `nfs_path: "/services/<service>"`
- `mount_point: "/mnt/services/freshrss"`
- `restic_password: "{{ <service>_restic_backup_pw }}"`


## Default variables

```
backup_service_name: "{{ base_dir | basename }}"
restic_cache_dir: "/var/cache/restic/{{ backup_service_name }}"  
backup_script_path: "/usr/local/bin/{{ backup_service_name }}-backup.sh"  
restic_repo: "{{ mount_point }}/repo"

backup_retention_daily: 7
backup_on_calendar: "*-*-* 02:00:00"
backup_randomized_delay_sec: 300
backup_nfs_mount_opts: "nfsvers=4.0,defaults,_netdev,noatime,timeo=600,retrans=5,x-systemd.automount,x-systemd.idle-timeout=600"
backup_run_user: "root"
```

These can be explicitly specified in the playbook if needed.

## Example use in playbook

```
roles:
  - restic_backup
```