# Imports
import language_tool_python
import argparse
from pathlib import Path

# ------------------------------------------------------
# Initialize API
tool = language_tool_python.LanguageToolPublicAPI("en-US")

# get the input text file from the user
parser = argparse.ArgumentParser(description="Grammar Checker Bot")
parser.add_argument("-i", "--input_file_path", help="Input file name", required=True)
p = parser.parse_args()


# open the file provided and read it
f = open(p.input_file_path, "r")
text = f.read()

# get the mistakes and corrections
matches = tool.check(text)

# use the corrections and update the mistakes
my_mistakes = []
my_corrections = []
start_positions = []
end_positions = []

# parsing the rules
for rules in matches:
    # print("------------------------------")
    # print(rules, "/n")
    if len(rules.replacements) > 0:
        start_positions.append(rules.offset)
        end_positions.append(rules.errorLength + rules.offset)
        my_mistakes.append(text[rules.offset : rules.errorLength + rules.offset])
        my_corrections.append(rules.replacements[0])

my_new_text = list(text)

for m in range(len(start_positions)):
    for i in range(len(text)):
        my_new_text[start_positions[m]] = my_corrections[m]
        if i > start_positions[m] and i < end_positions[m]:
            my_new_text[i] = ""

my_new_text = "".join(my_new_text)

# save the text in a file
f = open("output.txt", "w")
f = open("output.txt", "a")
f.write(my_new_text)
f.close()

# print for debug
print("Text with errors - \n", text)
print("\n")
print("Text after fixing the errors\n", my_new_text)
