import sys

for line in sys.stdin:
    word, length, count = line.strip().split("\t")
    if word:
        print "%s\t%s\t%d" % ("".join(sorted(word)), word, int(count))
