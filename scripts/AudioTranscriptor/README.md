## Audio Transcriptor

![python](https://img.shields.io/badge/language-Python-orange?style=for-the-badge)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=plasitc)](https://github.com/psf/black)

### About

This is a Audio Transcriptor python script , as the name suggests it does the automation of transcription of an audio file.

Here the transcription can be done in two ways:
1)Audio file to text 
2)Speech to text.

In the first one, we will be specifying the audio file for which we want to transcript.While in the second one, we need to speak through microphone , so that it recognizes and converts it. In both the cases, the text generated due transcription will be saved in a seperate text file , which we also specify.

### Setup

#### 1)Installing Libraries
You need to install following libraries for this script
* `pip install SpeechRecognition pydub`
* If you are using Windows :
    `pip install pyaudio`
  If you are using MacOS:
    `brew install portaudio`
    `pip install pyaudio`
  If you are using Linux:
    `sudo apt-get install python-pyaudio python3-pyaudio`
    `pip install pyaudio`

#### 2)Process
* Run the code in any code editor you want or in python IDLE.
* It asks for select any one option.If you wish to transcript audio file, then give 1 else if you wish to transcript speech give 2.
* Create a empty new text/doc file(.txt file is recommended) in any location you want and copy its full path (full path looks like `/Users/monishpalisetti/Desktop/Untitled.txt`)
* Now give this path as input where it asks for text file location.
* If you chosen option 1, similarly give the audio file path, where it asks for the input. Generally , they have extensions `.wav`.You can try some sample audio files which I included in this repository.
* After few seconds the text, which is the transcribed text from the audio  would be displayed , and the same text will be copied in the new text file.
* Now if you chosen option 2, Try to spaeak something when it displays `talk`.After 5 sec, what you spoke will be displayed, and you can talk again.The whole text , which is transcribed from your speech is copied to the text file.
