import sqlite3

conn = sqlite3.connect('corona.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS coronavirus')

cur.execute('CREATE TABLE coronavirus(State TEXT, Country TEXT, LastUpdate TEXT, Confirmed INTEGER, Suspected INTEGER, Recovered INTEGER, Death INTEGER);')

f = open('corona_uncleaned.csv')
j=0
k=None
for i in f:
    l = i.split(',')
    if(k==None): 
        k=1
        continue
    if(l[0]==''): l[0]='0'
    if(l[3]==''): l[3]=0
    if(l[4]==''): l[4]=0
    if(l[5]==''): l[5]=0
    if(l[6]==''): l[6]=0

    l[2] = l[2].split()[0]

    ### cur.execute('''INSERT INTO Counts (email, count) VALUES (?, 1)''', (email,))
    cur.execute('INSERT INTO coronavirus (State, Country, LastUpdate, Confirmed, Suspected, Recovered, Death) VALUES (?, ?, ?, ?, ?, ?, ?)', (l[0], l[1], l[2], l[3], l[4], l[5], l[6],  ))
    j+=1
    print('{} rows inserted'.format(j))
    conn.commit()
    
