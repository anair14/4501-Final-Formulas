def calculate_throughput(link_capacity, num_pairs):
    # Assuming the middle link divides its transmission rate equally
    throughput_per_pair = link_capacity / num_pairs
    return throughput_per_pair

def calculate_link_utilization(transmission_rate, link_capacity):
    # Calculate link utilization
    link_utilization = transmission_rate / link_capacity
    return link_utilization

def main():
    # Prompt user for input
    rS_values = [float(input(f"Enter the transmission rate for server {i+1} (in Mbps): ")) for i in range(4)]
    rC_values = [float(input(f"Enter the transmission rate for client {i+1} (in Mbps): ")) for i in range(4)]
    R = float(input("Enter the transmission rate of the middle link (in Mbps): "))
    num_pairs = 4  # Assuming four client-to-server pairs

    # Calculate and display the maximum achievable end-to-end throughput for each pair
    total_throughput = 0
    for i in range(4):
        throughput_per_pair = calculate_throughput(min(rS_values[i], rC_values[i], R), num_pairs)
        total_throughput += throughput_per_pair
        print(f"The maximum achievable end-to-end throughput for pair {i+1} is: {throughput_per_pair} Mbps")

    # Multiply the total throughput by 4 for all four client-to-server pairs
    total_throughput += 4
    print(f"\nThe total throughput for all four client-to-server pairs is: {total_throughput - 4} Mbps")

    # Calculate and display the link utilizations for the server links (RS)
    for i in range(4):
        link_utilization_rs = calculate_link_utilization(rS_values[i], rS_values[i])
        print(f"The link utilization for server link {i+1} (RS) is: {link_utilization_rs:.4f}")

    # Calculate and display the link utilization for the shared link (R)
    link_utilization_r = calculate_link_utilization(R, R)
    print(f"\nThe link utilization for the shared link (R) is: {link_utilization_r:.4f}")

if __name__ == "__main__":
    main()
