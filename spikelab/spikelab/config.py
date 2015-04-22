import configparser


# Default configuration options.
# Should be kept in sync with the reference configuration file.
DEFAULT = {

    'general': {
        'log_level': 'info',
        'log_file': 'spikelab.log',
    },

    'data': {
        'format': None,
        'voltage_gain': 1.0,
    },

    'filtering': {
        'method': 'butterworth',
        'butterworth_order': 5,
        'bandpass_low_frequency': None,
        'bandpass_high_frequency': None,
    },

    'detection': {
        'spike_sign': 'negative',
        'threshold_coefficient': 3.0,
    },

    'extraction': {
        'samples_before_peak': 16,
        'samples_after_peak': 16,
        'feature_count': 0,
    },

    'clustering': {
        'method': 'em',
    }

}


def read(filename):
    config = configparser.ConfigParser(
        defaults=DEFAULT,
        empty_lines_in_values=False,
        interpolation=configparser.ExtendedInterpolation(),
    )
    config.read(filename)
    return config
