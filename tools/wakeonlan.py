import os

# --- CONFIGURATION ---
# Format: "Device Name": "MAC_ADDRESS"
DEVICES = {
    "Optiplex1": "AA:BB:CC:DD:EE:FF",
    "Optiplex2": "11:22:33:44:55:66",
    "NAS": "00:11:22:33:44:55"
}

def main():
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
