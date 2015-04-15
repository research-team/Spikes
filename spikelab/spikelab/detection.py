import numpy as np


def find_threshold(signal, coeff):
    # threshold = np.std(np.abs(signal)) * coeff
    # Baseline threshold is calculated by the method described in
    # Quiroga, R., Nadasdy, Z., & Ben-Shaul, Y. (2004).
    # Unsupervised spike detection and sorting with wavelets
    # and superparamagnetic clustering.
    # Neural computation, 16(8), 1661-1687.
    threshold = np.median(np.abs(signal) / 0.6745) * coeff
    return threshold


def find_peak_indices(signal, threshold):
    # Indices where samples are greater than the threshold.
    spike_indices = np.nonzero(signal > threshold)[0]
    # Indices of spike_indices array where consecutive (increasing by 1)
    # blocks of indices break.
    spike_indices_breaks = np.where(np.diff(spike_indices) != 1)[0] + 1
    # Groups of indices where samples are greater than the threshold.
    # Each group is corresponding to a single spike.
    spike_regions = np.split(spike_indices, spike_indices_breaks)
    # Find peak indices.
    peak_indices = np.zeros(len(spike_regions), dtype=int)
    for i, region in enumerate(spike_regions):
        start = region[0]
        end = region[-1]
        region_values = signal[start : (end+1)]
        peak_indices[i] = start + np.argmax(region_values)
    return peak_indices
