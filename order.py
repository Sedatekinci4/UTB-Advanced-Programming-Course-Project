from tkinter import *
import sqlite3
from tkinter import messagebox


def order_ui():
    # For closing the window
    def close():
        root.destroy()

    def select_customer():
        print("value is:" + variable.get()[1])
        # Create a db or connect to one
        conn = sqlite3.connect("Hotel.db")
        # Create a cursor
        c = conn.cursor()
        c.execute("SELECT * FROM orders")
        records = c.fetchall()

        buyer = str(cust_var.get())
        num = int(variable.get()[1])
        print(num)
        print(buyer)

        for record in records:
            if record[0] == num:
                pri = record[4]
                break

        print(pri)

        global person
        global oid_p
        # Query the database
        c.execute("SELECT * FROM customers")
        cust_records = c.fetchall()
        for x in cust_records:
            if str(x) == str(buyer):
                person = x[0]
                break

        print(person)

        c.execute("SELECT * FROM customers")
        names = c.fetchall()
        for name in names:
            print(name)
            if str(name[0]) == str(person):
                print(name[5])
                print(pri)
                s = name[5] + pri
                break
        print(s)

        c.execute("SELECT *,oid FROM customers")
        b_name = c.fetchall()
        for i in b_name:
            if str(person) == str(i[0]):
                oid_p = i[6]
                break

        print(oid_p)

        # Commit change
        conn.commit()

        # close connection
        conn.close()

        # UPDATE THE BILL
        conn = sqlite3.connect('Hotel.db')
        c = conn.cursor()

        c.execute("""UPDATE customers SET
            cost = :cost
            WHERE oid = :oid""",
                  {
                      'cost': s,
                      'oid': oid_p
                  })

        # Commit change
        conn.commit()

        # close connection
        conn.close()
        messagebox.showinfo('SUCCESS', 'You have successfully give the order, the payment will be saved to your bill')
        root.destroy()

    root = Tk()
    root.title("SEDAT HOTEL ORDERS")
    root.geometry("500x500")

    top = Frame(root)
    top.pack(side="top")

    side_left = Frame(root)
    side_left.pack(side="top", anchor="nw")

    # Title
    label = Label(top, font=('arial', 30, 'bold italic'), text="----------ORDERS----------", fg="#34A2FE",
                  anchor="center")
    label.grid(row=0, column=0)

    # Exit button
    exit_button = Button(top, text="EXIT", font=('', 15), bg="#15d3ba",
                         relief=RIDGE,
                         height=1, width=15, fg="red", anchor="nw", command=close)
    exit_button.grid(row=1, column=1)

    # Create a db or connect to one
    conn = sqlite3.connect("Hotel.db")
    # Create a cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT * FROM orders")
    records = c.fetchall()
    order_count = len(records)

    for order in range(order_count):
        order_button = Button(side_left,
                              text="Meal: " + str(records[order][1]) + '\n' "Drink: " + str(
                                  records[order][2]) + '\n' + "Addition: " + str(
                                  records[order][3]) + '\n' + "Price: " + str(records[order][4]) + "$",
                              font=("Times", "10", "bold"), bg="#15d3ba", relief=RIDGE,
                              height=4,
                              width=20, fg="black", anchor="nw", command=select_customer)
        order_button.grid(row=order + 2, column=1, padx=30, pady=3)

    variable = StringVar(root)
    variable.set("SELECT THE DESIRED MENU")  # default value

    w = OptionMenu(root, variable, *records)
    w.pack()

    # button = Button(root, text="SUBMIT", command=select_customer)
    # button.pack()

    # Commit change
    conn.commit()
    # close connection
    conn.close()

    # FOR THE CUSTOMER BUTTONS
    # Create a db or connect to one
    conn = sqlite3.connect("Hotel.db")
    # Create a cursor
    c = conn.cursor()
    people = []
    # Query the database
    c.execute("SELECT Name,Surname,Room_number,Cost FROM customers")
    cust_records = c.fetchall()
    for cst in cust_records:
        people.append({cst[0], cst[1], cst[2]})
    customer_count = len(cust_records)

    for cst in range(customer_count):
        customer_button = Button(side_left,
                                 text="Name: " + str(cust_records[cst][0]) + '\n' "Surname: " + str(
                                     cust_records[cst][1]) + '\n' + "Room_NO: " + str(
                                     cust_records[cst][2]) + '\n' + "Bill: " + str(cust_records[cst][3]) + "$",
                                 font=("Times", "10", "bold"), bg="#15d3ba", relief=RIDGE,
                                 height=4,
                                 width=20, fg="black", anchor="nw", command=None)
        customer_button.grid(row=cst + 2, column=3, padx=30, pady=3)

    cust_var = StringVar(root)
    cust_var.set("SELECT THE CUSTOMER")  # default value

    w1 = OptionMenu(root, cust_var, *people)
    w1.pack()

    button = Button(root, text="SUBMIT", command=select_customer)
    button.pack()

    # Commit change
    conn.commit()

    # close connection
    conn.close()

    root.mainloop()


if __name__ == '__main__':
    order_ui()
