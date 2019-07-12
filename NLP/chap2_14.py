import nltk
from nltk.tokenize import word_tokenize
raw = open('E:\\NLP\\process.txt').read()
print(type(raw))

tokens=word_tokenize(raw)
type(tokens)
words=[w.lower() for w in tokens]
type(words)
print(words)
