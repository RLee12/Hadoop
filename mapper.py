import sys
import re

reload(sys)

# Change the encoding to utf-8, since there are many non-English 
# characters in the dataset.
sys.setdefaultencoding("utf-8")

stop_words = [unicode(line.strip()) for line in open("stop_words_en.txt").readlines()]

for line in sys.stdin:
    try:
        article_id, text = unicode(line.strip()).split('\t', 1)
    except ValueError as e:
        continue
    
    # Remove special characters at the start or at the end of any string.
    text = re.sub("^\W+|\W+$", "", text, flags=re.UNICODE)
    
    # Split words by any non-word characters and white space.
    words = re.split("\W*\s+\W*", text, flags=re.UNICODE)
    
    for word in words:
        print "%s\t%d" % (word, 1) # Output (key, value) pair.
