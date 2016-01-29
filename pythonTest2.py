import json
import psycopg2
import psycopg2.extras

#conn = psycopg2.connect("dbname=uniart4_pr host=localhost user=user password=password")
conn = psycopg2.connect('dbname=infraredRF')
#cur = conn.cursor()
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
cur.execute("""
select "remoteName", "buttonData"->'button'->>'volup' as avolup,"buttonData" from "infraredRF_data"
""")
#results = []
for row in cur.fetchall():
     print row['remoteName'],row['buttonData'],row['avolup']


