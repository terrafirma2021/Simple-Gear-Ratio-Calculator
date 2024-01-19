import os

# Function to calculate gear based on RPM and speed
def calculate_gear(RPM, speed):
    # Convert RPM and speed from hex to decimal
    RPM_decimal = int(RPM, 16)
    speed_decimal = int(speed, 16)

    # Calculate the gear variation
    gear_variation = (speed_decimal / RPM_decimal) * 50

    return gear_variation

# Clear the screen (for Windows)
os.system('cls')

# Print introductory message
print("Simple Yamaha Gear Calculator tool, for use with the Yamaha Datalogger to work out gears!")
print("Provide data in rows of 6x8 for each gear, you can input all rows at once!")
print("Input data expects raw hex from Kline, example: 01 37 06 00 2E 6B")
print("Outputs, Gear name: Variation: Constant:")

# Input the number of gears
num_gears = int(input("\nEnter the number of gears: "))

# Initialize a dictionary to store gear data
gear_data = {}

# Collect RPM and speed data for each gear
for gear_number in range(1, num_gears + 1):
    total_RPM_hex = '0x0000'
    total_speed_hex = '0x0000'
    for i in range(8):
        data_block = input(f"Enter data block {i + 1} for gear {gear_number} (e.g., '01 37 01 00 2B 63'): ")
        parts = data_block.split()
        if len(parts) >= 3:
            RPM_hex = parts[1]
            speed_hex = parts[2]
            total_RPM_hex = hex(int(total_RPM_hex, 16) + int(RPM_hex, 16))
            total_speed_hex = hex(int(total_speed_hex, 16) + int(speed_hex, 16))
    
    gear_variation = calculate_gear(total_RPM_hex, total_speed_hex)
    gear_data[f"Gear {gear_number}"] = gear_variation

# Display the results, including gear constants
gear_constants = {}

for gear_name, gear_variation in gear_data.items():
    gear_constant = 1 / gear_variation
    gear_constants[gear_name] = gear_constant

    print(f"\n{gear_name}: Variation {gear_variation:.2f}, Constant {gear_constant:.2f}")

# Prevent the script from closing automatically
input("\nPress Enter to quit!")
