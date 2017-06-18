#!/bin/python

import sys
import string
from elasticsearch import Elasticsearch
import urllib2

keyword = sys.argv[1]

chars = set("{}*\" ".format(string.lowercase[:26]))
if not all((c in chars) for c in keyword):
    print('Input niet geldig, gebruik alleen kleine letters, "\'s en/of spatie(s)')
    exit(1)

es = Elasticsearch([{'host': '192.168.122.249', 'port': 9200}])

matches =  es.search(index='reizen', doc_type='avonturen', q=keyword)
hits = matches['hits']['hits']
if not hits:
	print 'Niets gevonden :('
else:
	keyword = urllib2.quote("'{}'".format(keyword))
	print "<ul>"
	for hit in hits:
		print '<li>Reisavontuur: <a href=https://www.reisavonturen.net/cgi/storiesnew.cgi?zoekstring={}&sid={}&s={}>{}</a> ({}, {})\n<br>Score: {}</li>'.format(
			keyword,
			hit['_id'],
			hit['_source']['avonturiers'],
			hit['_source']['titel'],
			hit['_source']['avonturiers'],
			hit['_source']['continent'],
			hit['_score']
		)
	print "</ul>"
