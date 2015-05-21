import configparser
import math
import sys

import h5py as hdf

import numpy as np
import matplotlib.pylab as plt
import matplotlib
import seaborn as sns
import pandas as pd


def trace(channel, begin, end):
    plt.plot(channel['filtered'][int(begin):int(end)], color='b')
    plt.axhline(-channel.attrs['threshold'], color='r')
    plt.show()


def clusters(channel):
    features = channel['features']
    units = channel['units']
    unit_count = len(np.bincount(units))
    fig, subplots = plt.subplots(2, 2)
    for unit, color in zip(range(unit_count), matplotlib.colors.cnames.keys()):
        unit_points = np.take(features, np.where(units.value == unit), axis=0)[0]
        for i in range(3):
            subplots[i // 2, i % 2].scatter(unit_points[:, i], unit_points[:, (i + 1) % 3], color=color)
    plt.show()


def spikes(channel):
    waveforms = channel['waveforms']
    units = channel['units']
    unit_count = len(np.bincount(units))
    fig, subplots = plt.subplots(3, math.ceil(unit_count / 3))
    for unit, color in zip(range(unit_count), matplotlib.colors.cnames.keys()):
        wf = np.take(waveforms, np.where(units.value == unit), axis=0)[0]
        sp = subplots[unit // 3, unit % math.ceil(unit_count / 3)]
        sns.tsplot(wf, ax=sp, err_style='unit_traces')
    plt.show()


def main():
    matplotlib.style.use('ggplot')
    config = configparser.ConfigParser()
    config.read('config.ini')
    experiment = hdf.File(config['general']['file_name'], 'r')
    channel_number = config['general']['channel_number']
    channel = experiment['/channels/{}'.format(channel_number)]
    cmd = sys.argv[1] if len(sys.argv) >= 2 else 'trace'
    func = globals()[cmd]
    func(channel, *sys.argv[2:])


if __name__ == '__main__':
    main()
