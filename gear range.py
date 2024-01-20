import os
from collections import Counter

# Clear the screen (for Windows)
os.system('cls')

print("Simple Yamaha Gear Calculator tool, for use with the Yamaha Datalogger to work out gears!")
print("Provide data in rows of 6x8 for each gear, you can input all rows at once!")
print("Input data expects raw hex from Kline, example: 01 37 06 00 2E 6B")
print("Outputs, Gear name: RPM (Most Common): Constant:")

num_gears = int(input("\nEnter the number of gears: "))

gear_results = []

for gear_number in range(1, num_gears + 1):
    RPM_values = []  # List to store RPM values for each data block
    total_speed_hex = 0  # Reset total speed for each gear
    for i in range(8):
        data_block = input(f"Enter data block {i + 1} for gear {gear_number} (e.g., '01 37 01 00 2B 63'): ")
        parts = data_block.split()
        if len(parts) >= 3:
            RPM_hex = parts[1]
            RPM_values.append(RPM_hex)  # Store the RPM value for this data block
            speed_hex = parts[2]
            total_speed_hex += int(speed_hex, 16)  # Sum up speed values

    most_common_RPM = Counter(RPM_values).most_common(1)[0][0]
    RPM_decimal = int(most_common_RPM, 16) * 50  # Multiply the RPM by 50

    # Use total speed directly for the constant calculation
    gear_constant = total_speed_hex / RPM_decimal if RPM_decimal != 0 else 0

    # Scale the gear constant by 10000 and convert to uint16_t
    scaled_gear_constant = int(gear_constant * 10000)

    gear_results.append((gear_number, RPM_decimal, total_speed_hex, scaled_gear_constant))

# Displaying results at the end
for gear_number, RPM, total_speed, scaled_gear_constant in gear_results:
    print(f"\nGear {gear_number}: RPM {RPM}: Total Speed {total_speed}: Constant {scaled_gear_constant}")

input("\nPress Enter to quit!")
