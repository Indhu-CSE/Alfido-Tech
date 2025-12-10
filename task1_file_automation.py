import os
import logging
from datetime import datetime

# --------------------------
# LOGGING CONFIGURATION
# --------------------------
log_filename = f"file_operations_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(filename=log_filename, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def sort_files(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path):
                extension = filename.split('.')[-1]

                # Create folder if not exists
                folder_name = os.path.join(folder_path, extension)
                if not os.path.exists(folder_name):
                    os.mkdir(folder_name)
                    logging.info(f"Created folder: {folder_name}")

                # Move file to extension folder
                new_path = os.path.join(folder_name, filename)
                os.rename(file_path, new_path)
                logging.info(f"Moved {filename} → {extension}/")

    except Exception as e:
        logging.error(f"Error while sorting files: {e}")
        print("An error occurred while sorting files.")

def rename_files(folder_path, prefix):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path):
                new_name = prefix + "_" + filename
                new_path = os.path.join(folder_path, new_name)

                os.rename(file_path, new_path)
                logging.info(f"Renamed {filename} → {new_name}")

    except Exception as e:
        logging.error(f"Error while renaming: {e}")
        print("An error occurred while renaming files.")

def delete_temp_files(folder_path):
    try:
        removed = 0
        for filename in os.listdir(folder_path):
            if filename.endswith(('.tmp', '.log', '.cache')):
                file_path = os.path.join(folder_path, filename)
                os.remove(file_path)
                removed += 1
                logging.info(f"Deleted temp file: {filename}")

        print(f"{removed} temporary files deleted.")

    except Exception as e:
        logging.error(f"Error while deleting temp files: {e}")
        print("An error occurred while deleting temp files.")

# --------------------------
# MAIN PROGRAM
# --------------------------
print("📁 FILE AUTOMATION TOOL")
print("1. Sort Files")
print("2. Rename Files")
print("3. Delete Temporary Files")
print("4. Exit")

folder = input("Enter the folder path: ")

choice = input("Enter your choice: ")

if choice == "1":
    sort_files(folder)
    print("Files sorted successfully!")

elif choice == "2":
    prefix = input("Enter prefix for renaming: ")
    rename_files(folder, prefix)
    print("Files renamed successfully!")

elif choice == "3":
    delete_temp_files(folder)

elif choice == "4":
    print("Exiting...")

else:
    print("Invalid choice!")

print(f"Log file created: {log_filename}")
