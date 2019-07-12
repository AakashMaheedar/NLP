import nltk
from nltk.tokenize import word_tokenize



raw="""DENNIS: Listen, strange women lying in ponds distributing swords
... is no basis for a system of government.  Supreme executive power derives from
... a mandate from the masses, not from some farcical aquatic ceremony."""

token=word_tokenize(raw)
print(token)
string =' '.join(token)
print(string)


fdlist=nltk.FreqDist(['dog', 'cat', 'dog', 'cat', 'dog', 'snake', 'dog', 'cat'])
print(fdlist)
for word in sorted(fdlist):
    print(word,'->',fdlist[word],end='; ')
