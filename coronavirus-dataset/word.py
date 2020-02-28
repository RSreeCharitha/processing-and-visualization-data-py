import sqlite3

conn = sqlite3.connect('corona.sqlite')
cur = conn.cursor()


country = 'Mainland China'
cur.execute('SELECT State FROM coronavirus WHERE Country=? AND NOT State = ? LIMIT 10', (country , '0'))

for i in cur:
    print(i)



f = open('word.js','w')
f.write('words= ["')
