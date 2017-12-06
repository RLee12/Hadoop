import sys

for line in sys.stdin:
    word, length, count = line.strip().split("\t")
    if word:
        
        # Sort each word before outputing them, since words with different permutations will be exactly the 
        # same after being sorted.
        print "%s\t%s\t%d" % ("".join(sorted(word)), word, int(count))
