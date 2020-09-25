"""numpy_matplotlib_dot_pyplotasplt_scipy_dot_io_dot_wavfile.py
. NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
. Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It (plt) provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK+.
. scipy.io.wavfileaswf
"""
import matplotlib.pyplot as plt
import numpy as np
from os.path import dirname, join as pjoin
from scipy.io import wavfile
import scipy.io
import os

#data_dir = pjoin(dirname(scipy.io.__file__),'myworkspace_py','')
data_dir = pjoin(os.sep,'myworkspace_py')
wav_fname = pjoin(data_dir, 'Alesis-Fusion-Acoustic-Bass-C2.wav')
#wav_fname = 'Alesis-Fusion-Acoustic-Bass-C2.wav'
samplerate, data = wavfile.read(wav_fname)
print(f"number of channels = {data.shape[1]}")
length = data.shape[0] / samplerate
print(f"length = {length}second(s)")
time = np.linspace(0., length, data.shape[0])
plt.plot(time, data[:, 0], label="Left channel")
plt.plot(time, data[:, 1], label="Right channel")
plt.legend()
plt.xlabel("Time [seconds]")
plt.ylabel("Amplitude")
plt.show()


"""arr = np.array([1,2,3,4,5,6,7,8,9])
print("This array = ",arr, " with the type of ", type(arr),"!")"""

"""np.random.seed(19980801)
data = np.random.randn(2, 100)

fig,axs = plt.subplots(2, 2, figsize=(5,5))
axs[0,0].hist(data[0])
axs[1,0].scatter(data[0], data[1])
axs[0,1].plot(data[0], data[1])
axs[1,1].hist2d(data[0], data[1])

plt.show()"""