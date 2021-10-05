import os
import matplotlib.pyplot as plot
import numpy as np
from scipy.io import wavfile

audio_path = input("Enter : Path of the audio file\n>> ")
Path_Exist = os.path.isfile(audio_path)
if Path_Exist == False:
    print("Wrong Path Input")
    quit()
samplingFrequency, signalData = wavfile.read(audio_path, "r")
# due to most files being stereo-> 2 channels -> L : R
# we split stereo into mono L || R
p = signalData[:, 0]  # selection b/w 0 & 1 -> L : R channel
plot.subplot(211)
plot.title("Spectrogram of a wav file")
plot.plot(signalData)
plot.xlabel("Sample")
plot.ylabel("Amplitude")
plot.subplot(212)
plot.specgram(p, Fs=samplingFrequency)
plot.xlabel("Time")
plot.ylabel("Frequency")
plot.show()
