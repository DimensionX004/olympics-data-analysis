# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path
data = pd.read_csv(path)
#Code starts here

# Data Loading 
data.rename({"Total" : "Total_Medals"}, axis = 1, inplace = True)

# Summer or Winter
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', 'Winter')
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'], 'Both', data['Better_Event'])
#data.head(5)
x = data['Better_Event'].value_counts()
print(x)
better_event = x.index[0]
print(better_event)

# Top 10
def top_ten(df, col):
    #country_list = []
    country_list = df.nlargest(10, col)
    #country_list = df.iloc[:,1]
    country_list = list(country_list['Country_Name'])
    print(country_list)
    return country_list

top_countries = data[['Country_Name', 'Total_Summer', 'Total_Winter', 'Total_Medals']].copy()
print(top_countries.head(3))
print(top_countries.shape)
top_countries = top_countries.head(-1)
print(top_countries.shape)
top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')
common = []
common = [x for x in top_10_summer if x in top_10_winter]
common = [x for x in common if x in top_10]
print(common)

# Plotting top 10
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
#summer_df.plot(kind = 'bar')
figure, (ax_1, ax_2, ax_3) = plt.subplots(1, 3, figsize = (20,4))
ax_1.bar(summer_df['Country_Name'], summer_df['Total_Summer'], color = 'b')
ax_1.set_xlabel('Country Name')
ax_1.set_ylabel('Medals')
#ax_1.set_xticks(rotation = 45)

ax_2.bar(summer_df['Country_Name'], summer_df['Total_Winter'], color = 'g')
ax_2.set_xlabel('Country Name')
#ax_2.set_xticks(rotation = 45)

ax_3.bar(summer_df['Country_Name'], summer_df['Total_Medals'], color = 'r')
ax_3.set_xlabel('Country Name')
figure.autofmt_xdate(rotation = 45)
plt.tight_layout()

# Top Performing Countries
summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
id1 = summer_df.iloc[:, -1].idxmax()
summer_max_ratio = summer_df["Golden_Ratio"][id1]
summer_country_gold = summer_df["Country_Name"][id1]

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
id2 = winter_df.iloc[:, -1].idxmax()
winter_max_ratio = winter_df["Golden_Ratio"][id2]
winter_country_gold = winter_df["Country_Name"][id2]

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
id3 = top_df.iloc[:, -1].idxmax()
top_max_ratio = top_df["Golden_Ratio"][id3]
top_country_gold = top_df["Country_Name"][id3]

# Best in the world 
data_1 = data.head(-1)
data_1['Total_Points'] = 3*data_1['Gold_Total'] + 2*data_1['Silver_Total'] + data_1['Bronze_Total']
id4 = data_1['Total_Points'].idxmax()
print(id4)
most_points = data_1['Total_Points'][id4]
best_country = data_1['Country_Name'][id4]
print("The best Country is", best_country, " having", most_points, " points.")

# Plotting the best
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total', 'Silver_Total', 'Bronze_Total']]
print(best)
best.plot(kind = 'bar', stacked =True)


