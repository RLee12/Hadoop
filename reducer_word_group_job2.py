import sys

current_length = 0
word_group = []

for line in sys.stdin:
    sorted_word, word, count = line.strip().split("\t")
    count = int(count)
    length = len(sorted_word)
    if current_length != length:
        if current_length:
            if len(word_group) > 1:
                print "%d\t%d\t%s" % (sum([x[1] for x in sorted(word_group)]), 
                                      len(word_group), 
                                      ",".join([x[0] for x in sorted(word_group)]))
        current_length = length
        word_group = []
    word_group.append((word, count))

if word_group:
    if len(word_group) > 1:
        print "%d\t%d\t%s" % (sum([x[1] for x in sorted(word_group)]), 
                              len(word_group), 
                              ",".join([x[0] for x in sorted(word_group)]))
