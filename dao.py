import psycopg2 as psycopg


def insert(src, title):
    with psycopg.connect("dbname='postgres' user='postgres' host='0.0.0.0' password='1234'") as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO images (image, title) VALUES (%s, %s)", (src, title))


def select():
    with psycopg.connect("dbname=postgres user=postgres host=0.0.0.0 password=1234") as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM images")
            return cur.fetchall()