import os
import shutil

folder_path = r"D:\project rehan" 

file_categories = {
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

for file in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):

        _, extension = os.path.splitext(file)
        extension = extension.lower()

        for category, extensions in file_categories.items():

            if extension in extensions:

                destination_folder = os.path.join(folder_path, category)

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                shutil.move(
                    file_path,
                    os.path.join(destination_folder, file)
                )

                print(f"Moved: {file} → {category}")
                break

print("File organization completed!")