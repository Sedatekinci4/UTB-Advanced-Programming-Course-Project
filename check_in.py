from tkinter import *
from tkinter import messagebox
import sqlite3
import main

room_number_taken = []


class CheckIn:
    def __init__(self, root):
        self.root = root
        pad = 400
        self.root.title("CHECK IN SYSTEM")
        self.root.geometry(
            "{1}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad)
        )

        self.top = LabelFrame(self.root)
        self.top.pack(side="top")

        self.bottom = Frame(self.root)
        self.bottom.pack(side="top")

        self.deep = Frame(self.root)
        self.deep.pack(side="bottom")

        self.checkbox = Frame(self.root)
        self.checkbox.pack(side="top")

        # Top title that shows which operation we are doing
        self.label = Label(self.top, font=('Times', 50, 'bold'), text="CHECK IN", fg="#34A2FE", anchor="center")
        self.label.grid(row=0, column=3, padx=10, pady=20)

        # asking for a name entry
        self.name_label = Label(self.bottom, font=('Times', 20, 'bold'), text="ENTER YOUR NAME :", fg="#15d3ba",
                                anchor="w")
        self.name_label.grid(row=0, column=2, padx=10, pady=20)
        self.name_var = StringVar()

        self.name_entry = Entry(self.bottom, width=50, textvar=self.name_var)
        self.name_entry.grid(row=0, column=3, padx=10, pady=20)

        # address label
        self.address_label = Label(self.bottom, font=('Times', 20, 'bold'), text="ENTER YOUR ADDRESS :", fg="#15d3ba",
                                   anchor="w")
        self.address_label.grid(row=1, column=2, padx=10, pady=20)

        # text enter field
        self.address_var = StringVar()
        self.address_entry = Entry(self.bottom, width=50, textvar=self.address_var)
        self.address_entry.grid(row=1, column=3, padx=10, pady=20)

        # mobile label

        self.mobile_label = Label(self.bottom, font=('Times', 20, 'bold'), text="ENTER YOUR MOBILE NUMBER :",
                                  fg="#15d3ba",
                                  anchor="w")
        self.mobile_label.grid(row=2, column=2, padx=10, pady=20)

        # text enter field
        self.mobile_var = IntVar()
        self.mobile_entry = Entry(self.bottom, width=50, text=self.mobile_var)
        self.mobile_entry.grid(row=2, column=3, padx=10, pady=20)

        room_list = [1, 2, 3, 4]

        variable = Variable(root)
        variable.set("Choose the room")
        self.rooms = OptionMenu(root, variable, *room_list)
        self.rooms.pack()

        # number of days label
        self.days_label = Label(self.bottom, font=('Times', 20, 'bold'), text="ENTER NUMBER OF DAYS TO STAY :",
                                fg="#15d3ba",
                                anchor="w")
        self.days_label.grid(row=3, column=2, padx=10, pady=20)

        # text enter field
        self.days_var = IntVar()
        self.days_entry = Entry(self.bottom, width=50, text=self.days_var)
        self.days_entry.grid(row=3, column=3, padx=10, pady=20)

        # Back button
        # self.back_button = Button(self.deep, font=('Times', 20, 'bold'), text="BACK",bg="#15d3ba",
        #                           fg="black",
        #                           anchor="w")
        # self.back_button.grid(row=0, column=0, padx=10, pady=10)

        def submit_info():
            global ans
            name = self.name_entry.get()
            address = self.address_entry.get()
            room = self.rooms

            while True:
                self.h = str(self.mobile_entry.get())
                if self.h.isdigit() == True and len(self.h) != 0 and len(self.h) == 10:
                    mobile = self.h
                    ans = TRUE
                    break
                else:
                    ans = False
                    messagebox.showerror("ERROR", "PLEASE ENTER 10 DIGIT MOBILE NUMBER")
                    break

            while True:
                self.h = str(self.days_entry.get())
                if self.h.isdigit():
                    days = self.h
                    ans1 = True
                    break
                else:
                    ans1 = False
                    messagebox.showerror("ERROR", "NUMBER OF DAYS CANNOT BE VARIABLE")
                    break

            if ans == TRUE and ans1 == True:
                conn = sqlite3.connect('Hotel.db')
                with conn:
                    cursor = conn.cursor()
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS Hotel (Fullname TEXT,Address TEXT,mobile_number NUMBER,number_days '
                    'NUMBER)')
                cursor.execute('INSERT INTO Hotel (FullName,Address,mobile_number,number_days) '
                               'VALUES(?,?,?,?)', (name, address, mobile, days))
                conn.commit()
                with conn:
                    cursor.execute("SELECT * FROM Hotel")
                    print(cursor.fetchall())
            room_number()
            self.name_var.set('')
            self.address_var.set('')
            self.days_var.set('')
            self.mobile_var.set('')

        def room_number():
            room_number_taken.append(self.rooms)
            print(room_number_taken)

        def reset():
            self.rooms.destroy()
            variable = StringVar(root)
            variable.set("Choose the room")
            self.rooms = OptionMenu(root, variable, *room_list)
            self.rooms.pack()
            # self.room_number_var = random.choice(roomnumber)
            # self.rooms.selection_clear(root, variable)
            # self.rooms.insert(0, self.room_number_var)

            self.name_entry.delete(0, END)
            self.name_entry.insert(0, "")

            self.mobile_entry.delete(0, END)
            self.mobile_entry.insert(0, "")

            self.address_entry.delete(0, END)
            self.address_entry.insert(0, "")

            self.days_entry.delete(0, END)
            self.days_entry.insert(0, "")

            # create submit button

        self.submit_button = Button(self.deep, text="SUBMIT", font=('', 15), bg="#15d3ba", relief=RIDGE, height=2,
                                    width=15,
                                    fg="black", anchor="center", command=submit_info)
        self.submit_button.grid(row=5, column=1, padx=10, pady=10)

        # back to home page
        self.back_home_button = Button(self.deep, text="HOME", font=('', 15), bg="#15d3ba", relief=RIDGE, height=2,
                                       width=15,
                                       fg="black", anchor="center", command=main.home_ui)
        self.back_home_button.grid(row=5, column=2, padx=10, pady=10)

        Button(self.deep, text="RESET", font=('', 15), bg="#15d3ba", relief=RIDGE, height=2, width=15, fg="black",
               anchor="center", command=reset).grid(row=5, column=3, padx=10, pady=10)


def check_in_ui():
    root = Tk()
    application = CheckIn(root)
    root.mainloop()


if __name__ == '__main__':
    check_in_ui()
