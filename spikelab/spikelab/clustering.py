import numpy as np
import sklearn.cluster as clus


def cluster(waveforms, method, **kwargs):
    """Clsuters the waveforms using the specified method.
    """

    if method == 'kmeans':
        algorithm = clus.KMeans()
    else:
        raise Exception('Unknown clustering method: {}'.format(method))
    algorithm.set_params(**kwargs)
    algorithm.fit(waveforms)
    return algorithm.labels_
