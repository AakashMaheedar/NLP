import nltk
from nltk.tokenize import word_tokenize

raw=open("E:\\NLP\\process.txt").read()
print(len(raw))

token=word_tokenize(raw)
word=[w.lower() for w in token]
print(word[:20])
print(len(word))


vocab=sorted(set(word))
print(vocab[:20])
print(len(vocab))
