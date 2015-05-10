import sklearn.decomposition as decomp


def features(waveforms, count=None):
    return decomp.PCA(n_components=count).fit_transform(waveforms)
