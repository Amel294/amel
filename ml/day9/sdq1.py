from sklearn import preprocessing
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import matplotlib.pyplot as plt

df=pd.read_csv("/home/ai31/Desktop/common/ML/Day2/Questions/Immunotherapy.csv")
data=df.as_matrix()
#assification_report(y_test,p))
print df
X=data[:,0:7]
y=data[:,7]
#print X
#print y
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
knn=KNeighborsClassifier(n_neighbors=2)
knn.fit(X_train,y_train)
p=knn.predict(X_test)
a=accuracy_score(y_test,p)
print("accuracy",a)
print("confusion matrix")
print(classification_report(y_test,p))

scaler = preprocessing.StandardScaler().fit(X)
Xs=scaler.transform(X)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)
p1=knn.predict(X_test)
a1=accuracy_score(y_test,p1)
print("accuracy",a1)
print("confusion matrix")
print(classification_report(y_test,p1))
