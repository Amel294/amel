#!/usr/bin/python

from textblob import TextBlob
a=TextBlob("The children are in the rain")
print(a.tags)
