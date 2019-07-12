from nltk.corpus import webtext
for fileids in webtext.fileids():
    print(fileids,webtext.raw(fileids)[:65],'....')
    
