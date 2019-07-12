from nltk.corpus import gutenberg
gutenberg.fileids()
for fileids in gutenberg.fileids():
    num_letters=len(gutenberg.raw(fileids))
    num_words=len(gutenberg.words(fileids))
    print(fileids,"  ",num_letters,"  ",num_words)
    
