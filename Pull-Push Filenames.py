# Define the file path (replace 'numbers.txt' with the actual file path)
file_path = 'numbers.txt'

# Initialize an empty list to store the numbers
numbers_list = []

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the file line by line
    for line in file:
        # Strip any whitespace characters like '\n' from the end of the line and convert to a number
        number = float(line.strip())  # Use int(line.strip()) if you are dealing with integers
        # Append the number to the list
        numbers_list.append(number)

# Print the list of numbers
print(numbers_list)