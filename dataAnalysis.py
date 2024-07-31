import numpy
import matplotlib.pyplot as plt
import scipy
#mean-average of values
#speed=[99,76,90,65,85,76]
#meanValue=numpy.mean(speed)
#print(meanValue)
#median-is the value in the middle
#after you have sorted out the data
#medianValue=numpy.median(speed)
#print(medianValue)
#standard deviation
#is a value that describes
#how spread out the values are
#low std deviation->means that most of the values are closer to the mean value
#high std deviation->means that most of the values are spread out over a wider range
#stdDev=numpy.std(speed)
#print(stdDev)
#Variance->indicates how spread out the values are
#varianceData=numpy.var(speed)
#print(varianceData)
#Generating big data
#random()->generate random values
#data=numpy.random.randint(0,10,5)
#print(data)
#Histogram
# data=numpy.random.uniform(0.0,5.0,100)
# plt.hist(data,5)
# plt.show()
#scatter
#x=[10,20,30,40,50]
#y=[59,67,87,89,67]
#plt.scatter(x,y)
#plt.show()
#####SCIPY-Scientific Python#####
#print(scipy.__version__)\
#Linear Regression
#Regression is a term used when you
#try to find a relationship
#between variables
#You can use this relationship to
#predict future events
#Linear regression uses the 
#relationship between data points
#to draw a straight line through
#all of them
#the line can be used to predict
#future events
# x=[5,7,8,7,2,17,2,9,4,11,12,9,6]
# y=[99,86,87,88,111,86,103,87,94,78,77,85,86]
# plt.scatter(x,y)
# plt.show()
x=numpy.random.normal(3,1,100)
y=numpy.random.normal(150,40,100)/x
training_set_x=x[:80]
training_set_y=y[:80]
test_x=x[80:]
test_y=y[80:]
#plt.scatter(training_set_x,training_set_y)
plt.scatter()
plt.show()