import nltk, re, pprint
from nltk import word_tokenize


f=open("E:\\NLP\\process.txt")
raw=f.read()
#class type is str..
print(type(raw))
'''<class 'str'>'''
print(len(raw))
'''27848'''
print(raw[:75])
'''
THE TALE OF THE
THREE BROTHERS
Harry turned to look at Ron and Hermione. Ne
'''
tokens=word_tokenize(raw)
print(type(tokens))
print(len(tokens))
print(tokens[:10])

text=nltk.Text(tokens)
print(type(text))
print(text[100:150])
print(text.collocations())

print(raw[:10])
print(len(raw))
print(raw.find("THE TALE"))
print(raw.rfind("THE TALE"))
