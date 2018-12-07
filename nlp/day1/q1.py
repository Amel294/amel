from textblob import TextBlob
d=TextBlob('welcome to world of book')
print (d.sentences)

print (d.words)

print (d.noun_phrases)
