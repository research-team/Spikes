import scipy.signal as sig


def butterworth(signal, frequency, cutoff_low, cutoff_high, order):
    """Applies the Butterworth filter to the signal.
    """
    nyquist_freq = frequency / 2
    band = [cutoff_low / nyquist_freq, cutoff_high / nyquist_freq]
    b, a = sig.butter(order, band, btype='bandpass')
    return sig.filtfilt(b, a, signal)
