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
 
#SECTION 2: DATA MANIPULATION
rgr_168 = rgr_raw_data[rgr_raw_data.DAYS_SINCE_ACQUISITION == 168]
referral = rgr_168[rgr_raw_data.ACQUISITION_CHANNEL == "Referral"] 


outliers = []
def detect_outliers(data):
    threshold=3
    mean_1 = np.mean(data)
    std_1 =np.std(data)
    
    
    for y in data:
        z_score= (y - mean_1)/std_1 
        if np.abs(z_score) > threshold:
            outliers.append(y)
    return outliers

print((detect_outliers(referral["HOURS_WORKED_CUMULATIVE"])))
