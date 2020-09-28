# SA2RAGE_processing
SA2RAGE / B1 map

SA2RAGE processing for data collected with Bruker MRI instrument (with Paravision) SA2RAGE is a MRI experiment originally developped by F. Eggenschwiler et al, which allows to map the transmit magnetic field B_1^+ at every location (limited by the resolution of the experimental data):

Florent Eggenschwiler et al., Magnetic Resonance in Medicine 67:1609–1619 (2012), https://onlinelibrary.wiley.com/doi/full/10.1002/mrm.23145 // Further expanded in J.P. Marques and R. Gruetter, https://doi.org/10.1371/journal.pone.0069294.

I developped a Bruker method to run with Paravision 6 and the associated software written as a mixture of C program and python scripts to analyze the data. The processing software requires only to have access to the "method" file of the expreriment and the 2dseq file obtained from a complex Fourier transform of the aquired fid data.
