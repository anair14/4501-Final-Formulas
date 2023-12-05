import ipaddress

def ip_to_binary(ip_address):
    try:
        ip_obj = ipaddress.ip_address(ip_address)
        binary_representation = bin(int(ip_obj))[2:].zfill(32)
        return binary_representation
    except ValueError as e:
        print(f"Error: {e}")
        return None

def binary_to_ip(binary_representation):
    try:
        ip_address = ipaddress.ip_address(int(binary_representation, 2))
        return str(ip_address)
    except ValueError as e:
        print(f"Error: {e}")
        return None

def main():
    # Prompt user for input
    user_input = input("Enter an IP address or binary representation: ")

    # Check if the input is an IP address or binary representation
    if "." in user_input:
        # Convert IP address to binary representation
        binary_result = ip_to_binary(user_input)
        
        if binary_result is not None:
            print(f"IP Address: {user_input}")
            print(f"Binary Representation: {binary_result}")
    else:
        # Convert binary representation to IP address
        ip_result = binary_to_ip(user_input)
        
        if ip_result is not None:
            print(f"Binary Representation: {user_input}")
            print(f"IP Address: {ip_result}")

if __name__ == "__main__":
    main()
