import pyttsx3
import PyPDF2

print("WELCOME TO AUDIOBOOK")
filename = input("Enter name of input file(with .pdf extension):")
book = open(filename, "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)  # prints number of pages

speaker = pyttsx3.init()  # Initialize the speaker
rate = speaker.getProperty("rate")

user_rate = int(input("At what rate do you want to hear Audiobook?"))       #taking reading rate input from user
speaker.setProperty("rate", user_rate)
# rate=170 is normal speed, you can increase and decrease as per your convenience

speaker = pyttsx3.init()
user_input = int(input("Enter the starting page:"))
for i in range(user_input, pages):
    page = pdfReader.getPage(i)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()
print("Thank you")
