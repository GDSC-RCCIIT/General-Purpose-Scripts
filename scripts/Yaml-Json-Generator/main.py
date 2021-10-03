import os
import yaml
import json

directory_path = os.path.abspath(input("Please enter your directory relative path: "))
directory_list = os.listdir(directory_path)

if not any(".yaml" in string for string in directory_list):
    print("No YAML file(s) found.")
    exit(1)

for files in directory_list:
    if files.endswith(".yaml"):
        file_path = directory_path + "/" + files
        with open(file_path, "r") as stream:
            try:
                yaml_file = yaml.safe_load(stream)
                json_file_name = os.path.splitext(files)[0] + ".json"
                json_file_path = directory_path + "/" + json_file_name
                print("Processing " + json_file_name + " ...")
                json_file = open(json_file_path, "w")
                json_file.write(json.dumps(yaml_file))
                json_file.close()
            except yaml.YAMLError as e:
                print(e)
                exit(1)
    else:
        continue

print("Done !")
