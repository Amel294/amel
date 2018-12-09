import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
da=pd.read_csv("/home/ai31/Desktop/common/ML/Day3/Advertising.csv")
print(da.head())
da=da.as_matrix()
print(da)
x=da[:,[1,2,3]]
y=da[:,-1]
#print(x)
#print(y)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
lr=LinearRegression()
#print(x_train)
lr.fit(x_train,y_train)
p=lr.predict(x_test)
plt.scatter(y_test,p)
plt.show()
