import pandas as pd
import  numpy as np
import seaborn as sns
import folium
from matplotlib import pyplot as plt

df = pd.read_csv('2013-10 - Citi Bike trip data.csv')
# What is this datat about?

#print(df.head)
# print(df.describe())
# print(df.info)

#sns.histplot(df['tripduration'])
#print(sns.pairplot(df))
print(sns.pairplot(df[['tripduration', 'gender']]))

num_suscriber = df['usertype'].loc[df['usertype'] == 'Subscriber'].count()

#count total number of rows
total = len(df)

#calculate %, which devide to number of subscribers devide to total numbers of users

#print(round(num_suscriber/total*100,2), '% of totla riders on October 1')

# 1 Q - How does the duration of the trip depend on the starting time?
# starttime


df['hour'] = df.starttime.apply(lambda  x:x[11:13]).astype('str')
#print(df.starttime.apply(lambda  x:x[11:13]).astype('str'))

#visualisation
sns.scatterplot(x='hour', y='tripduration', data = df, hue ='usertype')
#plt.show()

# 2 Q - Which bike station is the most popular for starting a trip?

df2 = df.groupby(['start station id']).size().reset_index(name='counts')
temp = df.drop_duplicates('start station id')
# left join
pd.merge(df2, temp[['start station id', 'start station name', 'start station latitude', 'start station longitude']], how = 'left', on = ['start station id'])

#initilaze a map
m = folium.Map(location=[40.691966, -73.981302], title = 'OpenStreetMap', zoom_start=12)
#print(m)

#add points to map
for i in range(0, len(df2)):
    folium.Circle(
        location=[df.iloc[i]['start station latitude'], df.iloc[i]['start station longitude']],
        popup=df2.iloc[i]['start station name'],
        radius = float(df2.iloc[i]['counts'])/2,
        color = 'r',
        fill = True, fill_color  = 'red'
    ).add_to(m)
print(m)
plt.show()
