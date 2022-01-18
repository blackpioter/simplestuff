import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='docker' host='localhost' port='5432'")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()

    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='docker' host='localhost' port='5432'")
    cur = conn.cursor()

    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()

    conn.close()

def delete(item):
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='docker' host='localhost' port='5432'")
    cur = conn.cursor()

    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()

    conn.close()

def update(item, quantity):
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='docker' host='localhost' port='5432'")
    cur = conn.cursor()

    cur.execute("UPDATE store SET quantity=%s WHERE item=%s", (quantity,item))
    conn.commit()

    conn.close()

def view():
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='docker' host='localhost' port='5432'")
    cur = conn.cursor()

    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()

    return rows

create_table()
insert("Wine glass", 10, 12.5)
print(view())

update("Wine glass", 50)
print(view())

delete("Wine glass")
