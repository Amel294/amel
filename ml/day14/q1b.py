def ae(a):
        from sklearn.datasets import load_iris
        from sklearn.neural_network import MLPClassifier
        iris=load_iris()
        type(iris)
        if a==50:
                print('When iter is 50')
        elif a==500:
                print('Whaen iter is 500')
        elif a==1000:
                print('Whaen iter is 1000')
        #print(iris.feature_names)
        #print(iris.data)
        X=iris.data
        y=iris.target

	knn=MLPClassifier(activation='tanh',hidden_layer_sizes=(2),solver='sgd',learning_rate_init=0.01,max_iter=a,verbose=True)
        print(knn)
        knn.fit(X,y)
        print(knn.predict([[3,5,4,2]]))
        p=knn.predict(X)
        from sklearn.metrics import confusion_matrix
        print(confusion_matrix(y,p))
	print(knn.coefs_)
a=ae(50)
a=ae(500)
a=ae(1000)
