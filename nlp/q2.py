from textblob.classifiers import NaiveBayesClassifier
import glob
f=glob.glob("/home/ai31/nlp/nov14/Assignment 3/*/*")
trainData=[]
for i in f:
	cls=i.split('/')[-2]
	data=open(i).read().replace('\n','')
	tupple=(data,cls)
	train.appand(tupple)
classifier=NaiveBayesClass(trainData)
