# Voice to text
Transcribes speech from inputted audio file using PocketSphinx. 

## Prerequisites
- Requires Python3
- Requires Anaconda to download swig (make sure to add anaconda to PATH)
- Now, open a terminal and use `conda install swig`
- Then download pocketsphinx using: `pip install pocketsphinx`
- Now finally download SpeechRecognition: `pip install SpeechRecognition`

# Usage Examples
- Output to terminal
```
$ python voice_to_text.py -p whatstheweatherlike.wav
```
- Output to file
```
$ python voice_to_text.py -p whatstheweatherlike.wav -o text.txt
```
- You can also use this script without the "python" for the sake of comfort on UNIX systems.
```
$ chmod +x voice_to_text.py
$ ./voice_to_text.py -p whatstheweatherlike.wav
```
