#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 21:23:39 2018

@author: byron8899
"""
import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt


'''https://stackoverflow.com/questions/35106179/
how-to-get-iterate-a-date-time-list-to-get-year'''
dateparse = lambda x: datetime.strptime(x, '%Y-%m-%d')

'''Reads the csv file of sitka_weather_07_2014.csv'''
df = pd.read_csv('sitka_weather_2014.csv', parse_dates=['AKST'],
                       date_parser = dateparse)
df.info()
df.describe()

# Plotting Graph
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(df['AKST'],df['Max TemperatureF'], c='red')

# Format plot
plt.title('Daily high temperatures - 2014', fontsize =24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize = 16)
plt.tick_params(axis ='both', which = 'major', labelsize = 16)

plt.show()
