import sqlite3
from register import passwd

print(passwd)
conn = sqlite3.connect('db/db.db')
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS master_login(usr TEXT, password TEXT)')


def data_entry():
    c.execute("INSERT INTO master_login VALUES('anantnrg', 'password')")
    conn.commit()
    c.close()
    conn.close()


create_table()
data_entry()