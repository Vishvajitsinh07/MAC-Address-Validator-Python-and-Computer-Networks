import re

def is_valid_mac_address(mac):
    patterns = [
        r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$",
        r"^([0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}$",
        r"^[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}$"
    ]

    for pattern in patterns:
        if re.match(pattern, mac):
            return True
    return False

def print_instructions():
    print("Welcome to the MAC Address Validator!")
    print("Supported MAC address formats:")
    print("  1. XX:XX:XX:XX:XX:XX")
    print("  2. XX-XX-XX-XX-XX-XX")
    print("  3. XXXX.XXXX.XXXX")
    print("Type 'exit' to quit the program.")

def main():
    print_instructions()
    while True:
        mac = input("Enter a MAC address (or type 'exit' to quit): ").strip()
        if mac.lower() == 'exit':
            print("Thank you for using the MAC Address Validator. Goodbye!")
            break
        if is_valid_mac_address(mac):
            print(f"{mac} is a valid MAC address.")
        else:
            print(f"{mac} is NOT a valid MAC address.")

if __name__ == "__main__":
    main()
