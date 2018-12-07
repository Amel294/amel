from textblob import TextBlob
a=TextBlob("intreset")
print(a.correct())
b=(a.correct())
print(b.detect_language())
print(b.translate(to="fr"))
