
<div style="border: 1px solid black; padding: 20px;">

# Yamaha Gear Calculator

<a href="https://ibb.co/ngvGd4d"><img src="https://i.ibb.co/5My0pCp/image.png" alt="image" border="0"></a>

This is a simple Yamaha Gear Calculator tool designed for use with the Yamaha Datalogger to work out gear ratios. It allows you to input data in rows of 6x8 for each gear and calculates gear variations and constants based on RPM and speed data.

## Usage

1. Provide data in rows of 6x8 for each gear. You can input all rows at once.
2. Input data expects raw hexadecimal data from Kline, for example: `01 37 06 00 2E 6B`.
3. Enter the number of gears you want to analyze when prompted.
4. Input RPM and speed data for each gear's 8 data blocks.
5. The tool will take the most common RPM in that block as the average
6. Calculating and displaying the constants for each gear.
