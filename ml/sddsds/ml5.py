import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from  sklearn import metrics
data=pd.read_csv("/home/ai31/Desktop/common/ML/Day3/Questions/city.csv")
#print(data)
#print(data.head())
data=data.as_matrix()
x=data[:,[2,3,4,5]]
y=data[:,[-2]]
print(x)
print(y)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
lr=LinearRegression()
lr.fit(x_train,y_train)
p=lr.predict(x_test)
plt.scatter(y_test,p)
plt.show()                   
