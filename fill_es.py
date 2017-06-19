#!/bin/python

import MySQLdb
import json
from elasticsearch import Elasticsearch

# local config
import config
conn = MySQLdb.connect(user=config.user, passwd=config.password,
                       host=config.host,db=config.db)

cursor = conn.cursor()
query = ("SELECT sid, linkname, title, story, begindatum, einddatum, cont FROM avonturen order by sid")

cursor.execute(query)
es = Elasticsearch([{'host': '192.168.122.249', 'port': 9200}])
for (sid, linkname, title, story, begindatum, einddatum, cont) in cursor:
  print "Doing story with id: {}".format(sid)
  # decode/encode story (needed for windows specials..)
  story = story.decode('windows-1252')
  story = story.encode('utf-8')
  # replace newlines (..)
  story = story.replace('\n',' ').replace('\r','')
  # insert into ES
  # db reizen = ES index
  # table avonturen = ES doc_type
  # sql id (sid) = ES id
  # sql other columns = ES body
  es.index(index='reizen', doc_type='avonturen', id=sid, body={
    'avonturiers': linkname,
    'titel': title,
    'avontuur': json.dumps(story),
    'begindatum': begindatum,
    'einddatum': einddatum,
    'continent': cont
  })
cursor.close()
conn.close()
