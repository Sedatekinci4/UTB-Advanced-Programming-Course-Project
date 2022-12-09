from tkinter import *
import sqlite3
from tkinter import messagebox


def customer_info():
    root = Tk()
    root.geometry("600x600")
    root.title("SEDAT HOTEL CUSTOMER INFORMATION")

    def close():
        root.destroy()

    def update():
        # Create a db or connect to one
        conn = sqlite3.connect("Hotel.db")
        # Create a cursor
        c = conn.cursor()

        record_id = edit_box.get()
        c.execute("""UPDATE customers SET
            Name = :first,
            Surname = :last,
            Address = :address,
            Number = :number,
            Room_number = :room_no
            
            WHERE oid = :oid""",
                  {
                      'first': f_name_editor.get(),
                      'last': l_name_editor.get(),
                      'address': address_editor.get(),
                      'number': number_editor.get(),
                      'room_no': room_number_editor.get(),

                      'oid': record_id
                  })

        # Commit change
        conn.commit()
        # close connection
        conn.close()

        # Clear the text boxes
        f_name_editor.delete(0, END)
        l_name_editor.delete(0, END)
        address_editor.delete(0, END)
        number_editor.delete(0, END)
        room_number_editor.delete(0, END)

        messagebox.showinfo("DONE", "CUSTOMERS INFO HAS BEEN UPDATED")
        editor.destroy()
        root.destroy()

    def edit():
        def close_editor():
            editor.destroy()

        global editor
        editor = Tk()
        editor.title("EDIT CUSTOMERS")
        editor.geometry("400x400")

        global f_name_editor
        global l_name_editor
        global address_editor
        global number_editor
        global room_number_editor

        # Create tet boxes
        f_name_editor = Entry(editor, width=40, borderwidth=10)
        f_name_editor.grid(row=0, column=1, padx=20)
        l_name_editor = Entry(editor, width=40, borderwidth=10)
        l_name_editor.grid(row=1, column=1)
        address_editor = Entry(editor, width=40, borderwidth=10)
        address_editor.grid(row=2, column=1)
        number_editor = Entry(editor, width=40, borderwidth=10)
        number_editor.grid(row=3, column=1)
        room_number_editor = Entry(editor, width=40, borderwidth=10)
        room_number_editor.grid(row=4, column=1)

        # Create Box labels
        f_name_label = Label(editor, text="First Name")
        f_name_label.grid(row=0, column=0)
        l_name_label = Label(editor, text="Last Name")
        l_name_label.grid(row=1, column=0)
        address_label = Label(editor, text="Address")
        address_label.grid(row=2, column=0)
        number_label = Label(editor, text="Phone No")
        number_label.grid(row=3, column=0)
        room_number_label = Label(editor, text="Room No")
        room_number_label.grid(row=4, column=0)

        # Save button
        save_button = Button(editor, text="SAVE", font=('', 10), bg="#15d3ba",
                             relief=RIDGE,
                             height=1, width=15, fg="red", anchor="center", command=update)
        save_button.grid(row=6, column=1, padx=50)

        # Exit button
        exit_editor_button = Button(editor, text="EXIT", font=('', 10), bg="#15d3ba",
                                    relief=RIDGE,
                                    height=1, width=15, fg="red", anchor="center", command=close_editor)
        exit_editor_button.grid(row=8, column=1, pady=10)

        # Create a db or connect to one
        conn = sqlite3.connect("Hotel.db")
        # Create a cursor
        c = conn.cursor()

        record_id = edit_box.get()
        c.execute("SELECT * FROM customers WHERE oid = " + record_id)
        records = c.fetchall()
        if not records:
            print("empty")
            messagebox.showerror("Warning", "NO SUCH A CUSTOMER WITH THIS OID")
            close_editor()
            root.destroy()

        for record in records:
            f_name_editor.insert(0, record[0])
            l_name_editor.insert(0, record[1])
            address_editor.insert(0, record[2])
            number_editor.insert(0, record[3])
            room_number_editor.insert(0, record[4])

    # Create query function
    def query():
        # Create a db or connect to one
        conn = sqlite3.connect("Hotel.db")
        # Create a cursor
        c = conn.cursor()

        # Query the database
        c.execute("SELECT *,oid FROM customers")
        records = c.fetchall()
        print(records)

        # Loop through records
        print_records = ''
        for record in records:
            print_records += "First Name:  " + '\t' + str(record[0]) + '\n' \
                             + "Last Name:   " + '\t' + str(record[1]) + '\n' \
                             + "Address:     " + '\t' + str(record[2]) + '\n' \
                             + "Phone Number:" + '\t' + str(record[3]) + '\n' \
                             + "Room No:     " + '\t' + str(record[4]) + '\n' \
                             + "Bill Price:  " + '\t' + str(record[5]) + '$' + '\n' \
                             + "Dates:" + '\t' + str(record[6]) + '\n' \
                             + "Oid:         " + '\t' + str(record[7]) + '\n\n'
        query_label = Label(root, text=print_records, anchor='center')
        query_label.grid(row=4, column=0)

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
    exit_button.grid(row=2, column=2)

    # Edit box
    edit_box = Entry(root, width=40, borderwidth=10)
    edit_box.grid(row=2, column=0)

    # Edit button
    edit_button = Button(root, text="EDIT", font=('', 10), bg="#15d3ba",
                         relief=RIDGE,
                         height=1, width=15, fg="red", anchor="center", command=edit)
    edit_button.grid(row=2, column=3, padx=5)

    root.mainloop()


if __name__ == '__main__':
    customer_info()
