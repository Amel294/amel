from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import Ridge
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.linear_model import Lasso
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('/home/ai31/ml/Day8/x03.txt',delimiter='\s+')
#print data
data=data.as_matrix()
X=data[:,(1,2)]
y=data[:,3]
rf=KNeighborsRegressor()

rf.fit(X,y)
predictions=rf.predict(X)
print(mean_squared_error(y,predictions))
plt.scatter(y,predictions)
plt.show()

