import ipaddress

def ip_to_dotted_decimal(ip_address):
    try:
        ip_obj = ipaddress.ip_address(ip_address)
        dotted_decimal = str(ip_obj)
        return dotted_decimal
    except ValueError as e:
        print(f"Error: {e}")
        return None

def dotted_decimal_to_ip(dotted_decimal):
    try:
        ip_obj = ipaddress.ip_address(dotted_decimal)
        ip_address = int(ip_obj)
        return ip_address
    except ValueError as e:
        print(f"Error: {e}")
        return None

def main():
    # Prompt user for input
    user_input = input("Enter an IP address or dotted-decimal notation: ")

    # Check if the input is an IP address or dotted-decimal notation
    if "." in user_input:
        # Convert dotted-decimal notation to IP address
        ip_address_result = dotted_decimal_to_ip(user_input)

        if ip_address_result is not None:
            print(f"Dotted-Decimal Notation: {user_input}")
            print(f"IP Address: {ip_address_result}")
    else:
        # Convert IP address to dotted-decimal notation
        dotted_decimal_result = ip_to_dotted_decimal(user_input)

        if dotted_decimal_result is not None:
            print(f"IP Address: {user_input}")
            print(f"Dotted-Decimal Notation: {dotted_decimal_result}")

if __name__ == "__main__":
    main()
