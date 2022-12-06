from tkinter import *
import sqlite3
from tkinter import messagebox


def house_keeper_ui():
    def close_file():
        root.destroy()

    def show_keeper():
        # Create a db or connect to one
        conn = sqlite3.connect("Hotel.db")
        # Create a cursor
        c = conn.cursor()

        c.execute("SELECT *, oid FROM keepers")
        keepers = c.fetchall()
        print(keepers)

        # Loop through records
        print_keepers = ''
        for keeper in keepers:
            print_keepers += str(keeper[0]) + '\t' + " Room: " + str(keeper[1]) + " " + '\t' + "OID->  " + str(
                keeper[2]) + "\n"

        query_label = Label(root, text=print_keepers)
        query_label.grid()
        conn.close()

    def send_keeper():
        print("Caller customer oid is= " + variable.get()[1])
        print("Selected keeper oid is= " + variable_keeper.get()[1])
        keeper_oid = variable_keeper.get()[1]
        # Create a db or connect to one
        conn = sqlite3.connect("Hotel.db")
        # Create a cursor
        c = conn.cursor()

        c.execute("SELECT *, oid FROM keepers")
        keepers = c.fetchall()
        print(keepers)

        c.execute("SELECT *,oid FROM customers")
        customers = c.fetchall()
        for customer in customers:
            if str(customer[6]) == str(variable.get()[1]):
                new_room_no = customer[4]
                print(new_room_no)

        c.execute("""UPDATE keepers SET
                    Room_no = :Room_no
                    WHERE oid = :oid""",
                  {
                      'Room_no': new_room_no,
                      'oid': keeper_oid
                  })
        # Commit change
        conn.commit()

        # close connection
        conn.close()
        messagebox.showinfo('SUCCESS', 'You have successfully called the housekeeper!!')
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
            print_records += str(record[0]) + " " + str(record[1]) + " " + '\t' + str(
                record[4]) + '\t' + "OID->  " + str(record[6]) + "\n"

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
    keeper = []
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
        customer.insert(0, [record[6], record[0], record[1], record[4]])
    conn.close()
    print(customer)

    # Create a db or connect to one
    conn = sqlite3.connect(database)
    # Create a cursor
    c = conn.cursor()

    c.execute("SELECT *,oid FROM keepers")
    records = c.fetchall()
    for record in records:
        keeper.insert(0, [record[2], record[0], record[1]])
    conn.close()
    print(customer)

    variable_keeper = StringVar(root)
    variable_keeper.set("Available HouseKeepers")  # default value

    w = OptionMenu(root, variable_keeper, *keeper)
    w.grid()

    variable = StringVar(root)
    variable.set("Who is calling the Housekeeper")  # default value

    w = OptionMenu(root, variable, *customer)
    w.grid()

    label = Label(top, font=('arial', 25, 'bold italic'), text=" ------HouseKeeping------\nService", fg="#34A2FE",
                  anchor="center")
    label.grid()

    # CREATE a query button
    query_btn = Button(root, text="Show customers", command=query)
    query_btn.grid()

    # CREATE a query button
    keeper_btn = Button(root, text="Show keepers", command=show_keeper)
    keeper_btn.grid()

    button = Button(root, text="SUBMIT", command=send_keeper)
    button.grid()

    # Exit button
    exit_button = Button(top, text="EXIT", font=('', 15), bg="#15d3ba",
                         relief=RIDGE,
                         height=1, width=5, fg="red", anchor="nw", command=close_file)
    exit_button.grid()

    root.mainloop()


if __name__ == '__main__':
    house_keeper_ui()
