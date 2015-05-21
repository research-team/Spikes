import configparser
import sys

import h5py as hdf

from spikelab.core.parsers import neuralynx
from spikelab.core import filters, detect, extract, sort


PIPELINE_STAGES = {
    'parse': 0,
    'filter': 1,
    'detect': 2,
    'extract': 3,
    'cluster': 4,
}


def _overwrite_dataset(group, name, data):

    if name in group:
        del group[name]
    return group.create_dataset(name, shape=data.shape, dtype=data.dtype,
            data=data, chunks=True, fletcher32=True)


def full_pipeline(fromstage):
    stagecode = PIPELINE_STAGES[fromstage]

    config = configparser.ConfigParser()
    config.read('config.ini')

    print('Opening')
    f = hdf.File(config['general']['file_name'])
    channel_number = int(config['general']['channel_number'])
    channel = f.require_group('/channels/{}'.format(channel_number))

    if stagecode <= PIPELINE_STAGES['parse']:
        print('Parsing')
        raw = neuralynx.csc(config['general']['raw_data_file'])
        _overwrite_dataset(channel, 'raw', raw)
    else:
        raw = channel['raw']

    if stagecode <= PIPELINE_STAGES['filter']:
        print('Filtering')
        filtered = filters.butterworth(
            raw,
            frequency=int(config['general']['sampling_rate']),
            cutoff_low=float(config['filtering']['cutoff_low']),
            cutoff_high=float(config['filtering']['cutoff_high']),
            order=int(config['filtering']['order']),
        )
        _overwrite_dataset(channel, 'filtered', filtered)
    else:
        filtered = channel['filtered']

    if stagecode <= PIPELINE_STAGES['detect']:
        print('Detecting')
        threshold = detect.median_threshold(
            filtered,
            coeff=float(config['detection']['threshold_coefficient']),
        )
        channel.attrs['threshold'] = threshold
        peaks, waveforms = detect.waveforms(
            filtered,
            threshold,
            samples_before=int(config['detection']['samples_before']),
            samples_after=int(config['detection']['samples_after']),
        )
        _overwrite_dataset(channel, 'peaks', peaks)
        _overwrite_dataset(channel, 'waveforms', waveforms)
    else:
        peaks, waveforms = channel['peaks'], channel['waveforms']

    if stagecode <= PIPELINE_STAGES['extract']:
        nfeatures = int(config['extraction']['nfeatures'])
        if nfeatures == 0:
            nfeatures = None
        print('Extracting')
        features = extract.features(
            waveforms,
            count=nfeatures,
        )
        _overwrite_dataset(channel, 'features', features)
    else:
        features = channel['features']

    if stagecode <= PIPELINE_STAGES['cluster']:
        print('Clustering')
        units = sort.cluster(features, max_units=int(config['clustering']['max_units']), n_iterations=int(config['clustering']['n_iterations']), n_runs=int(config['clustering']['n_runs']))
        _overwrite_dataset(channel, 'units', units)

    print('Closing')
    f.close()


def main():
    fromstage = sys.argv[1] if len(sys.argv) >= 2 else 'parse'
    full_pipeline(fromstage)


if __name__ == '__main__':
    main()
