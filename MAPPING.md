# Proxies

## Management Proxy
Location: Raspberry Pi
Network: VLAN10
Purpose: Accessing management interfaces.

## App Proxy
Location: pve01
Network: VLAN 20
Purpose: Accessing self-hosted services
Services: vars/services.yaml

## VPS Proxy
Location: Debin-VPS
Network: Default
Purpose: Accessing VPS-hosted services
    - Website
    - KnowledgeBase
