from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
import pandas as pd
t1=pd.read_csv("data_banknote_authentication.txt")
t=t1.values
X=t[:,:-1]
y=t[:,4]
Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.2)
knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(Xtrain,ytrain)
p=knn.predict(Xtest)

print "Accuracy Score :",accuracy_score(ytest,p)
print "Confusion Matrix : \n",confusion_matrix(ytest,p)

def fn(p):
	if p==0:
		return "Counterfit"
	else:
		return "Not Counter Fit"
a1=[]
a=input("Enter Variance,Skewness,Curtosis,Entropy of Wavlet Transform Image : ")
a1.append(a)
print fn(knn.predict(a1))

