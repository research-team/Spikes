import numpy as np
import sklearn.decomposition as decomp


def extract_waveforms(signal, peak_indices, samples_before, samples_after):
    """Return a 2D-array of waveforms for each peak.

    The "samples_after" argument includes the peak.
    """

    # TODO: Merge intersecting waveforms.
    total_samples = samples_before + samples_after
    waveforms = np.zeros((len(peak_indices), total_samples), dtype=int)
    for i, peak_index in enumerate(peak_indices):
        start = peak_index - samples_before
        if start < 0:
            start = 0
        # Slices are right-exclusive
        end = peak_index + samples_after
        if end > len(signal):
            end = len(signal)
        waveforms[i] = signal[start:end]
    return waveforms


def reduce_dimensions(waveforms, ndims, method, **kwargs):
    if method == 'pca':
        algorithm = decomp.PCA(n_components=ndims)
    else:
        raise Exception(
            'Unknown dimensionality reduction method: '.format(method)
        )
    algorithm.set_params(**kwargs)
    algorithm.fit(waveforms)
    return algorithm.transform(waveforms)
