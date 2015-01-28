# Review of open-source neuroscience software

## General-purpose libraries and frameworks

### BioSig

Publication: [BioSig: The Free and Open Source Software Library for Biomedical Signal Processing](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3061298/)

Homepage: http://biosig.sourceforge.net

* A biomedical signal processing library with very broad applicability.
* Includes C/C++ librares, toolboxes for Octave/MATLAB, Python bindings and also and other components not relevant to this project.
* Not well suited for the neuroscience in particular.
* Poorly documented, supports neither Axon Binary File (.abf) nor Neuralynx (.ncs) data formats.

### Neo

Publication: [Neo: an object model for handling electrophysiology data in multiple formats](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3930095/)

Homepage: http://neuralensemble.org/neo

* A language-independent, simple object model for representing electrophysiological data
* Does not have any built-in analysis functionality by design
* Has a Python implementation which supports many data formats
* For the neuroscience problem domain, the model is both simple, accurate and non-restrictive
* Documentation quality is good
* Performance is expected to be sufficient, due to NumPy with ATLAS/LINPACK

It is promising to design and implement a data analysis framework on the top of Neo for [common spike sorting pipeline](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3314330/figure/F1/).
This framework can be used to experiment with different algorithms for different pipeline stages.
Finally, it can be integrated with GUI data viewers built on top of Neo.

## Graphical user interface tools

### SigViewer

Homepage: http://sigviewer.sourceforge.net

* Biosignal viewer based on the BioSig library.

For our purposes, it has the same disadvantages as the BioSig library.

### Stimfit

Publication: [Stimfit: quantifying electrophysiological data with Python](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3931263/)

Homepage: http://stimfit.org

* Old, stable software
* Has very unintuitive interface
* Has an interactive Python console

### SpykeViewer

Publication: [Spyke Viewer: a flexible and extensible platform for electrophysiological data analysis](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3822898/)

Homepage: http://spyke-viewer.g-node.org

* Based on the Neo library
* Has a plugin system and an interactive console
* Very good GUI tool considering the Neo backend.
* GUI is not intuitive and reflects the underlying system architecture rather than providing easy-to-use interface for neuroscientists.

The best general-purpose viewer considering usage of the Neo model.

### OpenElectrophy

Publication: [OpenElectrophy: An Electrophysiological Data- and Analysis-Sharing Framework](www.ncbi.nlm.nih.gov/pmc/articles/PMC2694696/)

Homepage: http://neuralensemble.org/OpenElectrophy

* Based on the Neo library
* Has graphs in time and frequency domain
* Targets to storing electrophysiogical data in the database, managing collections of data

Not very useful as a tool for continious usage.

### Klusters, NeuroScope and NDManager

Publication: [Klusters, NeuroScope, NDManager: a free software suite for neurophysiological data processing and visualization](http://www.ncbi.nlm.nih.gov/pubmed/16580733) *no full-text article*

Homepage: http://neurosuite.sourceforge.net

* Tools for data management, visualisation and clustering.

Looks quite good on screenshots, but doesn't support required data formats.

### KlustaKwik, KlustaViewa and SpikeDetekt

Publication: [High-dimensional cluster analysis with the Masked EM Algorithm](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4298163/)

Homepage: http://klusta-team.github.io

* Tools for spike detection, automatic batch clustering and refining clusters manually.

Looks very good, but tailored to a specific data format and workflow.

## Spike sorting libraries and frameworks

### SpikePy

Homepage: https://code.google.com/p/spikepy

A framework for spike sorting.

* Has a GUI
* Doesn't support required data formats
* Poorly documented

It can be used as an example for building our own pipeline.

### SpikeSort

Homepage: http://spikesort.org

Another framework for spike sorting.

* Documentation is good
* Doesn't support required data formats
* Implements several clutering methods
* Has limited visualisation functionality, but main work is done through the Python console

The best library for rapid prototyping and experimentation, assuming confidence with Python.

### Caton

Homepage: https://code.google.com/p/caton

Yet another spike sorting library.

* Intended to work with KlustaKwik
* Doesn't support required data formats

Worth looking to the source code.
