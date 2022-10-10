from tkinter import *
import sqlite3


def customer_info():
    root = Tk()
    root.geometry("400x400")
    root.title("CUSTOMER INFORMATION")

    def close():
        root.destroy()

    # Create query function
    def query():
        # Create a db or connect to one
        conn = sqlite3.connect("Hotel.db")
        # Create a cursor
        c = conn.cursor()

        # Query the database
        c.execute("SELECT * FROM customers")
        records = c.fetchall()
        print(records)

        # Loop through records
        print_records = ''
        for record in records:
            print_records += "First Name:" + '\t' + str(record[0]) + '\n' \
                             + " Last Name:" + '\t' + str(record[1]) + '\n' \
                             + " Address:" + '\t' + str(record[2]) + '\n' \
                             + " Phone Number:" + '\t' + str(record[3]) + '\n' \
                             + " Room No:" + '\t' + str(record[4]) + '\n\n'

        query_label = Label(root, text=print_records)
        query_label.grid(row=3, column=0)

        # Commit change
        conn.commit()

        # close connection
        conn.close()

    # CREATE a query button
    query_btn = Button(root, text="Show Records", command=query)
    query_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=124)

    # Exit button
    exit_button = Button(root, text="EXIT", font=('', 10), bg="#15d3ba",
                         relief=RIDGE,
                         height=1, width=15, fg="red", anchor="center", command=close)
    exit_button.grid(row=2, column=1)

    root.mainloop()


if __name__ == '__main__':
    customer_info()
