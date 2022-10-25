from tkinter import *
import sqlite3


def test_ui():
    root = Tk()
    root.geometry("600x600")
    root.title("SEDAT HOTEL ROOM INFORMATION")

    database = "Hotel.db"

    # Create a db or connect to one
    conn = sqlite3.connect(database)
    # Create a cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT cost FROM customers")
    records = c.fetchall()
    for record in records:
        print(record[0])
    conn.close()

if __name__ == '__main__':
    test_ui()