# Audio file formats

# .mp3 - lossy 

# .flac - lossless

# .wav (standard)  - uncompressed

import wave

# Audio signal Parameters

# - number of channels 
# - sample width
# - framerate / sample_rate:44,100Hz  no of samples per second
# - number of frames
# - values of a frame


#load our wav file
obj = wave.open("dancer.wav","rb")

# extract parameter
# getters functions

print("Number of channels",obj.getnchannels())
print("Sample Width",obj.getsampwidth())
print("Frame Rate",obj.getframerate())
print("Number of Frames",obj.getnframes())
print("Parameterts",obj.getparams())

#calculate the time of audio
# time in seconds

t_audio = obj.getnframes() / obj.getframerate()
print(round(t_audio))

# get actual frames

frames = obj.readframes(-1)  # -1 will read all rames
print(type(frames) , type(frames[0]))
print(len(frames))

# len of frames is twice as number of framess 
# means 2 bytes per sample 

print(len(frames)/2)

#when you are done reading you should close it
obj.close()

# to save the data 

obj_new = wave.open("divesh.wav" , "wb")
# setter functions

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(44100.0)

obj_new.writeframes(frames)  #duplicating it

obj_new.close()






