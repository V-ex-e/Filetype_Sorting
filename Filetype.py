import os
import shutil

def organize_files(source_folder, destination_folder):
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(filename)

            if file_extension:
                file_extension = file_extension[1:]  # Remove the leading dot
                folder_path = os.path.join(destination_folder, file_extension)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved {filename} to {folder_path}")

if __name__ == "__main__":
    #these ared the folders you needd to exchange for sorting folder and destination of the sorted folders
    source_folder = r"C:\Users\mattp\Downloads"
    destination_folder = r"C:\Users\mattp\Desktop"

    organize_files(source_folder, destination_folder)
