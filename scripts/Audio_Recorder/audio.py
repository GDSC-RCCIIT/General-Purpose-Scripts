import time
import sounddevice as sd
import wavio as wv

# Sampling frequency
freq = 45000

# Recording duration
duration = int(input("Enter the duration (in seconds): "))

print("Recording...")
# Start recorder with the given values of duration and sample frequency
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

# View timer and record audio for the given number of seconds
while duration:
    mins, secs = divmod(duration, 60)
    timer = "{:02d}:{:02d}".format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    duration -= 1

print("Done!")
num = input("Enter a number for your file name: ")

# Convert the NumPy array to audio file
wv.write("recording" + num + ".wav", recording, freq, sampwidth=2)

print("Saved file as recording" + num + ".wav in the present directory.")
