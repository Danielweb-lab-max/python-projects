import pandas
data=pandas.read_csv('data.csv')
calories_mean=data["Calories"].mean()
data["Calories"].fillna(calories_mean,inplace=True)
print(data.describe())

#data.dropna(inplace=True)
#data.fillna(150,inplace=True)
#to replace only for specified columns
#data["Calories"].fillna(150,inplace=True)
#to calculate mean
#calories_mean=data["Calories"].mean()
#to calculate median
#calories_median=data['Calories'].median()
#to calculate mode
# calories_mode=data['Calories'].mode()[0]

# data["Calories"].fillna(calories_mode,inplace=True)
# print(data.to_string())
