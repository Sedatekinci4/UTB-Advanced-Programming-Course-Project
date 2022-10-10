from tkinter import *
import sqlite3
from tkinter import messagebox


def check_in_ui():
    root = Tk()
    root.title("SEDAT HOTEL CHECK IN")
    root.geometry("500x500")

    # databases

    # Create a db or connect to one

    def close_it():
        root.destroy()

    # Create submit function for databases
    def submit():
        # Create a db or connect to one
        conn = sqlite3.connect("Hotel.db")

        # Create a cursor
        c = conn.cursor()

        # Insert into table
        c.execute("INSERT INTO customers VALUES (:f_name, :l_name, :address, :number, :room_number)",
                  {
                      'f_name': f_name.get(),
                      'l_name': l_name.get(),
                      'address': address.get(),
                      'number': number.get(),
                      'room_number': room_number.get()
                  })

        # Commit change
        conn.commit()

        # close connection
        conn.close()

        # Clear the text boxes
        f_name.delete(0, END)
        l_name.delete(0, END)
        address.delete(0, END)
        number.delete(0, END)
        room_number.delete(0, END)

        messagebox.showinfo("information", "Check in done succesfully")

    # Create tet boxes
    f_name = Entry(root, width=40, borderwidth=10)
    f_name.grid(row=0, column=1, padx=20)
    l_name = Entry(root, width=40, borderwidth=10)
    l_name.grid(row=1, column=1)
    address = Entry(root, width=40, borderwidth=10)
    address.grid(row=2, column=1)
    number = Entry(root, width=40, borderwidth=10)
    number.grid(row=3, column=1)
    room_number = Entry(root, width=40, borderwidth=10)
    room_number.grid(row=4, column=1)

    # Create Box labels
    f_name_label = Label(root, text="First Name")
    f_name_label.grid(row=0, column=0)
    l_name_label = Label(root, text="Last Name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(root, text="Address")
    address_label.grid(row=2, column=0)
    number_label = Label(root, text="Phone No")
    number_label.grid(row=3, column=0)
    room_number_label = Label(root, text="Room No")
    room_number_label.grid(row=4, column=0)

    # Create a submit button
    submit_btn = Button(root, text="Add record to Database", command=submit)
    submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # Exit button
    exit_button = Button(root, text="EXIT", font=('', 10), bg="#15d3ba",
                         relief=RIDGE,
                         height=1, width=15, fg="red", anchor="center", command=close_it)
    exit_button.grid(row=7, column=2, padx=10, pady=10)

    root.mainloop()


if __name__ == '__main__':
    check_in_ui()
