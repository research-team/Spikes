import numpy as np


def csc(filename):
    """Read Neuralynx continuously sampled channel (CSC) recorded data.
    """

    with open(filename, 'rb') as f:
        # Skip the header (first 16KB), because it contains unspecified
        # text, for informational purposes only.
        f.seek(16384)
        # The rest of the file contains a sequence of chunks.
        chunks = list(_csc_chunks(f))
    # Convert chunk into a single fixed-length array of samples.
    samples = np.concatenate(chunks)
    return samples


def _csc_chunks(f):
    """Generator that returns a sequence of payloads for the file stream.
    """

    while True:
        # The first 20 bytes of the chunk contain metadata, which is not
        # needed.
        metadata = f.read(20)
        # Stop the generator if end of file is reached.
        if len(metadata) != 20:
            raise StopIteration
        # Read the payload: 512 elements of 16-bit signed little-endian
        # integers.
        raw_payload = f.read(1024)
        # Convert payload into array.
        payload = np.frombuffer(raw_payload, dtype=np.dtype('<i2'))
        yield payload
