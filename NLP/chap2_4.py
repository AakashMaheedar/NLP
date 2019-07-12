import nltk
from nltk.corpus import brown
news_text = brown.words(categories='news')
fdlist=nltk.FreqDist(w.lower() for w in news_text)
modals=['what','when','how','why']
for m in modals:
    print (m+ ":",fdlist[m],end=' ')
