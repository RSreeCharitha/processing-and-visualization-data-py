import sqlite3

conn = sqlite3.connect('corona.sqlite')
cur = conn.cursor()

l=list()
country = 'Mainland China'
cur.execute('SELECT DISTINCT COUNTRY FROM coronavirus;')
#cur.execute('SELECT State FROM coronavirus WHERE Country=? AND NOT State = ? LIMIT 10', (country , '0'))

for i in cur:
    l.append(i[0])

print(len(l))
print(l)

cur.execute('SELECT COUNT(*) from coronavirus')
count = cur.fetchone()[0]

f = open('word.js','w')
f.write('myWords= [\n')

lol = l[len(l)-1]

for i in l:
    cur.execute('SELECT COUNT(Country) FROM coronavirus where Country = ? ',(i,))
    num = cur.fetchone()[0]
    if(num>100):
        num=99
    print(num)
    #f.write('{word:'+ i +', size: '+str(num)+'},')
    f.write("{word:'")
    f.write(i)
    f.write("', size: ")
    f.write(str(num))
    f.write("}")
    if(lol!=i):
        f.write(',')
    f.write('\n')

f.write( "\n];\n")
