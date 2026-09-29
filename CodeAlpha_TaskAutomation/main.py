import os
import shutil

def move_jpg_files(source_folder, destination_folder):
    if not os.path.exists(source_folder):
        print("Source folder does not exist.")
        return

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    moved_files = 0

    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".jpg"):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            shutil.move(source_path, destination_path)
            print(f"Moved: {filename}")
            moved_files += 1

    print(f"\nTotal JPG files moved: {moved_files}")


source = input("Enter source folder path: ")
destination = input("Enter destination folder path: ")

move_jpg_files(source, destination)
