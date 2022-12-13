from tkinter import *
import sqlite3
from tkinter import messagebox
from datetime import datetime

oids = []

def bill_ui():
    def close_it():
        root.destroy()

    def print_bill(value):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        bill = ''
        discount = value/10
        discount_f = float("{0:.2f}".format(discount))
        kdv = value/15
        kdv_f = float("{0:.2f}".format(kdv))
        net_total = value - discount
        net_total_f = float("{0:.2f}".format(net_total))
        grand_total = net_total + kdv
        grand_total_f = float("{0:.2f}".format(grand_total))

        bill += "\n\n             Sedat Hotel\n--------------------------------------\nDate: "+dt_string+"\n--------------------------------------\nItems              Qty          Total\n--------------------------------------\nAccomodation         1            "+str(value)+"\n\n--------------------------------------\nDiscount @10%                   "+str(discount_f) + "\n                        --------------\nNet Total                       "+str(net_total_f) + "\nKDV                             "+ str(kdv_f)+"\n--------------------------------------\nGrand Total                     "+str(grand_total_f)+ "\n--------------------------------------\n           # ITEMS SOLD 1\n    TC# 1810 8412 0447 6524 7000\n   Thank You for Shopping With Us!\n       "+dt_string+"\n     ✯✯✯ CUSTOMER COPY ✯✯✯"
        print(bill)
        messagebox.showinfo("Success", "You've succesfully paid\nGood days")

    # Create function to delete a record
    def delete():
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
            oids.append(str(record[7]))

        for oid in oids:
            if str(oid) == str(oid_for_pay.get()):
                c.execute("SELECT Cost from customers WHERE oid=" + str(oid_for_pay.get()))
                bill_cost = c.fetchall()
                print(bill_cost[0][0])
                val = int(bill_cost[0][0])
                print_bill(val)
                c.execute("DELETE from customers WHERE oid=" + oid_for_pay.get())
                # Commit change
                conn.commit()

                # close connection
                conn.close()
                messagebox.showinfo("Checked out", "The person that pays has checked out form the system!")
                root.destroy()
                return

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
        print_records = '  --Person ----- Room no --- Cost ----- OID---\n'
        for record in records:
            print_records += str(record[0]) + " " + str(record[1]) + " " + '\t' + str(
                record[4]) + '\t' + str(record[5]) + ' $\t' + "OID->  " + str(record[7]) + "\n"

        query_label = Label(root, text=print_records)
        query_label.grid()

        # Commit change
        conn.commit()

        # close connection
        conn.close()

    root = Tk()
    root.geometry("500x500")
    root.title("SEDAT HOTEL BILLING TAB")

    top = Frame(root)
    top.grid()

    label = Label(top, font=('arial', 25, 'bold italic'), text=" ----------- Billing Service ----------", fg="#34A2FE",
                  anchor="center")
    label.grid()

    oid_for_pay = Entry(top, width=10, borderwidth=10)
    oid_for_pay.grid(row=1, column=0)

    button = Button(top, text="SUBMIT PAYMENT", command=delete, bg="lightgreen")
    button.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=15)

    # CREATE a query button
    query_btn = Button(top, text="Show customers and costs", command=query, height=1, width=15, bg="#F7BE81")
    query_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=20)

    # Exit button
    exit_button = Button(top, text="EXIT", font=('', 15), bg="red", activeforeground="black",
                         relief="ridge",
                         height=1, width=20, fg="white", anchor="center", command=close_it)
    exit_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=15)

    root.mainloop()


if __name__ == '__main__':
    bill_ui()
