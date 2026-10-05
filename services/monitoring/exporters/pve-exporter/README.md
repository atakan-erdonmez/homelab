pve-exporter is used to export data about the Proxmox environment. It pulls the data from the Proxmox API from anywhere. Currently hosted in svc01.

It requires permissions & user:

Create the PVE users manually
NOTE: The reason why it is not automated is because it is hard to make it idompotent, since the user might have wrong permissions etc. Since this is a one time thing, it is ok to create it manually. commands are here:

# 1. Create a dedicated monitoring user
pveum user add monitoring@pve -comment "Monitoring read-only user"

# 2. Create a role with only audit (read-only) privileges
pveum role add monitoring -privs "VM.Audit,Pool.Audit,Datastore.Audit,Sys.Audit,SDN.Audit"

# 3. Assign the role at the root path (covers all nodes, VMs, storage)
pveum aclmod / -user monitoring@pve -role monitoring

# 4. Create API token with privilege separation DISABLED
pveum user token add monitoring@pve monitoring --privsep 0