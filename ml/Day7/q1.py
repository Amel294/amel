from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score,train_test_split,KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from matplotlib import pyplot as plt
import pandas as pd

iris=load_iris()
#data=data.as_matrix()
#print(iris)
X=iris.data
y=iris.target
kfold=KFold(10,random_state=7)
models=[]
models.append(("DT",DecisionTreeClassifier()))
models.append(("KNN",KNeighborsClassifier()))
models.append(("NB",GaussianNB()))
models.append(("SV",SVC()))
models.append(("LR",LogisticRegression()))
result=[]
names=[]
scoring='accuracy'
for name,model in models:
	kfold=KFold(n_splits=10,random_state=7)
	v=cross_val_score(model,X,y,cv=kfold,scoring=scoring)
	result.append(v)
	names.append(name)
	print(name)
	print(v)
fig=plt.figure()
fig.suptitle('Algorithm Comparison')
ax=fig.add_subplot(111)
plt.boxplot(result)
ax.set_xticklabels(names)
plt.show()

