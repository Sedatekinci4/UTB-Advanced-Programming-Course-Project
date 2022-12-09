from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk


def house_keeper_ui():
    def close_file():
        root.destroy()

    def clear_keeper():
        keeper_clear_oid = "v"
        # Create a db or connect to one
        conn = sqlite3.connect("Hotel.db")
        # Create a cursor
        c = conn.cursor()
        keeper_clear_oid = variable_keeper.get()[1]
        print(keeper_clear_oid)
        if str(keeper_clear_oid) == "v":
            messagebox.showwarning('SUCCESS', 'no housekeeper selected!!')
            return
        new_room_no = 0
        c.execute("""UPDATE keepers SET
                            Room_no = :Room_no
                            WHERE oid = :oid""",
                  {
                      'Room_no': new_room_no,
                      'oid': keeper_clear_oid
                  })
        # Commit change
        conn.commit()

        # close connection
        conn.close()
        messagebox.showinfo('SUCCESS', 'You have successfully called the housekeeper!!')
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
            if str(customer[7]) == str(variable.get()[1]):
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
                record[4]) + '\t' + "OID->  " + str(record[7]) + "\n"

        query_label = Label(root, text=print_records)
        query_label.grid()

        # Commit change
        conn.commit()

        # close connection
        conn.close()

    root = Tk()
    root.geometry("500x500")
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
        customer.insert(0, [record[7], record[0], record[1], record[4]])
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

    variable_keeper = StringVar(root)
    variable_keeper.set("Available HouseKeepers")  # default value

    w = OptionMenu(root, variable_keeper, *keeper)
    w.grid()

    variable = StringVar(root)
    variable.set("Who is calling the Housekeeper")  # default value

    w = OptionMenu(root, variable, *customer)
    w.grid()

    label = Label(top, font=('arial', 25, 'bold italic'), text=" ------HouseKeepingService------", fg="#34A2FE",
                  anchor="center")
    label.grid()

    # CREATE a query button
    query_btn = Button(root, text="Show customers", command=query,height=1, width=15, bg="#F7BE81")
    query_btn.grid()

    # CREATE a query button
    keeper_btn = Button(root, text="Show keepers", command=show_keeper,height=1, width=15, bg="#F7BE81")
    keeper_btn.grid()

    keeper_clear_btn = Button(top, text="Clear keepers room info", font=('', 15), bg="#34A2FE",
                              relief=RIDGE,
                              height=1, width=20, fg="black", anchor="nw", command=clear_keeper)
    keeper_clear_btn.grid()

    button = Button(root, text="SUBMIT", command=send_keeper, bg="lightgreen")
    button.grid()

    # Exit button
    exit_button = Button(top, text="EXIT", font=('', 15), bg="red", activeforeground="black",
                         relief=RIDGE,
                         height=1, width=20, fg="white", anchor="center", command=close_file)
    exit_button.grid()

    root.mainloop()


if __name__ == '__main__':
    house_keeper_ui()
