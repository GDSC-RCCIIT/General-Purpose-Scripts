# Imports
import language_tool_python

# Initial API
tool = language_tool_python.LanguageToolPublicAPI("en-US")

# initalizae filename
FILENAME = "input.txt"

text = """ update your text here. tool will will fidn grammatically isues and fix it. you can use this text too see an few of of the problems that LanguageTool can detecd. What do you thinks of grammar checkers? Please not that they are not perfect."""

# get the mistakes and corrections
matches = tool.check(text)

# use the corrections and update the mistakes
my_mistakes = []
my_corrections = []
start_positions = []
end_positions = []

# parsing the rules
for rules in matches:
    print("------------------------------")
    print(rules, "/n")
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
f = open("myfile.txt", "w")
f = open("myfile.txt", "a")
f.write(my_new_text)
f.close()

print(my_new_text)
