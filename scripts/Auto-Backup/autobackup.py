import os
import zipfile


def backup(folder):
    folder = os.path.abspath(folder)

    zip_name = os.path.basename(folder) + ".zip"
    destination = input("Enter the destination folder:\n")

    print(f"Creating file {zip_name}")
    backupzip = zipfile.ZipFile(f"{destination}\\{zip_name}", "w")

    for _, dirname, files in os.walk(folder):
        for folder in dirname:
            backupzip.write(folder)

        for file in files:
            if file.endswith(".zip"):
                continue
            backupzip.write(file)
        break

    backupzip.close()
    print("The zip file has been created in your destination folder.")


source_folder = input("Enter the path of the source folder:\n")
backup(source_folder)
