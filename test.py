from tkinter import *
import sqlite3


def test_ui():
    def send_keeper():
        print("value is =" + variable.get())

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
            print_records += str(record[0]) + " " + str(record[1]) + " " + '\t' + str(record[4])+ '\t' + "OID->  " + str(record[6]) + "\n"

        query_label = Label(root, text=print_records)
        query_label.grid()

        # Commit change
        conn.commit()

        # close connection
        conn.close()

    root = Tk()
    root.geometry("400x400")
    root.title("SEDAT HOTEL HOUSEKEEPING TAB")

    global house_keeper
    customer = []
    database = "Hotel.db"
    house_keeper = 2

    top = Frame(root)
    top.grid()

    # Create a db or connect to one
    conn = sqlite3.connect(database)
    # Create a cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *,oid FROM customers")
    records = c.fetchall()
    for record in records:
        customer.insert(0, {record[0], record[1], record[4], record[6]})
    conn.close()
    print(customer)

    variable = StringVar(root)
    variable.set("WHO IS CALLING THE HOUSEKEEPER")  # default value

    w = OptionMenu(root, variable, *customer)
    w.grid()

    label = Label(top, font=('arial', 25, 'bold italic'), text="------HouseKeeping------\nService", fg="#34A2FE",
                  anchor="center")
    label.grid()

    # CREATE a query button
    query_btn = Button(root, text="Show OID's", command=query)
    query_btn.grid()

    button = Button(root, text="SUBMIT", command=send_keeper)
    button.grid()

    # Exit button
    exit_button = Button(top, text="EXIT", font=('', 15), bg="#15d3ba",
                         relief=RIDGE,
                         height=1, width=15, fg="red", anchor="nw", command=None)
    exit_button.grid()

    root.mainloop()


if __name__ == '__main__':
    test_ui()
