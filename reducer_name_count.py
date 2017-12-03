
import sys

names_dict = {}
all_words = {}

for line in sys.stdin:
    word, wcount = line.strip().split("\t", 1)
    all_words[word.lower()] = all_words.get(word.lower(), 0) + int(wcount)
    if word[0].isupper() and word[1:].islower():
        names_dict[word.lower()] = names_dict.get(word.lower(), 0) + int(wcount)
    
for key, value in names_dict.items():
    if key:
        if 100.*value/all_words.get(key)>=99.5:
            print "%s\t%d" % (key, value)