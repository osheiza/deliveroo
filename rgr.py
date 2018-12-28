#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:15:54 2018

@author: osheizaotori
"""

#Import appropriate packages for analysis
import os 
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#Load data into dataframe
os.chdir('/Users/osheizaotori/Desktop/Jobs/Deliveroo/deliveroo')
rgr_raw_data = pd.read_csv('rgr_data_test-2 (1).csv')

#SECTION 1: Exploratory Data Analysis
print(rgr_raw_data.head())
print(rgr_raw_data.tail())
print(rgr_raw_data.describe())
print(pd.unique(rgr_raw_data['ACQUISITION_CHANNEL']))
print(len(pd.unique(rgr_raw_data['RIDER_ID']))) #Current fleet
## Rider 67787 is an outlier




