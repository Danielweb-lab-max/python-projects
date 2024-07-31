#r squared technique
#measure the relationship between the x axis and y axis
#and the value ranges from 0 to 1
#0 means no relationship
#1 means totally related
import numpy
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
x=numpy.random.normal(3,1,100)
y=numpy.random.normal(150,40,100)/x
train_x=x[:80]
train_y=y[:80]
test_x=x[80:]
test_y=y[80:]
mymodel=numpy.poly1d(numpy.polyfit(train_x,train_y,4))
#r2=r2_score(train_y,mymodel(train_x))
r2=r2_score(test_y,mymodel(test_x))
print(r2)
myline=numpy.linspace(0,6,100)
plt.scatter(train_x,train_y)
plt.plot(myline,mymodel(myline))
plt.show()