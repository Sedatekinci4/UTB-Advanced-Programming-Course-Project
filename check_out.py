from tkinter import *
import sqlite3
from tkinter import messagebox


def check_out_ui():
    root = Tk()
    root.title("SEDAT HOTEL CHECK OUT")
    root.geometry("500x500")

    oids = []

    def close():
        root.destroy()

    # Create function to delete a record
    def delete():
        print(oids)
        # Create a db or connect to one
        conn = sqlite3.connect("Hotel.db")
        # Create a cursor
        c = conn.cursor()

        # Query the database
        c.execute("SELECT *, oid FROM customers")
        records = c.fetchall()
        print(records)

        # Loop through records

        print_records = ''
        for record in records:
            oids.append(str(record[6]))

        for oid in oids:
            if str(oid) == str(delete_box.get()):
                print("same")
                c.execute("DELETE from customers WHERE oid=" + delete_box.get())

                # Commit change
                conn.commit()

                # close connection
                conn.close()
                messagebox.showinfo("Success", "Succesfully checked out")
                root.destroy()

        messagebox.showwarning("Warning", "No matching customers!!!")
        # close connection
        conn.close()
        root.destroy()

    def query():
        # Create a db or connect to one
        conn = sqlite3.connect("Hotel.db")
        # Create a cursor
        c = conn.cursor()

        # Query the database
        c.execute("SELECT *, oid FROM customers")
        records = c.fetchall()
        print(records)

        # Loop through records

        print_records = ''
        for record in records:
            print_records += str(record[0]) + " " + str(record[1]) + " " + '\t' + str(record[6]) + "\n"
            oids.append(str(record[6]))

        print(oids)

        query_label = Label(root, text=print_records)
        query_label.grid(row=6, column=0, columnspan=2)

        # Commit change
        conn.commit()

        # close connection
        conn.close()

    # Creating the boxes
    delete_box = Entry(root, width=40, borderwidth=10)
    delete_box.grid(row=0, column=1)

    # Creating the box label
    delete_box_label = Label(root, text="Delete ID")
    delete_box_label.grid(row=0, column=0)

    # CREATE a query button
    query_btn = Button(root, text="Show OID's", command=query)
    query_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=124)

    # create a delete button
    delete_btn = Button(root, text="Delete Record", command=delete)
    delete_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=124)

    # Exit button
    exit_button = Button(root, text="EXIT", font=('', 10), bg="#15d3ba",
                         relief=RIDGE,
                         height=1, width=15, fg="red", anchor="center", command=close)
    exit_button.grid(row=4, column=3, padx=10, pady=10)

    root.mainloop()


if __name__ == '__main__':
    check_out_ui()
