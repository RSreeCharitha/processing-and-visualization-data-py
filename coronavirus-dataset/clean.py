import sqlite3

conn = sqlite3.connect('corona.sqlite')
cur = conn.cursor()

cur.execute('SELECT count(*) FROM coronavirus;')

count=cur.fetchone()[0]


cur.execute("DELETE FROM coronavirus where State='0';")

cur.execute('SELECT count(*) FROM coronavirus;')

print('Deleted {} rows'.format(count-cur.fetchone()[0]))


conn.commit()