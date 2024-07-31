#import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
#generate random 100000 values between 5 and 1
#x=np.random.normal(5.0,1.0,100000)
#plot histogram to visualize the above data
#plt.show()
#x->age of cars
x=[5,7,8,7,2,17,2,9,4,11,12,9,6]
#y->average speeds of cars
y=[99,86,87,88,111,86,103,87,94,78,77,85,86]
slope,intercept,r,p,std_err=stats.linregress(x,y)
def plotGraph(x):
    return slope*x+intercept
speed=plotGraph(25)
print(speed)
#mymodel=list(map(plotGraph,x))

#plt.scatter(x,y)
#plt.plot(x,mymodel)
#plt.show()

