import os
from gtts import gTTS

# Beginning:
resp = int(
    input(
        """Convert text to speech\n\nPress:\n\t<1> To enter text by typing\n\t<2> To scan text from a text file\n >> """
    )
)

if resp == 1:
    # The text that you want to convert to audio

    mytext = input("Enter text here:\n")
    language = "en"
    filteredtext = ""
    for i in mytext:
        if i == " ":
            continue
        filteredtext += i
    # Language in which you want to convert

    """ Passing the text and language to the engine, here we have marked slow=False. This tells the module that the converted audio should have a high speed."""

    # Checking whether the input text is correct or not.

    if filteredtext.isalpha():
        myobj = gTTS(text=mytext, lang=language, slow=False)
    else:
        myobj = gTTS("Please enter valid text", lang=language, slow=False)

    # Saving the converted audio in a mp3 file named convertedaud

    myobj.save("voice.mp3")

    # Playing the converted file
    os.system("voice.mp3")

elif resp == 2:
    # You will need to enter the path of the text file in the terminal.

    file_path = input("Enter file path here:\n")

    FLIST = open(file_path, "r").read().replace("\n", " ")

    print("Please wait...Processing")

    # Checking whether the text file contains valid text or not.

    filteredtext = ""
    for i in FLIST:
        if i == " ":
            continue
        filteredtext += i

    if filteredtext.isalpha():
        TTS = gTTS(text=str(FLIST), lang="en-uk", slow=False)
    else:
        TTS = gTTS("Please enter a file with valid text", lang="en-uk", slow=False)

    # Save to mp3 in current dir.

    TTS.save("voice.mp3")

    # Plays the mp3 using the default app on your system that is linked to mp3s.

    print(FLIST)
    os.system("start voice.mp3")
else:
    print("Invalid input")
