"""create1kHZ_sampledat44100HZ_16bitPCMMono.py
Create a 1000HZ sine(正弦) wave, sampled at 44100HZ. Write to 32-bit PCM(Pulse Code Modulation), Mono(single stereo channel that needs 2 bytes)
"""
import scipy as sp
import numpy as np
from scipy.io.wavfile import write

fS = 1000
dt = np.dtype(np.int32)
#sig = np.fromfile('Alesis-Fusion-Acoustic-Bass-C2.wav', dtype=dt, count=-1, sep='')
sig = np.fromfile('file_example_WAV_10MG.wav', dtype=dt, count=-1, sep='')
m = np.max(np.abs(sig))
sigf32 = (sig/m).astype(np.float32)
sp.io.wavfile.write('sound.wav', int(fS), sigf32)
