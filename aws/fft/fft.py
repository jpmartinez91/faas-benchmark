import numpy as np
from numpy.fft import fft, fftfreq


def run(samples, rate):
    # Generar arreglo de numeros generados al azar
    points = np.linspace(0, 1.0, samples)
    # Generar señal partiendo del arreglo anterios
    signal = np.sin(40 * 2 * np.pi * points) + 0.5 * \
        np.sin(90 * 2 * np.pi * points)
    # Obtner la tranformada de Fourier
    fourier = fft(signal)
    # Obtener las frecuencias de la Transformada de Fourier.
    frequency = fftfreq(signal.size, rate)
    return frequency, fourier
