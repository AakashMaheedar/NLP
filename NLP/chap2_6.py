import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root ='E:\\NLP\\MyFiles'
wordlists=PlaintextCorpusReader(corpus_root,'.*')
list=wordlists.fileids()
print(list)
list2=wordlists.words('kc.txt')
print(list2)
