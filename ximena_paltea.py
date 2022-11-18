# !pip install opencage
# https://opencagedata.com/tutorials/geocode-in-python
#$ pip install streamlit --upgrade

import streamlit as st
import pandas as pd
import numpy as np
from opencage.geocoder import OpenCageGeocode

DataUbigeos = pd.read_csv('ubigeos-completos.csv')
DataUbigeos
