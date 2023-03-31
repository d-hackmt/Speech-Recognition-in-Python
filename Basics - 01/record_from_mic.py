from re import T
import wave
import pyaudio
# PyAudio is a Python library that 
# provides an interface to work with audio in real-time.


FRAMES_PER_BUFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

p = pyaudio.PyAudio()
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFER     
)

print("start recording")

seconds = 5
frames = []
for i in range(0,int(RATE/FRAMES_PER_BUFER*seconds)):
    data = stream.read(FRAMES_PER_BUFER)
    frames.append(data)
    
stream.stop_stream()
stream.close()
p.terminate()

# saving the file

obj_new = wave.open("output.wav" , "wb")
obj_new.setnchannels(CHANNELS)
obj_new.setsampwidth(p.get_sample_size(FORMAT))
obj_new.setframerate(RATE)
obj_new.writeframes(b"".join(frames))  # Making it
obj_new.close()


