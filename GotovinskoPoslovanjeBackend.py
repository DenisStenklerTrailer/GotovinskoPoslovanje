import sqlite3

def connect():
    conn = sqlite3.connect("GotovinskoPoslovanje.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS GotovinskoPoslovanje (id INTEGER PRIMARY KEY, datum DATE, purpose TEXT, price FLOAT)")
    conn.commit()
    conn.close()

def insert(date, purpose, price):
    conn = sqlite3.connect("GotovinskoPoslovanje.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO GotovinskoPoslovanje VALUES (NULL,?,?,?)",(date,purpose,price))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("GotovinskoPoslovanje.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM GotovinskoPoslovanje")
    rows = cur.fetchall()
    conn.close()
    return rows

def view_plus():
    conn = sqlite3.connect("GotovinskoPoslovanje.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM GotovinskoPoslovanje WHERE price>0")
    rows = cur.fetchall()
    conn.close()
    return rows

def view_minus():
    conn = sqlite3.connect("GotovinskoPoslovanje.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM GotovinskoPoslovanje WHERE price<0")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(datum='', purpose='', price=''):
    conn = sqlite3.connect("GotovinskoPoslovanje.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM GotovinskoPoslovanje WHERE datum=? OR purpose=? OR price=?", (datum,purpose,price))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("GotovinskoPoslovanje.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM GotovinskoPoslovanje WHERE id=?", (id,))
    conn.commit()
    conn.close()

def sum():
    conn = sqlite3.connect("GotovinskoPoslovanje.db")
    cur = conn.cursor()
    cur.execute("SELECT SUM(price) FROM GotovinskoPoslovanje")
    sum = cur.fetchall()
    conn.close()
    return sum

def update(id, datum, purpose, price):
    conn = sqlite3.connect("GotovinskoPoslovanje.db")
    cur = conn.cursor()
    cur.execute("UPDATE GotovinskoPoslovanje SET datum=?,purpose=?,price=? WHERE id=?",(datum, purpose, price, id))
    conn.commit()
    conn.close()

connect()
print(sum())
#insert("27.11.2019", "Bend", -2122.4)
#delete(1)
#print(view())
#print(search(purpose="Bend"))