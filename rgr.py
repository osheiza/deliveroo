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
os.chdir('/Users/osheizaotori/Desktop/Jobs/Deliveroo/Final Project')
rgr_raw_data = pd.read_csv('rgr_data_test-2 (1).csv')

#Exploratory Data Analysis
print(rgr_raw_data.head())
print(np.median)

#Separate into acquisition channels
referral = rgr_raw_data[rgr_raw_data.ACQUISITION_CHANNEL == 'Referral']
digital = rgr_raw_data[rgr_raw_data.ACQUISITION_CHANNEL == 'Digital']
organic = rgr_raw_data[rgr_raw_data.ACQUISITION_CHANNEL == 'Organic']
job_platforms = rgr_raw_data[rgr_raw_data.ACQUISITION_CHANNEL == 'Job Platforms']
offline = rgr_raw_data[rgr_raw_data.ACQUISITION_CHANNEL == 'Offline']
unknown = rgr_raw_data[rgr_raw_data.ACQUISITION_CHANNEL == 'Unknown']


#Pie Chart


#Plots of metrics to consider
#Mean throughput by days of acquistion
mean_by_days_since_acq = referral.groupby('DAYS_SINCE_ACQUISITION')['THROUGHPUT_CUMULATIVE'].mean()
organic_by_days_since_acq = organic.groupby('DAYS_SINCE_ACQUISITION')['THROUGHPUT_CUMULATIVE'].mean()
ax = mean_by_days_since_acq.plot(x='DAYS_SINCE_ACQUISITION', y='THROUGHPUT_CUMULATIVE', label='Referrals')
organic_by_days_since_acq.plot(x='DAYS_SINCE_ACQUISITION', y='THROUGHPUT_CUMULATIVE', label='Organic', ax=ax)
ax.set_ylabel('Orders/Hours')
