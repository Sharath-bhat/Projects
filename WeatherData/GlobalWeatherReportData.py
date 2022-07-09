import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

#rread and convert the csv file to dataframe
weather_df = pd.read_csv('fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')

#create a data frame for 2015 weather data, and find the max and min value of temprature
weather_df_2015 = weather_df[weather_df['Date'].str.contains('2015')]
weather_df_2015['Date'] = weather_df_2015.Date.str[5:]
maxtemp_2015 = weather_df_2015.groupby('Date')['Data_Value'].max()
mintemp_2015 = weather_df_2015.groupby('Date')['Data_Value'].min()

#create a data frame for data till 2014, remove leapdays (02-29) and find the max and min temprature 
weather_df_till_2014 = weather_df[weather_df['Date']<='2015']
weather_df_till_2014['Date'] = weather_df_till_2014.Date.str[5:]
weather_df_till_2014 = weather_df_till_2014[weather_df_till_2014['Date']!='02-29']
maxtemp_till_2014 = weather_df_till_2014.groupby('Date')['Data_Value'].max()
mintemp_till_2014 = weather_df_till_2014.groupby('Date')['Data_Value'].min()

#make a list range from 1-365
observation_dates = list(range(1,366))

#devide the x and y into 365 spaces 
x = np.linspace(1,365,365)
y = np.linspace(1,365,365)

#find the broken record high and low tem in 205
record_high_in_2015 = maxtemp_2015[maxtemp_2015 >= maxtemp_till_2014.reindex_like(maxtemp_2015)]
record_low_in_2015 = mintemp_2015[mintemp_2015 <= mintemp_till_2014.reindex_like(mintemp_2015)]
x = [n for n in range(0,365) if (maxtemp_2015.iloc[n] >=maxtemp_till_2014 .iloc[n]) ]
y = [n for n in range(0,365) if (mintemp_2015.iloc[n] <=mintemp_till_2014 .iloc[n]) ]

#plot the fig on a frame of 20x20
plt.figure(figsize=(20,20))
plt.plot(maxtemp_till_2014.values,'-o',mintemp_till_2014.values, '-o' ,zorder=1)

#scratter the points of high record and low on top of plot
plt.scatter(x,record_high_in_2015, s=50, c='r', zorder=2)
plt.scatter(y,record_low_in_2015, s=50, c='green', zorder=2)

#make the x axis ticks as month and paint the inbetween the lines
plt.xticks(range(0, len(maxtemp_till_2014), 30), maxtemp_till_2014.index[range(0, len(maxtemp_till_2014), 30)], rotation=45)
plt.gca().fill_between(observation_dates, maxtemp_till_2014,mintemp_till_2014, facecolor='green', alpha=0.2)

# remove the top and right spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

#name the axis and add legends
plt.xlabel('Day of the Year')
plt.ylabel('Temperature (Tenths of Degrees C)')
plt.title('Global Daily Climate Records')
plt.gca().legend((['record high temperatures', 'record low temperatures','record high broken in 2015','record low broken in 2015']))

plt.savefig('Global_Weather_Data.png')