# Swarnendu Moitra, January 2023
# MNE Preprocessing Pipeline code, for Queen Mary University of London
# Using MNE v1.3.0


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import mne
import copy, os, sys
import os.path as op

# Raw File
raw_file = '/media/swarmoi/QM-Drive/Dropbox/SAVANT-Personal/QM-EEG/QM-EEG-Protocol/Data/example.bdf'
raw = mne.io.read_raw_bdf(raw_file, preload=False)

events = mne.find_events(raw)