def calculate_packet_delay(proc_delay, queue_delay, trans_delay, prop_delay):
    nodal_delay = proc_delay + queue_delay + trans_delay + prop_delay
    return nodal_delay

def main():
    # Prompt user for input
    proc_delay = float(input("Enter processing delay (d_proc) in milliseconds: "))
    queue_delay = float(input("Enter queueing delay (d_queue) in milliseconds: "))
    trans_delay = float(input("Enter transmission delay (d_trans) in milliseconds: "))
    prop_delay = float(input("Enter propagation delay (d_prop) in milliseconds: "))

    # Calculate and display packet delay
    nodal_delay = calculate_packet_delay(proc_delay, queue_delay, trans_delay, prop_delay)

    print(f"The total packet delay (d_nodal) is: {nodal_delay} milliseconds")

if __name__ == "__main__":
    main()
