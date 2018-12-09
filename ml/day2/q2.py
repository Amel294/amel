from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
iris=load_iris()
#print(iris)
#print(len(iris))
X=iris.data
#print X
#print(len(X))
y=iris.target
#print y
Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.2)
#print(len(Xtrain))
#print(len(Xtest))
#print(len(ytrain))
#print(len(ytest))
knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(Xtrain,ytrain)
p=knn.predict(Xtest)
print "Accuracy Score :",accuracy_score(ytest,p)
print "Confusion Matrix : \n",confusion_matrix(ytest,p)
