import sys
import re

reload(sys)
sys.setdefaultencoding("utf-8")

stop_words = [unicode(line.strip()) for line in open("stop_words_en.txt").readlines()]

for line in sys.stdin:
    try:
        article_id, text = unicode(line.strip()).split('\t', 1)
    except ValueError as e:
        continue
    text = re.sub("^\W+|\W+$", "", text, flags=re.UNICODE)
    words = re.split("\W*\s+\W*", text, flags=re.UNICODE)
    for word in words:
        if word:
            if word.lower() not in stop_words:
                print "%s\t%d" % (word.lower(), 1)
