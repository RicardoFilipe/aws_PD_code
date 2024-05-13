#!/usr/bin/python
import psycopg2
import psycopg2.extras
import decimal
import os


db_host = "XXX.rds.amazonaws.com"
db_port = 5432
db_name = "analytics"
db_user = "postgres" #change me
db_pass = "postgres" #change me


def make_conn():
    conn = None
    try:
        conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (db_name, db_user, db_host, db_pass))
    except:
        print ("I am unable to connect to the database")
    return conn


def fetch_data(conn):
    result = []
    
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # get info
    query_cmd = 'select a.barcode, a.type as description, a.year as year, a.stockqty  from public."warehouseinfo" a'
    
    cursor.execute(query_cmd)

    raw = cursor.fetchall()
    for line in raw:
        result.append(line)

    return result