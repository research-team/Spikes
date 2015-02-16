# KlustaKwik Installation and Usage

## Installation

1. https://github.com/klusta-team/example/blob/master/install.md#all-systems-linux-mac-os-x-and-windows
2. https://github.com/klusta-team/example/blob/master/README.md#linux-and-mac-os-x (steps 2 and 3)
3. Download KlustaKwik exacutable source (either by cloning or by downloading the ZIP archive) from https://github.com/klusta-team/klustakwik
4. Run `make` from the cloned reposutory or unpacked source
5. Copy the `KlustaKwik` executable to your `PATH`, renaming it to `klustakwik` (in lower case)

### Notes

1. You don't need the example data (`klustakwik-example.zip`)
2. Double-check your Python executable: `which python` should point to the Miniconda distribution

## Usage

1. Run spike detection and clustering: `klusta experiment.prm` (probe and data files should be in the same directory)
2. Launch KlustaViewa: `klustaviewa experiment.kwik`

### Notes

4. When using the `klusta` tool, use `--overwrite` option to overwrite previously generated files
3. You might want to save log file from the KlustaKwik output; use `klusta experiment.dat | tee log.txt`
