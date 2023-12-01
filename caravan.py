def calculate_caravan_lineup_time(propagation_speed, service_time, caravan_size):
    # Time to push entire caravan through toll booth
    total_service_time = service_time * caravan_size
    # Time for the last car to propagate from 1st to 2nd toll booth
    propagation_time = (caravan_size - 1) * (1 / propagation_speed)  # Assuming the caravan is lined up before the 2nd toll booth
    # Total time until caravan is lined up before 2nd toll booth
    total_time = total_service_time + propagation_time
    return total_time

def main():
    # Prompt user for input
    propagation_speed = float(input("Enter the speed of propagation (km/hr): "))
    service_time = float(input("Enter the service time at the toll booth (sec): "))
    caravan_size = int(input("Enter the number of cars in the caravan: "))

    # Calculate and display the time until caravan is lined up before 2nd toll booth
    lineup_time = calculate_caravan_lineup_time(propagation_speed, service_time, caravan_size)

    print(f"time to “push” entire caravan through toll booth onto highway: {lineup_time:.2f} seconds.")

if __name__ == "__main__":
    main()
