
import os
import shutil


print("Welcome to the File Organizer!")

folder_path = input("Enter the Folder Path: ")

if not os.path.exists(folder_path):
    print("The specified folder path does not exist.")
    exit()

files = os.listdir(folder_path)

print("Files are Organizing...")

for file in files:
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        file_name, file_extension = os.path.splitext(file)

        if file_extension == ".pdf":
            folder_name = "PDF Files"
        elif file_extension == ".txt":
            folder_name = "Text Files"
        elif file_extension == ".py":
            folder_name = "Python Files"
        elif file_extension in [".jpg", ".jpeg", ".png"]:
            folder_name = "Image Files"
        else:
            folder_name = "Other Files"

        destination_folder = os.path.join(folder_path, folder_name)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        destination_path = os.path.join(destination_folder, file)
        shutil.move(file_path, destination_path)

        print(f"Moved '{file}' to '{destination_folder}'")
        # print(f"File: {file}")
        # print(f"File Extension: {file_extension}")
        # print("-"*20)
print("\nFiles Organized Successfully!")

