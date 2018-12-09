from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from  sklearn import metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv("/home/ai31/Desktop/common/ML/Day3/pimaindians.csv")
print (data.head())
data=data.as_matrix()
x=data[:,[1,8]]
y=data[:,[-1]]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
lr=LogisticRegression()
lr.fit(x_train,y_train)
p=lr.predict(x_test)
plt.scatter(y_test,p)
plt.show()
