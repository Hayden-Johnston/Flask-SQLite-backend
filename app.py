# author: Hayden Johnston
# github: hgjohn
# date: 07/11/2023
# description: Flask SQLite database functions

from flask import Flask
import sqlite3

app = Flask(__name__)

def connect_db():
    """Connects to sqlite database."""
    try:
        con = sqlite3.connect('database.db')
    except:
        print("database.db connection failed")
    finally:
        return con

def create_table():
    """Creates a table in the database."""
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute("CREATE TABLE my_table ("
                    "name TEXT NOT NULL, "
                    "value TEXT)")

        con.commit()
        print("User table created.")
    except:
        print("Table creation failed")
    finally:
        con.close()

def insert_db(data):
    """Add a new entry to the table."""
    con = connect_db()
    cur = con.cursor()
    try:
        cur.execute("INSERT or IGNORE into my_table (name, value) VALUES (?, ?)",
                    (data['name'], data['value']))
        con.commit()
        con.rollback()
    except:
        print("Unable to add to database.")
    finally:
        con.close()

def get_db():
    """Get all items from the table."""
    items = []
    con = connect_db()
    cur = con.cursor()
    try:
        cur.execute("SELECT * FROM my_table")
        database_data = cur.fetchall()

        for data in database_data:
            dict = {"name": data[0], "value": data[1]}
            items.append(dict)

    except:
        print("Error: unable to fetch database")
    finally:
        con.close()
    return items

def get_by_name(name):
    """Get item data by name."""
    con = connect_db()
    cur = con.cursor()
    try:
        
        cur.execute(f"SELECT * FROM my_table WHERE name= ?;",(name,))
        row = cur.fetchall()
    except:
        print("get med by name failed")
    finally:
        con.close()
        return row

def update_db(data):
    """Update an item in the database."""
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute("UPDATE my_table SET value = ? WHERE name = ?",
                    (data['value'], data['name']))
        con.commit()
    except Exception as e:
        print("update database failed", str(e))
    finally:
        con.close()

def delete_db(name):
    """Delete an item from the database."""
    try:
        con = connect_db()
        con.execute("DELETE FROM my_table WHERE name = ?",
                    (name,))
        con.commit()
    except:
        print("Unable to delete database.")
    finally:
        con.close()

# ---------------------------- BASIC TESTING --------------------------- #

# create_table()
# insert_test = {"name": "test", "value": "test_value"}
# insert_db(insert_test)
# print(get_by_name("test"))
# update_test = {"value": "test_notes", "name": "test"}
# update_db(update_test)
# delete_db("test")
# print(get_db())