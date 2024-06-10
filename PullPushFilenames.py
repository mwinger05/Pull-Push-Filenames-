import os
import shutil

# Define the file path (replace 'numbers.txt' with the actual file path)
file_path = "C:\\Users\\Inspiron 15 5579\\OneDrive\\Documents\\Walsh Lab\\TestList.txt"

# Initialize an empty list to store the numbers
numbers_list = []

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the file line by line
    for line in file:
        # Strip any whitespace characters like '\n' from the end of the line and convert to a number
        numberString = line.strip()  # Use int(line.strip()) if you are dealing with integers
        # Append the number to the list
        numbers_list.append(numberString)

#create copy from variable
from_folder_path = "C:\\Users\\Inspiron 15 5579\\OneDrive\\Documents\\Walsh Lab"

#create copy to variable
to_folder_path = "C:\\Users\\Inspiron 15 5579\\OneDrive\\Documents\\Walsh Lab\\ToFolderPath"

# Ensure the target directory exists
os.makedirs(to_folder_path, exist_ok=True)

# List all files in the directory
files_in_directory = os.listdir(from_folder_path)

# Iterate through the numbers list and check each item
for number in numbers_list:
    found = False
    for filename in files_in_directory:
        if number in filename:
            print(f"{number} found in file name: {filename}")
            # Full path of the source file
            source_file_path = os.path.join(from_folder_path, filename)
            # Full path of the destination file
            destination_file_path = os.path.join(to_folder_path, filename)
            # Copy the file
            shutil.copy(source_file_path, destination_file_path)
            print(f"Copied {filename} to {to_folder_path}")
            found = True
            break
    if not found:
        print(f"{number} not found in any file name")
