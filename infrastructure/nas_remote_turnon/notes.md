on rasp:

sudo apt update
sudo apt install python3-pip python3-venv -y
python3 -m venv ~/tapo-env
source ~/tapo-env/bin/activate
pip install python-kasa
pip install --upgrade tapo


script:

import asyncio
import sys
from tapo import ApiClient

IP = "192.168.1.9"
EMAIL = "your-tapo-email"
PASSWORD = "your-tapo-password"

async def main(action):
    client = ApiClient(EMAIL, PASSWORD)
    plug = await client.p110(IP)
    if action == "on":
        await plug.on()
    elif action == "off":
        await plug.off()
    else:
        print("Use: on or off")
        return
    print("Done:", action)

asyncio.run(main(sys.argv[1]))


# usage
~/tapo-env/bin/python /home/atakan/homelab/tools/plug_control/plug.py on

~/tapo-env/bin/python /home/atakan/homelab/tools/plug_control/plug.py off

