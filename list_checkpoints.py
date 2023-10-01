
import os

# List all files in the checkpoints directory
dir_path = 'checkpoints'
files = os.listdir(dir_path)

# Print the filenames and deduce their roles based on naming conventions
for file in files:
    print(f'File: {file}')