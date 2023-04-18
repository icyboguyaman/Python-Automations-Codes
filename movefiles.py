import os
import shutil

# Set the path of the source folder
src_folder = 'path/to/source/folder'

# Set the path of the destination folder
dest_folder = 'path/to/destination/folder'

# Set the file extension of the files you want to move
file_extension = '.txt'

# Loop through all the files in the source folder
for filename in os.listdir(src_folder):
    # Check if the file has the desired extension
    if filename.endswith(file_extension):
        # Create the full path of the source file
        src_file = os.path.join(src_folder, filename)
        # Create the full path of the destination file
        dest_file = os.path.join(dest_folder, filename)
        # Move the file to the destination folder
        shutil.move(src_file, dest_file)
        print(f'Moved file: {filename}')

print('All files have been moved.')
