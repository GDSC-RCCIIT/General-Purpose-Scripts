import os
import sys
import platform
import subprocess
import pyperclip

# Seeing if the file exists
if os.path.exists(sys.argv[1]):
    f = open(sys.argv[1], "r")
    f_contents = f.read()
    f.close()
else:
    print(
        "Usage: python clipboard.py file_name\n      OR\n       python clipboard.py 'path_of_the_file'"
    )
    exit(1)

whatos = platform.system()

if whatos == "Darwin":
    subprocess.run("pbcopy", universal_newlines=True, input=f_contents)
    print("Success! Copied to clipboard.")
elif whatos == "Linux":
    pyperclip.copy(f_contents)
    print("Success! Copied to clipboard.")
elif whatos == "Windows":
    subprocess.run("clip", universal_newlines=True, input=f_contents)
    print("Success! Copied to clipboard.")
else:
    print("Failed! Clipboard not supported.")
