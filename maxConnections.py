def calculate_max_connections(lengths, num_hops):
    max_connections = (sum(lengths) // num_hops) - 2
    return max_connections

def main():
    # Ask user for input
    num_hops = int(input("Enter the number of consecutive hops required for each connection: "))
    
    # Ask user for lengths between circuits
    length_AB = int(input("Enter the number of circuits between A and B: "))
    length_BC = int(input("Enter the number of circuits between B and C: "))
    length_CD = int(input("Enter the number of circuits between C and D: "))
    length_DA = int(input("Enter the number of circuits between D and A: "))

    # Calculate and display the maximum number of ongoing connections
    lengths = [length_AB, length_BC, length_CD, length_DA]
    max_connections = calculate_max_connections(lengths, num_hops)

    print(f"The maximum number of ongoing connections in the network is: {max_connections}")

if __name__ == "__main__":
    main()
