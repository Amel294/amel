#!/usr/bin/python

from textblob import TextBlob
fd=open("/home/ai31/nlp/ass2/sample","r")
text=fd.read()
a=TextBlob(text)
#print(a)
sen=a.sentences
print(sen)
print("No of sentence:"+str(len(sen)))
wrd=a.words
#print(wrd)
print("NO of words:"+str(len(wrd)))

print("main"+str(wrd[0]))

for word,tag in text.tags:
	if tag=="NN" or tag=="NNS"
		print "--",word, "=",tag
fd.close()
