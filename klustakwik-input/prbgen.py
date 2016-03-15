#!/usr/bin/env python


"""Generate the probe file.
"""


from __future__ import print_function


from itertools import combinations
from pprint import PrettyPrinter


PRB_FILE_NAME = 'experiment.prb'
CHANNEL_GROUPS_COUNT = 4
CHANNELS_IN_GROUP = 4


def main():
    channel_groups = {}
    for i in range(CHANNEL_GROUPS_COUNT):
        start = CHANNELS_IN_GROUP * i
        end = start + CHANNELS_IN_GROUP
        channels = list(range(start, end))
        channel_groups[i] = {
            'channels': channels,
            'graph': list(combinations(channels, 2)),
        }
    with open(PRB_FILE_NAME, 'w') as f:
        f.write('channel_groups = \\\n')
        PrettyPrinter(stream=f).pprint(channel_groups)


if __name__ == '__main__':
    main()
