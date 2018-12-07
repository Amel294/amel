from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.linear_model import Lasso
import matplotlib.pyplot as plt
data=load_boston()
#print data
X=data.data
y=data.target
rf=RandomForestRegressor()

rf.fit(X,y)
predictions=rf.predict(X)
print(mean_squared_error(y,predictions))
plt.scatter(y,predictions)
plt.show()
