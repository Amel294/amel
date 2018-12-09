
from sklearn import preprocessing
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import matplotlib.pyplot as plt

df=pd.read_csv("/home/ai31/Desktop/common/ML/Day7/bank.csv",delimiter=',')
data=df.as_matrix()
print df
X=data[:,1:4]
y=data[:,4]
print X
print y
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
knn=KNeighborsClassifier(n_neighbors=2)
knn.fit(X_train,y_train)
p=knn.predict(X_test)
a=accuracy_score(y_test,p)
print("accuracy",a)
print("confusion matrix")
print(classification_report(y_test,p))

