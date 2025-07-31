import subprocess
import argparse
import re
import random

def get_current_mac(interface):
    try:
        output = subprocess.check_output(["ip", "link", "show", interface]).decode()
        mac_search = re.search(r"ether\s([\da-fA-F:]{17})", output)
        if mac_search:
            return mac_search.group(1)
    except subprocess.CalledProcessError:
        return None

def spoof_mac(interface, new_mac):
    subprocess.call(["ip", "link", "set", interface, "down"])
    subprocess.call(["ip", "link", "set", interface, "address", new_mac])
    subprocess.call(["ip", "link", "set", interface, "up"])

def generate_random_mac():
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: f"{x:02x}", mac))

def main():
    parser = argparse.ArgumentParser(description="CrackMac - MAC Address Spoofer Tool")
    parser.add_argument("-i", "--interface", required=True, help="Network interface (e.g., eth0, wlan0)")
    parser.add_argument("-m", "--mac", help="New MAC address (optional)")
    parser.add_argument("-r", "--random", action="store_true", help="Generate random MAC address")
    parser.add_argument("-c", "--check", action="store_true", help="Check current MAC address")

    args = parser.parse_args()

    if args.check:
        mac = get_current_mac(args.interface)
        if mac:
            print(f"Current MAC address for {args.interface}: {mac}")
        else:
            print("Could not read MAC address.")
        return

    if args.random:
        new_mac = generate_random_mac()
    elif args.mac:
        new_mac = args.mac
    else:
        print("Please specify a MAC address with -m or use -r for a random one.")
        return

    print(f"Changing MAC address of {args.interface} to {new_mac}")
    spoof_mac(args.interface, new_mac)
    print("MAC address changed successfully.")

if __name__ == "__main__":
    main()
