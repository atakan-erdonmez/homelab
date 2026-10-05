For pve nodes:

# Node_Exporter
It exports hosts & hardware level metrics like CPU, RAM etc

follow guide: https://www.nxsi.io/blog/proxmox-monitoring-grafana-guide

1- create the requirements.yaml for using the role prometheus.prometheus
2- download collection with ansible galaxy
`ansible-galaxy collection install -r requirements.yaml`
3- run node_exporter 
    (creates user node-exp)
    systemctl status node_exporter.service
    runs on 9100

4-  




run ansible playbook to install prom, grafana, and pve-exporter