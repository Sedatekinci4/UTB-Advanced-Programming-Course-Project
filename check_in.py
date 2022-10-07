from tkinter import *

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

        self.checkbox = Frame(self.root)
        self.checkbox.pack(side="top")

        # Top title that shows which operation we are doing
        self.label = Label(self.top, font=('Times', 50, 'bold'), text="CHECK IN", fg="#34A2FE", anchor="center")
        self.label.grid(row=0, column=3, padx=10, pady=10)

        # asking for a name entry
        self.name_label = Label(self.bottom, font=('Times', 20, 'bold'), text="ENTER YOUR NAME :", fg="#15d3ba",
                                anchor="w")
        self.name_label.grid(row=0, column=2, padx=10, pady=10)
        self.name_var = StringVar()

        self.name_entry = Entry(self.bottom, width=50, textvar=self.name_var)
        self.name_entry.grid(row=0, column=3, padx=10, pady=10)

        # address label
        self.address_label = Label(self.bottom, font=('Times', 20, 'bold'), text="ENTER YOUR ADDRESS :", fg="#15d3ba",
                                   anchor="w")
        self.address_label.grid(row=1, column=2, padx=10, pady=10)

        # text enter field
        self.address_var = StringVar()
        self.address_entry = Entry(self.bottom, width=50, textvar=self.address_var)
        self.address_entry.grid(row=1, column=3, padx=10, pady=10)

        # mobile label

        self.mobile_label = Label(self.bottom, font=('Times', 20, 'bold'), text="ENTER YOUR MOBILE NUMBER :",
                                  fg="#15d3ba",
                                  anchor="w")
        self.mobile_label.grid(row=2, column=2, padx=10, pady=10)

        # text enter field
        self.mobile_var = IntVar()
        self.mobile_entry = Entry(self.bottom, width=50, text=self.mobile_var)
        self.mobile_entry.grid(row=2, column=3, padx=10, pady=10)

        # number of days label
        self.days_label = Label(self.bottom, font=('Times', 20, 'bold'), text="ENTER NUMBER OF DAYS TO STAY :",
                                fg="#15d3ba",
                                anchor="w")
        self.days_label.grid(row=3, column=2, padx=10, pady=10)

        # text enter field
        self.days_var = IntVar()
        self.days_entry = Entry(self.bottom, width=50, text=self.days_var)
        self.days_entry.grid(row=3, column=3, padx=10, pady=10)

        variable = StringVar(root)
        w = OptionMenu(root, variable, "one", "two", "three")
        w.pack()


def check_in_ui():
    root = Tk()
    application = CheckIn(root)
    root.mainloop()

if __name__ == '__main__':
    check_in_ui()