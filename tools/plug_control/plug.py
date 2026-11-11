import asyncio
import sys
from tapo import ApiClient

IP = "192.168.1.9"
EMAIL = "atakanerdonmez06@gmail.com"
PASSWORD = "CbhTT3YYGZIU9d7jpGU8"

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
