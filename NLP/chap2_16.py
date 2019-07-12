import nltk,re
from nltk.corpus import stopwords
list1=[w for w in nltk.corpus.words.words('en') if w.islower()]
print(list1)
