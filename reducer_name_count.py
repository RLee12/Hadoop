# Count the number of names in the dataset. A name has the following properties:
# 1. The first character is not a digit
# 2. The first letter is uppercase, and all the other letters are lowercase
# 3. When this word appears in the dataset regardless of its case (i.e. the first letter is not necessarily upper case) 
# and condition (2) is not met, the occurrence of such case is less than 0.5%

import sys

names_dict = {}
all_words = {}

for line in sys.stdin:
    word, wcount = line.strip().split("\t", 1)
    
    # Count words regardless of first and second condition.
    all_words[word.lower()] = all_words.get(word.lower(), 0) + int(wcount)
    
    # Take all three conditions into consideration.
    if word[0].isupper() and word[1:].islower():
        names_dict[word.lower()] = names_dict.get(word.lower(), 0) + int(wcount)
    
for key, value in names_dict.items():
    if key:
        if 100.*value/all_words.get(key)>=99.5:
            print "%s\t%d" % (key, value)
