#synonymous set..
import nltk
from nltk.corpus import wordnet as wn
print(wn.synsets('motorcar'))
print(wn.synset('car.n.01').lemma_names())
'''
[Synset('car.n.01')]
['car', 'auto', 'automobile', 'machine', 'motorcar'
'''

print(wn.synset('car.n.01').definition())
'''
a motor vehicle with four wheels; usually propelled by an internal combustion engine
'''
myinput=input("type: ")
print(wn.synsets(flower))
