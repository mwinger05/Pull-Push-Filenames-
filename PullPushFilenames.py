import os
import shutil

# Prompt for the text file path
file_path = input("Enter the path to the text file (e.g., C:\\Users\\YourName\\Documents\\TestList.txt): ").strip('\"')

# Prompt for the directory to copy from
from_folder_path = input("Enter the path to the directory to copy from (e.g., C:\\Users\\YourName\\Documents\\FromFolder): ").strip('\"')

# Prompt for the directory to copy to
to_folder_path = input("Enter the path to the directory to copy to (e.g., C:\\Users\\YourName\\Documents\\ToFolder): ").strip('\"')

# Initialize an empty list to store the numbers
numbers_list = []

# Open the file in read mode
try:
    with open(file_path, 'r') as file:
        # Read the file line by line
        for line in file:
            # Strip any whitespace characters like '\n' from the end of the line and convert to a number
            numberString = line.strip()
            # Append the number to the list
            numbers_list.append(numberString)
except FileNotFoundError:
    print(f"The file at {file_path} was not found.")
    exit()

# Ensure the target directory exists
os.makedirs(to_folder_path, exist_ok=True)

# List all files in the directory
try:
    files_in_directory = os.listdir(from_folder_path)
except FileNotFoundError:
    print(f"The directory at {from_folder_path} was not found.")
    exit()

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
            try:
                shutil.copy(source_file_path, destination_file_path)
                print(f"Copied {filename} to {to_folder_path}")
                found = True
                break
            except Exception as e:
                print(f"Failed to copy {filename}. Error: {e}")
                exit()
    if not found:
        print(f"{number} not found in any file name")
