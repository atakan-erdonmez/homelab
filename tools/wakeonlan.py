import json, os

# --- CONFIGURATION ---
# Format: "Device Name": "MAC_ADDRESS"

def load_devices():
    # load devices from ./devices.json
    try:
        return json.load(open("devices.json"))
    except FileNotFoundError:
        print("Error: devices.json missing. Create it first!")
    except json.JSONDecodeError:
        print("Error: devices.json is broken (check your commas/quotes).")
    return {}

def main():
    DEVICES = load_devices()
    if not DEVICES: return
    
    print("--- Wake-on-LAN Controller ---")
    device_names = list(DEVICES.keys())
    
    # List the devices
    for i, name in enumerate(device_names, 1):
        print(f"{i}. {name}")
    
    try:
        # Ask which device
        choice = int(input("\nWhich device you want to turn on? (Enter number): "))
        
        if 1 <= choice <= len(device_names):
            target_name = device_names[choice - 1]
            target_mac = DEVICES[target_name]
            
            print(f"Sending wake signal to {target_name} ({target_mac})...")
            
            # Execute the system command 'wakeonlan <MAC>'
            os.system(f"wakeonlan {target_mac}")
        else:
            print("Error: Number out of range.")
            
    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()
