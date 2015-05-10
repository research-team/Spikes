import numpy as np


def stddev_threshold(signal, coeff):
    """Find the threshold based on a standard deviation of the signal."""

    return coeff * np.std(np.abs(signal))


def median_threshold(signal, coeff=4):
    """Find the median-based threshold.

    Baseline threshold is calculated by the method described in
    Quiroga, R., Nadasdy, Z., & Ben-Shaul, Y. (2004).
    Unsupervised spike detection and sorting with wavelets
    and superparamagnetic clustering.
    Neural computation, 16(8), 1661-1687.
    """

    return coeff * np.median(np.abs(signal) / 0.6745)


def waveforms(signal, threshold, samples_before, samples_after):
    """Extract spike waveforms from the signal, together with their indices.

    Detection is performed on negative potential.
    Overlapping spikes are ignored, as well as ones that are too close
    to begin/end of the signal.
    """

    # Signal indices where samples are greater than the threshold.
    above_threshold = np.where(signal < -threshold)[0]
    # Indices of above_threshold where consecutive blocks of indices break.
    above_threshold_breaks = np.where(np.ediff1d(above_threshold) > 1)[0] + 1
    # Groups of indices where samples are greater than the threshold.
    # Each group is corresponding to a single spike.
    regions = np.split(above_threshold, above_threshold_breaks)
    # Find all available peaks.
    peaks = []
    last_peak = None
    samples_total = samples_before + samples_after
    for region in regions:
        start = region[0]
        end = region[-1] + 1
        peak = start + np.argmin(signal[start:end])
        # Ignore spikes which are out of signal bounds.
        if (peak < samples_before) or (peak > len(signal) - samples_after):
            last_peak = peak
            continue
        # Ignore overlapping spikes.
        if last_peak and (peak - last_peak < samples_total):
            # Remove last peak if it has been remembered.
            if peaks[-1] == last_peak:
                peaks.pop()
            last_peak = peak
            continue
        peaks.append(peak)
    peaks = np.array(peaks)
    # Extract waveforms at valid spike peaks.
    waves = np.zeros((len(peaks), samples_total))
    for i, peak in enumerate(peaks):
        waves[i] = signal[peak-samples_before:peak+samples_after]
    return peaks, waves
