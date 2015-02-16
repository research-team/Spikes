# Software Usage

## Klusta Sute

1. Download [the Python converter script and the shell wrapper](ncs2dat) and place them to the directory with NCS files
2. Download [the probe file and the configuration file](klustakwik-input) and place them to the directory with NCS files
3. Run the shell wrapper script (it may take approximately 5 minutes to convert the data)
4. Run spike detection and clustering: `klusta experiment.prm`
5. Launch KlustaViewa: `klustaviewa experiment.kwik`

### Notes

1. When using the `klusta` tool, use `--overwrite` option to overwrite previously generated files
2. You might want to save log file from the KlustaKwik output; use `klusta experiment.dat | tee log.txt`
