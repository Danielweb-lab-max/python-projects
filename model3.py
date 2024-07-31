#model to predict co2 emission of a car
#based on size of the engine
import pandas as pd
from sklearn import linear_model
data=pd.read_csv('cardata.csv')
x=data[['Weight','Volume']]
y=data['CO2']
regr=linear_model.LinearRegression()
regr.fit(x,y)
#predict co2 emission of car where given some
#car weight and a volume
predictedCo2=regr.predict([[2300,1300]])
print(predictedCo2)
#We have predicted that a car with a 1.3 litre engine
#capacity and a weight of 2300kg will
#emit 107 grams of co2