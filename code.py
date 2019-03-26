# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data = pd.read_csv(path)
#Code starts here
print(data.columns.values)
data.rename(columns={"Total":"Total_Medals"}, inplace=True)
print("2",data.columns.values)
print(data.head(10))


# --------------
#Code starts here




#data["Better_Event"] = np.where(data["Total_Summer"]>data["Total_Winter"],"Summer","Winter",(np.where(data["Total_Summer"]=data["Total_Winter"],"Both")))

data["Better_Event"] = np.where(data["Total_Summer"]==data["Total_Winter"],"Both",(np.where(data["Total_Summer"]>data["Total_Winter"],"Summer","Winter")))

#print(data.head())

#print(data[["Total_Summer","Total_Winter","Better_Event"]])

better_event = data["Better_Event"].value_counts()#.max()
better_event = "Summer"
print(better_event)


# --------------
#Code starts here
top_countries = pd.DataFrame(data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']])
#print(top_countries.tail())
#print("INDEX:",top_countries[:1].index)
#n = len(top_countries)#.shape[0]
top_countries.drop(top_countries.tail(1).index,inplace=True)
#print(top_countries.tail())

def top_ten(df, col_name):
    country_list=[]
    country_list.clear()
    top_10 = df.nlargest(10,col_name)
    #country_list.append(top_10["Country_Name"])
    print(top_10[["Country_Name","Total_Summer","Total_Winter","Total_Medals"]])
    country_list = top_10['Country_Name'].tolist()
    return country_list

top_10_summer = top_ten(top_countries,"Total_Summer")
print("Top 10 Summer", top_10_summer)

top_10_winter = top_ten(top_countries,"Total_Winter")
print("Top 10 Winter", top_10_winter)

top_10 = top_ten(top_countries,"Total_Medals")
print("Top 10 Medal Count", top_10)


common = [x for x in top_10_summer if x in top_10_winter and x in top_10]
print("Common:", common)


# --------------
#Code starts here
summer_df = data[data["Country_Name"].isin(top_10_summer)]
print(summer_df.head())
winter_df = data[data["Country_Name"].isin(top_10_winter)]
top_df = data[data["Country_Name"].isin(top_10)]

#summer_df.plot.bar(x=summer_df["Country_Name"],y=summer_df["Total_Summer"])
#plt.show()


# --------------
#Code starts here

##  SUMMER  ##
summer_df["Golden_Ratio"]=summer_df["Gold_Summer"]/summer_df["Total_Summer"]
#print(summer_df[["Country_Name","Gold_Summer","Total_Summer","Golden_Ratio"]])
summer_max_ratio = summer_df["Golden_Ratio"].max() #0.4249471458773784
print(summer_max_ratio)
summer_country_gold = summer_df[summer_df["Golden_Ratio"]==summer_max_ratio]["Country_Name"].item() #China
print(summer_country_gold)

##  WINTER  ##
winter_df["Golden_Ratio"]=winter_df["Gold_Winter"]/winter_df["Total_Winter"]
winter_max_ratio = winter_df["Golden_Ratio"].max() #0.4020618556701031
print(winter_max_ratio)
winter_country_gold = winter_df[winter_df["Golden_Ratio"]==winter_max_ratio]["Country_Name"].item() #Soviet Union
print(winter_country_gold)

##  OVERALL  ##
top_df["Golden_Ratio"]= top_df["Gold_Total"]/top_df["Total_Medals"]
top_max_ratio = top_df["Golden_Ratio"].max()
print(top_max_ratio)
top_country_gold = top_df[top_df["Golden_Ratio"]==top_max_ratio]["Country_Name"].item()
print(top_country_gold)





# --------------
#Code starts here
data_1 = data[:-1]

#Add new Column "Total Points" to data_1
data_1["Total_Points"]= data_1["Gold_Total"]*3 + data_1["Silver_Total"]*2 + data_1["Bronze_Total"]*1
#print(data_1["Total_Points"].head())

most_points = max(data_1["Total_Points"])
print(most_points)
# Use the previous codes solution method
best_country = data_1.loc[data_1["Total_Points"].idxmax,"Country_Name"]
print(best_country)


# --------------
#Code starts here

best = data[data["Country_Name"]==best_country]

best = best[['Gold_Total','Silver_Total','Bronze_Total']]
print(best)

best.plot.bar(stacked = True)
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation=45)


