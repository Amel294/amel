from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data=pd.read_csv("ex1.txt")
#print(data)
data=data.as_matrix()
print(data)
x_profit=data[:,[1]]
y_population=data[:,[0]]
print(x_profit)
print(y_population)
plt.scatter(y_population,x_profit)
plt.show()
x_train,x_test,y_train,y_test=train_test_split(y_population,x_profit,test_size=0.2)
lr=LinearRegression
lr.fit(x_train,y_train)
p=lr.predict(x_test)

