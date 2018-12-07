from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error,mean_absolute_error

from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt
import pandas
import numpy

data = load_boston()
#print data
X=data.data
y=data.target
reg=MLPRegressor()
reg.fit(X,y)
predictions=reg.predict(X)
print (mean_squared_error(y,predictions))
print (mean_absolute_error(y,predictions))
plt.scatter(y,predictions)
plt.show()





