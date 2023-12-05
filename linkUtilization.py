def calculate_access_link_utilization(cache_hit_rate, access_link_capacity, origin_server_rate):
    cache_hit_rate = float(cache_hit_rate)
    access_link_capacity = float(access_link_capacity)
    origin_server_rate = float(origin_server_rate)

    # Calculate the rate to browsers over access link
    access_link_rate = (1 - cache_hit_rate) * origin_server_rate

    # Calculate access link utilization
    access_link_utilization = access_link_rate / access_link_capacity

    return access_link_utilization


def calculate_average_end_to_end_delay(cache_hit_rate, delay_origin_servers, delay_cache):
    cache_hit_rate = float(cache_hit_rate)
    delay_origin_servers = float(delay_origin_servers)
    delay_cache = float(delay_cache)

    # Calculate average end-to-end delay
    average_delay = cache_hit_rate * delay_cache + (1 - cache_hit_rate) * delay_origin_servers

    return average_delay


def main():
    # Prompt user for input
    cache_hit_rate = input("Enter cache hit rate (e.g., 0.4): ")
    access_link_capacity = input("Enter access link capacity (in Mbps, e.g., 1.54): ")
    origin_server_rate = input("Enter rate from origin servers (in Mbps, e.g., 2.01): ")
    delay_origin_servers = input("Enter delay from origin servers (in msec, e.g., 2.01): ")
    delay_cache = input("Enter delay when satisfied at cache (in msec, e.g., 0.5): ")

    # Calculate access link utilization
    access_link_utilization = calculate_access_link_utilization(cache_hit_rate, access_link_capacity, origin_server_rate)
    print(f"Access Link Utilization: {access_link_utilization:.2f}")

    # Calculate average end-to-end delay
    average_end_to_end_delay = calculate_average_end_to_end_delay(cache_hit_rate, delay_origin_servers, delay_cache)
    print(f"Average End-to-End Delay: {average_end_to_end_delay:.2f} msec")

if __name__ == "__main__":
    main()
