# Swarnendu Moitra, January 2023
# MNE Preprocessing Pipeline code, for Queen Mary University of London
# Using MNE v1.3.0


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import mne
import copy, os, sys
import os.path as op

# Experiment name

expname = 'GreekEnglish'

# Path to directory
exppath = '/media/swarmoi/QM-Drive/Dropbox/SAVANT-Personal/QM-EEG/QM-EEG-Protocol'

# EEG Data folder
eegpath = exppath + '/Data'
os.chdir(exppath)

### MNE 
root = exppath
#raw_file = eegpath / 'DKTCYD-test.bdf'
raw_file = '/media/swarmoi/QM-Drive/Dropbox/SAVANT-Personal/QM-EEG/QM-EEG-Protocol/Data/DKTCYD-test.bdf'
raw = mne.io.read_raw_bdf(raw_file, preload=False)

#events_file = root / 'sample_audvis_filt-0-40_raw-eve.fif'
events = mne.read_events(events_file)

raw.crop(tmax=90)  # in seconds (happens in-place)
# discard events >90 seconds (not strictly necessary, but avoids some warnings)
#events = events[events[:, 0] <= raw.last_samp]

print("m")
