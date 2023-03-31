import wave
import numpy as np
import matplotlib.pyplot as plt


obj = wave.open("divesh.wav","rb")

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)  # sample for each point in time

obj.close()

t_audio = n_samples / sample_freq
print(t_audio)

# since its a byte object we can create numpy array out of it.

signal_array = np.frombuffer(signal_wave, dtype=np.int16)
print(signal_array.shape)

# for stereo:
#l_channel = signal_array[0::2]
#r_channel = signal_array[1::2]


times = np.linspace(0 ,t_audio , num=n_samples)


# plotting 

plt.figure(figsize=(15 ,5))
plt.plot(times , signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal wave")
plt.xlabel("Time (s)")
plt.xlim(0 , t_audio)

plt.show()

