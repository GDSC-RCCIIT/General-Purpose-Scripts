import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence


r = sr.Recognizer()


def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """

    sound = AudioSegment.from_wav(path)

    chunks = split_on_silence(
        sound,
        min_silence_len=500,
        silence_thresh=sound.dBFS - 14,
        keep_silence=500,
    )
    folder_name = "audio-chunks"

    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""

    for i, audio_chunk in enumerate(chunks, start=1):

        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")

        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)

            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                whole_text += text

    return whole_text


print("Select:\n1)Audio file transcription\n2)Speech transcription")
op = input()
tfloc = input(
    "Please input the full path where the you want the text file to be saved:"
)
if op == "1":
    path = input("Please input full path of audio file:")
    text = get_large_audio_transcription(path)
    text_file = open(tfloc, "w")
    text_file.write(text)
    text_file.close()
    print(text)
elif op == "2":
    whole_text = ""
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.record(source, duration=4)
        print("Time over, thanks")

        try:

            print("Text: " + r.recognize_google(audio_text))
            whole_text += audio_text
        except:
            print("Sorry, I did not get that")
    text_file = open(tfloc, "w")
    text_file.write(text)
    text_file.close()
else:
    print("Invalid key")
