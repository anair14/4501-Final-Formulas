import ipaddress

def ip_port_to_binary(ip_address, port):
    try:
        # Parse the IP address
        ip_obj = ipaddress.ip_address(ip_address)
        
        # Convert IP address to binary format
        binary_ip = bin(int(ip_obj))[2:].zfill(32)

        # Convert port to binary format
        binary_port = bin(int(port))[2:].zfill(16)

        return binary_ip, binary_port
    except ValueError as e:
        print(f"Error: {e}")
        return None, None

def main():
    # Prompt user for input
    ip_address = input("Enter IP address (e.g., 200.23.16.0): ")
    port = input("Enter port (e.g., 80): ")

    # Convert IP address and port to binary format
    binary_ip, binary_port = ip_port_to_binary(ip_address, port)

    if binary_ip is not None and binary_port is not None:
        print(f"Binary IP Address: {binary_ip}")
        print(f"Binary Port: {binary_port}")

if __name__ == "__main__":
    main()
