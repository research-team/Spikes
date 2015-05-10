import configparser
import sys

import h5py as hdf

import numpy as np
import matplotlib.pylab as plt
import matplotlib


def trace(channel, begin, end):
    plt.plot(channel['filtered'][int(begin):int(end)], color='b')
    plt.axhline(-channel.attrs['threshold'], color='r')
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
