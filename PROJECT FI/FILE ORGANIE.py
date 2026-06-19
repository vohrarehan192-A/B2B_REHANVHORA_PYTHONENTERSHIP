import os
import shutil

# Folder to organize
folder_path = input("Enter the folder path to organize: ")

# Check if folder exists
if not os.path.exists(folder_path):
    print("Folder does not exist!")
    exit()

# Organize files
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Get file extension
    extension = os.path.splitext(file_name)[1].lower()

    # Handle files without extensions
    if extension == "":
        folder_name = "No_Extension"
    else:
        folder_name = extension[1:].upper() + "_Files"

    # Create folder if it doesn't exist
    destination_folder = os.path.join(folder_path, folder_name)
    os.makedirs(destination_folder, exist_ok=True)

    # Move file
    destination_path = os.path.join(destination_folder, file_name)
    shutil.move(file_path, destination_path)

print("✅ Files organized successfully!")