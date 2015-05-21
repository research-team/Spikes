import numpy as np
from sklearn import mixture

def cluster(features, max_units, n_iterations, n_runs):
    """Compute cluster labels for features."""

    best_score = float('inf')
    for n_units in range(2, max_units + 1):
        for cov_type in 'spherical', 'tied', 'diag', 'full':
            gmm = mixture.GMM(n_components=n_units, covariance_type=cov_type, n_iter=n_iterations, n_init=n_runs)
            gmm.fit(features)
            labels = gmm.predict(features)
            labels_count = len(np.bincount(labels))
            logstring = 'n_units: {}, cov_type: {}'.format(n_units, cov_type)
            if not gmm.converged_:
                print('NOT CONVERGED', logstring)
                continue
            if labels_count < 2:
                print('SINGLE CLUSTER', logstring)
                continue
            print('Computing score', logstring)
            score = gmm.bic(features)
            print('score: {}'.format(score), logstring)
            if score < best_score:
                best_score = score
                best_cov_type = cov_type
                best_labels = labels
                best_n_units = n_units
    print('The best score for n_units = {}, cov_type = {}: {}'.format(best_n_units, best_cov_type, best_score))
    return best_labels
