import matplotlib.pyplot as plt
from math import sqrt
import matplotlib.transforms as transforms
import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])

#traspose the dataframe for easy change
df_t = df.transpose(copy=True)

#get mean and standrt deviation for the columns (1992-95)
mean = df_t.describe().mean().values
std = df_t.describe().std()

# print(mean)

# formula for confidence interval over a mean value is ± z* σ/√n, z=1.96 for the confidence of 95%
z= 1.96 
confid_int = z*(std.values/sqrt(len(df_t.index)))
# print(confid_int)

#get the value form the user 
Y = int(input('Please Enter a Y value:'))

#define the color of the graph as per the Y and meanvalues
def colorbar(Y,mean, confid_int):
    if (Y<(mean+confid_int)) and (Y>(mean-confid_int)):
        return 'white'
    elif Y<(mean+confid_int):
        return 'red'
    else:
        return 'blue'

bar_color=[colorbar(Y,mean[i],confid_int[i]) for i in range(len(mean))]

# print(f'color{bar_color}')


fig, ax = plt.subplots()

#the line x=0 and the y=Y line (hotizontal to x axis)
ax.axhline(Y, color='green', ls='--')
trans = transforms.blended_transform_factory(ax.get_yticklabels()[0].get_transform(), ax.transData)
ax.text(0,Y, f"{Y}", color="green", transform=trans, 
        ha="right", va="center")

#plot the graph with yerr= confidence interval
plt.bar(range(df.shape[0]),mean, width=0.5, color=bar_color, align='center', yerr=confid_int)

#add title and make the visualization more readable.
plt.title("CI of noraml population distribution since 1992-95")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.xticks(np.arange(len(df.index)), df.index)
ax.set_facecolor('lightgray')

plt.show()