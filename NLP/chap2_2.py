from nltk.corpus import gutenberg
gutenberg.fileids()
macbeth_sentences=gutenberg.sents('shakespeare-macbeth.txt')
longest_len=max(len(s) for s in macbeth_sentences)
list1=[]
for s in macbeth_sentences:
    if len(s)==longest_len:
        list1.append(s)
print(list1)
