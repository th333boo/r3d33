#!/usr/bin/env python3
from decouple import config
from sqlalchemy import create_engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

import MySQLdb
db = MySQLdb.connect(host="localhost",user="bbi",passwd="borntobein",db="bbi")
cur = db.cursor()
cur.execute("SELECT * FROM bbi")
for row in cur.fetchall():
    print row[0]
db.close()