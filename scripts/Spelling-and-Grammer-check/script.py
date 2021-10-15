import language_tool_python
from spellchecker import SpellChecker

spell = SpellChecker()

# find those words that may be misspelled
misspelled = spell.unknown(["cmputr", "watr", "study", "wrte"])

for word in misspelled:
	# Get the one `most likely` answer
	print(spell.correction(word))

	# Get a list of `likely` options
	print(spell.candidates(word))




# Mention the language keyword
tool = language_tool_python.LanguageToolPublicAPI('en-US')
i = 0

# Path of file which needs to be checked
with open(r'/Users/mahal/Work/General-Purpose-Scripts/scripts/Spelling-and-Grammer-check/transcript.txt', 'r') as fin:
			
	for line in fin:
		matches = tool.check(line)
		i = i + len(matches)	
		pass

# prints total mistakes which are found
# from the document
print("No. of mistakes found in document is ", i)
print()
	
# prints mistake one by one
for mistake in matches:
	print(mistake)
	print()

