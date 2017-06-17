#!/bin/python

import sys
from elasticsearch import Elasticsearch

keyword = sys.argv[1]
es = Elasticsearch([{'host': '192.168.122.249', 'port': 9200}])

matches =  es.search(index='reizen', doc_type='avonturen', q=keyword)
hits = matches['hits']['hits']
if not hits:
	print 'Niets gevonden :('
else:
	for hit in hits:
		print 'Reisavontuur: <a href="https://www.reisavonturen.net/cgi/storiesnew.cgi?sid={}&s={}">{}</a> ({}, {})\nScore: {}\n'.format(
			hit['_id'],
			hit['_source']['avonturiers'],
			hit['_source']['titel'],
			hit['_source']['avonturiers'],
			hit['_source']['continent'],
			hit['_score']
		)
