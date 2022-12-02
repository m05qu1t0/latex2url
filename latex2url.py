import re
import sys
import urllib.parse
# 2 lines hahah
with open(sys.argv[1], "r", encoding="utf-8") as fp, open(sys.argv[2], "w", encoding="utf-8") as fq:
    fq.write(re.sub(r"(\${1,2})[^\$]+\1", lambda s: "![]("+r"http://latex.codecogs.com/gif.latex?" + urllib.parse.quote(s.group(0).strip("$"))+")", fp.read()))