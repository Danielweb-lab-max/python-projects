import pandas
import matplotlib.pyplot as plt
data=pandas.read_csv('data.csv')
data.plot(kind = 'hist', x = 'Duration', y = 'Calories')
plt.show()