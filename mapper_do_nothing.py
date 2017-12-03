
import sys

for line in sys.stdin:
    word, count = line.strip().split("\t", 1)
    print "%s\t%d" % (word, int(count))