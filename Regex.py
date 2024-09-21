
import os
import re
import shutil

def organize_files(source_folder, destination_folder):
    pattern = re.compile(r'\.([a-zA-Z0-9]+)$')

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path):
            match = pattern.search(filename)
            if match:
                file_type = match.group(1)
                folder_path = os.path.join(destination_folder, file_type)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved {filename} to {folder_path}")

if __name__ == "__main__":
    source_folder = r"C:\Users\mattp\Downloads"
    destination_folder = r"C:\Users\mattp\Desktop"

    organize_files(source_folder, destination_folder)
