
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics as m
import numpy as np
from mpl_toolkits import mplot3d
from sklearn.model_selection import train_test_split


a=pd.read_csv('ex2.txt')
a=a.as_matrix()
area=a[:,[0]]
bed=a[:,[1]]
price=a[:,[2]]
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.scatter3D(area,bed,price)
plt.show()
lr=LinearRegression()
x=a[:,[0,1]]
y=a[:,[2]]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2)
lr.fit(x_train,y_train)
hp=lr.predict(x_test)
print(np.sqrt(m.mean_squared_error(y_test,hp)))
