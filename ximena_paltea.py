# !pip install opencage
#$ pip install streamlit --upgrade

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gdown
import os
from opencage.geocoder import OpenCageGeocode

DataUbigeos = pd.read_csv('https://cloud.minsa.gob.pe/s/GkfcJD8xKHJeCqn/download')
DataUbigeos
