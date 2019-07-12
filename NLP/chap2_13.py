import nltk
from nltk.tokenize import word_tokenize
s=input("Enter some text :")
raw=len(word_tokenize(s))
print("You Have Typed ",raw," words")
