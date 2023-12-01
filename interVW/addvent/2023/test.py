file_path = "inputday1a.txt"  # Replace with your file path

# Initialize the sum of calibration values
total_calibration_sum = 0

# Open the file in read mode
with open(file_path, "r") as file:
    # Iterate through each line in the file
    for line in file:
        # Extract the first and last digits
        first_digit = int(line[0])
        last_digit = int(line[-1])

        # Combine the first and last digits to form a two-digit number
        calibration_value = (first_digit * 10) + last_digit

        # Add the calibration value to the total sum
        total_calibration_sum += calibration_value

# Print the sum of all calibration values
print("Sum of Calibration Values:", total_calibration_sum)