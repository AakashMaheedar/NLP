import nltk
from nltk.tokenize import word_tokenize
raw="Hi my name Aakash ,and aakash is a good boy"


#normalize..
token=word_tokenize(raw)
word=[w.lower() for w in token]

#count - FreqDist
fd=nltk.FreqDist(word)
for word in sorted(fd):
    print(word,'->',fd[word],end=' ')
print('I want a {} right now'.format('coffee'))
