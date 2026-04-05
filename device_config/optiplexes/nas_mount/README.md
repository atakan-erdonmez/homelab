# Mount NAS to Proxmox Nodes

This deployment mounts my NAS into Proxmox nodes using NFS. 

I am directly editing config files and using Proxmox commands instead of using Proxmox GUI. This is because when I use GUI for mounting, even the parameters are the same, the NAS gives input/output error.

So, I mount the NFS share using the /etc/fstab file and mount command.

- **Source**: 192.168.10.103/infrastructure/proxmox
- **Destination**: /mnt/nas-proxmox
- **ID**: nas-proxmox

Then, I add the mount location as a directory, specifying parameters using the `pvesm` command.

Finally, I create a temp directory for local vzdump for performance.


## Manual Code

The manual process can be seen in the code below:


- fstab entry:
`192.168.10.103:/infrastructure/proxmox /mnt/nas-proxmox nfs nfsvers=4.0,hard,_netdev,noatime,timeo=600,retrans=10 0 0`

- Mounting:
```
mkdir /mnt/nas-proxmox
systemctl daemon-reload
mount -a
```

- Add directory & configure parameters:
```
pvesm add dir nas-proxmox --path /mnt/nas-proxmox --content backup,images,rootdir,vztmpl,iso
pvesm set nas-proxmox --content backup,images,rootdir,vztmpl,iso --prune-backups keep-last=5
```
- Add the 'tmpdir: /var/tmp' entry in the `/etc/vzdump.conf` file.