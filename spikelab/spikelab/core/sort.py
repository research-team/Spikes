import sklearn.mixture as mm


def cluster(features):
    """Compute cluster labels for features."""

    gmm = mm.DPGMM()
    gmm.fit(features)
    return gmm.predict(features)
