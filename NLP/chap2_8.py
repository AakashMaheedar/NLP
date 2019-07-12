import nltk
from nltk.corpus import gutenberg
def unusal_word(text):
    text_voc=set(w.lower() for w in text if w.isalpha())
    english_vocb=set(w.lower() for w in nltk.corpus.words.words())
    unusal=text_voc-english_vocb
    return sorted(unusal)
print(unusal_word(nltk.corpus.gutenberg.words('austen-sense.txt')))
