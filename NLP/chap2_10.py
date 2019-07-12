import nltk
puzzle_letters=nltk.FreqDist('egivrvonl')
obligatory='r'
wordlist=nltk.corpus.words.words()
words=[w for w in wordlist if len(w)>=6 and obligatory in w and nltk.FreqDist(w)<=puzzle_letters]
print(words)
#names...
names=nltk.corpus.names
print(names.fileids())

male_names=names.words('male.txt')
female_names=names.words('female.txt')
common_names=[w for w in male_names if w in female_names]
print(common_names)
