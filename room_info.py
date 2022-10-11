from tkinter import *
import sqlite3


def room_info_ui():
    root = Tk()
    root.geometry("600x600")
    root.title("ROOM INFORMATION")

    def close():
        root.destroy()

    def query():
        # Create a db or connect to one
        conn = sqlite3.connect("Hotel.db")
        # Create a cursor
        c = conn.cursor()

        # Query the database
        c.execute("SELECT * FROM customers")
        records = c.fetchall()
        print(records)

        # Rooms vaiables
        room101 = 0
        room102 = 0
        room103 = 0
        room201 = 0
        room202 = 0
        room203 = 0
        room301 = 0
        room302 = 0
        room303 = 0
        room401 = 0
        room402 = 0
        room403 = 0

        # Loop through records
        print_records = ''
        for record in records:
            if str(record[4]) == '101':
                room101 = 1
            elif str(record[4]) == '102':
                room102 = 1
            elif str(record[4]) == '103':
                room103 = 1
            elif str(record[4]) == '201':
                room201 = 1
            elif str(record[4]) == '202':
                room202 = 1
            elif str(record[4]) == '203':
                room203 = 1
            elif str(record[4]) == '301':
                room301 = 1
            elif str(record[4]) == '302':
                room302 = 1
            elif str(record[4]) == '303':
                room303 = 1
            elif str(record[4]) == '401':
                room401 = 1
            elif str(record[4]) == '402':
                room402 = 1
            elif str(record[4]) == '403':
                room403 = 1

        room_101_cb = Checkbutton(root, text="Room 101   --- Normal 1 bed 1 person room ---")
        room_101_cb.grid(row=4 ,column=0)
        room_101_cb.config(state=DISABLED)
        if room101 == 1:
            room_101_cb.select()
        room_102_cb = Checkbutton(root, text="Room 102   --- Normal 1 bed 1 person room ---")
        room_102_cb.grid(row=5, column=0)
        room_102_cb.config(state=DISABLED)
        if room102 == 1:
            room_102_cb.select()
        room_103_cb = Checkbutton(root, text="Room 103   --- Normal 1 bed 1 person room ---")
        room_103_cb.grid(row=6, column=0)
        room_103_cb.config(state=DISABLED)
        if room103 == 1:
            room_103_cb.select()
        room_201_cb = Checkbutton(root, text="Room 201")
        room_201_cb.grid(row=7, column=0)
        room_201_cb.config(state=DISABLED)
        if room201 == 1:
            room_201_cb.select()
        room_202_cb = Checkbutton(root, text="Room 202")
        room_202_cb.grid(row=8, column=0)
        room_202_cb.config(state=DISABLED)
        if room202 == 1:
            room_202_cb.select()
        room_203_cb = Checkbutton(root, text="Room 203")
        room_203_cb.grid(row=9, column=0)
        room_203_cb.config(state=DISABLED)
        if room203 == 1:
            room_203_cb.select()
        room_301_cb = Checkbutton(root, text="Room 301")
        room_301_cb.grid(row=10, column=0)
        room_301_cb.config(state=DISABLED)
        if room301 == 1:
            room_301_cb.select()
        room_302_cb = Checkbutton(root, text="Room 302")
        room_302_cb.grid(row=11, column=0)
        room_302_cb.config(state=DISABLED)
        if room302 == 1:
            room_302_cb.select()
        room_303_cb = Checkbutton(root, text="Room 303")
        room_303_cb.grid(row=12, column=0)
        room_303_cb.config(state=DISABLED)
        if room303 == 1:
            room_303_cb.select()
        room_401_cb = Checkbutton(root, text="Room 401")
        room_401_cb.grid(row=13, column=0)
        room_401_cb.config(state=DISABLED)
        if room401 == 1:
            room_401_cb.select()
        room_402_cb = Checkbutton(root, text="Room 402")
        room_402_cb.grid(row=14, column=0)
        room_402_cb.config(state=DISABLED)
        if room402 == 1:
            room_402_cb.select()
        room_403_cb = Checkbutton(root, text="Room 403")
        room_403_cb.grid(row=15, column=0)
        room_403_cb.config(state=DISABLED)
        if room403 == 1:
            room_403_cb.select()

        query_label = Label(root, text=print_records)
        query_label.grid(row=3, column=0)

        # Commit change
        conn.commit()

        # close connection
        conn.close()

    # CREATE a query button
    query_btn = Button(root, text="Show Room Info", command=query)
    query_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=124)

    root.mainloop()


if __name__ == '__main__':
    room_info_ui()
