import os
from collections import Counter

# Clear the screen (for Windows)
os.system('cls')

# Print introductory message
print("Simple Yamaha Gear Calculator tool, for use with the Yamaha Datalogger to work out gears!")
print("Provide data in rows of 6x8 for each gear, you can input all rows at once!")
print("Input data expects raw hex from Kline, example: 01 37 06 00 2E 6B")
print("Outputs, Gear name: RPM (Most Common): Constant:")

# Input the number of gears
num_gears = int(input("\nEnter the number of gears: "))

# Initialize a dictionary to store gear data
gear_data = {}

# Collect RPM and speed data for each gear
for gear_number in range(1, num_gears + 1):
    RPM_values = []  # List to store RPM values for each data block
    total_speed_hex = '0x0000'
    for i in range(8):
        data_block = input(f"Enter data block {i + 1} for gear {gear_number} (e.g., '01 37 01 00 2B 63'): ")
        parts = data_block.split()
        if len(parts) >= 3:
            RPM_hex = parts[1]
            RPM_values.append(RPM_hex)  # Store the RPM value for this data block
            speed_hex = parts[2]
            total_speed_hex = hex(int(total_speed_hex, 16) + int(speed_hex, 16))
    
    # Count the RPM values and pick the most common one
    most_common_RPM = Counter(RPM_values).most_common(1)[0][0]
    RPM_decimal = int(most_common_RPM, 16)
    
    # Calculate the constant for this gear
    speed_decimal = int(total_speed_hex, 16)
    gear_constant = (speed_decimal / RPM_decimal * 50)
    
    gear_data[f"Gear {gear_number}"] = (most_common_RPM, gear_constant)

# Display the results, including gear RPM (most common) and constant
for gear_name, (most_common_RPM, gear_constant) in gear_data.items():
    print(f"\n{gear_name}: Constant {gear_constant:.2f}")

# Prevent the script from closing automatically
input("\nPress Enter to quit!")
