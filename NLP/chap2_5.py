import nltk
from nltk.corpus import brown
cdf=nltk.ConditionalFreqDist((genre,word)
                             for genre in brown.categories()
                             for word in brown.words(categories=genre))
genres=['news','hobbies','romance','humor']
modals=['can','could','may','might','must','will']
cdf.tabulate(conditions=genres,samples=modals)
