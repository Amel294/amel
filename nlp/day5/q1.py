
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
s1='The sun is blue'
s2='The sun is bright'
s3='The flowers are beautifull'
s4='day is wednesday'
s5='Coding is fun'
query='The day is bright and beautifull'
dataset=[s1,s2,s3,s4,s5]
tfidf=TfidfVectorizer()
tfidf.fit(dataset)
matrix=tfidf.fit_transform(dataset)
dict=tfidf.vocabulary_
for key in dict.keys():
        print(key+" "+str(dict[key]))
dataset1=[s1,s2,s3,s4,s5,query]
x=tfidf.fit_transform(dataset)
y=cosine_similarity(x)
print(y)

