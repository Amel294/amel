#!/usr/bin/python

from textblob import Word
theword = Word("watch")
print(theword.pluralize())



from textblob import Word
theword = Word("watches")
print(theword.singularize())
