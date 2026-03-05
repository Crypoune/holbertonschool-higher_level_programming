#!/usr/bin/python3
"""
    Script that lists all states from the database.
"""
import MySQLdb
import sys


def list_states(username, password, db_name):
    """ LIsts all states from the database `db_name` """
    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
            charset="utf8"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print(f"MySQL Error: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
