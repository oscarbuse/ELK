#!/bin/python

import sys
import string

keyword = sys.argv[1]

chars = set("{}*\" ".format(string.lowercase[:26]))
if not all((c in chars) for c in keyword):
    print('Input not clean')
else:
    print "Keyword: {}".format(keyword)
