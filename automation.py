import os
import shutil
from datetime import datetime

# Define the directories to scan for subfolders
subfolder_scan_dirs = [
    r"C:\Users\nmkoninn\Downloads",
    r"C:\Users\nmkoninn\Pictures",
    r"C:\Users\nmkoninn\Music",
    r"C:\Users\nmkoninn\Videos",
    r"B:\\",
    r"E:\\"
]

# Get the current date in DD-MM-YYYY format
current_date = datetime.now().strftime("%d-%m-%Y")
organized_dir = os.path.join(r"C:\Users\nmkoninn\Desktop\Organized", current_date)

# Create the dated folder if it doesn't exist
if not os.path.exists(organized_dir):
    os.makedirs(organized_dir)

# Function to copy subfolders and their contents
def copy_subfolders(source_dir, target_dir):
    for root, dirs, files in os.walk(source_dir):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            # Construct the destination path for the subfolder
            target_subfolder = os.path.join(target_dir, dir_name)

            # Copy the subfolder and its contents to the target location
            if not os.path.exists(target_subfolder):
                shutil.copytree(dir_path, target_subfolder)

# Function to organize miscellaneous files from top-level only (ignoring subfolders)
def organize_misc_files(source_dir, target_dir):
    for file in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file)

        # Process only files, skip directories
        if os.path.isfile(file_path):
            # Get the file extension
            file_ext = os.path.splitext(file)[1].lower().replace('.', '')  # Remove the dot and make lowercase
            if not file_ext:
                file_ext = 'unknown'  # For files without an extension

            # Create a folder for the file extension if it doesn't exist
            ext_folder = os.path.join(target_dir, file_ext)
            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)

            # Move the file to the appropriate folder
            dst_file = os.path.join(ext_folder, file)

            # Avoid overwriting files with the same name
            if not os.path.exists(dst_file):
                shutil.move(file_path, dst_file)
            else:
                # Rename the file if it already exists
                base_name, ext = os.path.splitext(file)
                counter = 1
                new_dst_file = os.path.join(ext_folder, f"{base_name}_{counter}{ext}")
                while os.path.exists(new_dst_file):
                    counter += 1
                    new_dst_file = os.path.join(ext_folder, f"{base_name}_{counter}{ext}")
                shutil.move(file_path, new_dst_file)

# Loop through each home directory to copy subfolders and their contents
for home_dir in subfolder_scan_dirs:
    if os.path.exists(home_dir):
        print(f"Copying subfolders and their contents from: {home_dir}")
        copy_subfolders(home_dir, organized_dir)

# Now process top-level files from Desktop and Documents (no subfolders)
for base_dir in [r"C:\Users\nmkoninn\Desktop", r"C:\Users\nmkoninn\Documents"]:
    if os.path.exists(base_dir):
        print(f"Organizing miscellaneous files in directory: {base_dir}")
        organize_misc_files(base_dir, organized_dir)

print("Subfolders and miscellaneous files have been sorted and organized successfully!")
