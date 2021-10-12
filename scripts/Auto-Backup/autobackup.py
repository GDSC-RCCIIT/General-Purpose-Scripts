import os
import zipfile


def backup(folder):

    zip_name = os.path.basename(folder) + ".zip"
    destination = input("Enter the destination folder:\n")

    print(f"Creating file {zip_name}")
    backupzip = zipfile.ZipFile(f"{destination}\\{zip_name}", "w")

    for files in os.listdir(folder):
        if files.endswith(".zip"):
            continue
        backupzip.write(files)
        if os.path.isdir(files):
            for f in os.listdir(files):
                backupzip.write(f"{files}\\{f}")

    backupzip.close()
    print("The zip file has been created in your destination folder.")


source_folder = input("Enter the path of the source folder:\n")
os.chdir(source_folder)
backup(source_folder)
