"""Fourier_transform_createtwosinewave.py
learn from (1) https://pythontic.com/visualization/signals/fouriertransform_fft
(2) https://www.ritchievink.com/blog/2017/04/23/understanding-the-fourier-transform-by-example/
(3) demo of Fourier_transform https://charlesliuyx.github.io/2018/02/18/%E3%80%90%E7%9B%B4%E8%A7%82%E8%AF%A6%E8%A7%A3%E3%80%91%E8%AE%A9%E4%BD%A0%E6%B0%B8%E8%BF%9C%E5%BF%98%E4%B8%8D%E4%BA%86%E7%9A%84%E5%82%85%E9%87%8C%E5%8F%B6%E5%8F%98%E6%8D%A2%E8%A7%A3%E6%9E%90/#%E5%82%85%E7%AB%8B%E5%8F%B6%E5%8F%98%E6%8D%A2
"""
import numpy as np
import matplotlib.pyplot as plotter

samplingFrequency = 100;
samplingInterval = 1 / samplingFrequency;
beginTime = 0;
endTime = 10;
signal1Frequency = 4;
signal2Frequency = 7;
time = np.arange(beginTime, endTime, samplingInterval);

# Create two sine waves
amplitude1 = np.sin(2 * np.pi * signal1Frequency * time)
amplitude2 = np.sin(2 * np.pi * signal2Frequency * time)

# Create subplot
figure, axis = plotter.subplots(4, 1)
plotter.subplots_adjust(hspace=1)

# Time domain representation for sine wave 1
axis[0].set_title('Sine wave with a frequency of 4 Hz')
axis[0].plot(time, amplitude1)
axis[0].set_xlabel('Time')
axis[0].set_ylabel('Amplitude')

# Time domain representation for sine wave 2
axis[1].set_title('Sine wave with a frequency of 7 Hz')
axis[1].plot(time, amplitude2)
axis[1].set_xlabel('Time')
axis[1].set_ylabel('Amplitude')

# Add the sine waves
amplitude = amplitude1 + amplitude2

# Time domain representation of the resultant sine wave
axis[2].set_title('Sine wave with multiple frequencies')
axis[2].plot(time, amplitude)
axis[2].set_xlabel('Time')
axis[2].set_ylabel('Amplitude')

# Frequency domain representation
fourierTransform = np.fft.fft(amplitude) / len(amplitude)  # Normalize amplitude
fourierTransform = fourierTransform[range(int(len(amplitude) / 2))]  # Exclude sampling frequency
tpCount = len(amplitude)
values = np.arange(int(tpCount / 2))
timePeriod = tpCount / samplingFrequency
frequencies = values / timePeriod

# Frequency domain representation
axis[3].set_title('Fourier transform depicting the frequency components')
axis[3].plot(frequencies, abs(fourierTransform))
axis[3].set_xlabel('Frequency')
axis[3].set_ylabel('Amplitude')
plotter.show()
