import numpy as np
from numpy.fft import fft, fftfreq
# The Fourier transform is commonly used to convert a signal in the time spectrum to a frequency spectrum. (time spectra are sound waves, electricity, mechanical vibrations et)

# This is where the Fourier Transform comes in. This method makes use of te fact that every non-linear function can be represented as a sum of (infinite) sine waves


def run(samples, rate):
    points = np.linspace(0, 1.0, samples)
    signal = np.sin(40 * 2 * np.pi * points) + 0.5 * \
        np.sin(90 * 2 * np.pi * points)
    fourier = fft(signal)
    frequency = fftfreq(signal.size, rate)
    return frequency, fourier
