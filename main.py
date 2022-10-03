from tkinter import *
import os


class Hotel:
    def __init__(self, root):
        self.root = root
        pad = 100
        self.root.title("SEDAT HOTEL MANAGEMENT SYSTEM")
        self.root.geometry(
            "{1}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad)
        )

        top = Frame(self.root)
        top.pack(side="top")

        bottom = Frame(self.root)
        bottom.pack(side="top")

        self.label = Label(top, font=('arial', 50, 'bold italic'), text="----------WELCOME----------", fg="#34A2FE",
                           anchor="center")
        self.label.grid(row=0, column=3)

        # Check in button
        self.check_in_button = Button(bottom, text="CHECK IN", font=("Times", "20", "bold"), bg="#15d3ba", relief=RIDGE,
                                      height=2,
                                      width=45, fg="black", anchor="center", command=None)
        self.check_in_button.grid(row=0, column=2, padx=10, pady=10)

        # Check out button
        self.check_out_button = Button(bottom, text="CHECK OUT", font=("Times", "20", "bold"), bg="#15d3ba",
                                       relief=RIDGE,
                                       height=2, width=45, fg="black", anchor="center", command=None)
        self.check_out_button.grid(row=1, column=2, padx=10, pady=10)

        # Room info button
        self.room_info_button = Button(bottom, text="INFORMATION OF ALL GUESTS", font=("Times", "20", "bold"),
                                       bg="#15d3ba",
                                       relief=RIDGE,
                                       height=2, width=45, fg="black", anchor="center", command=None)
        self.room_info_button.grid(row=2, column=2, padx=10, pady=10)

        # Guest info button
        self.get_info_button = Button(bottom, text="INFORMATION OF ROOMS", font=("Times", "20", "bold"), bg="#15d3ba",
                                      relief=RIDGE,
                                      height=2, width=45, fg="black", anchor="center", command=None)
        self.get_info_button.grid(row=3, column=2, padx=10, pady=10)

        # Order sth button
        self.order_button = Button(bottom, text="ORDERS (FOOD / DRINK)", font=("Times", "20", "bold"), bg="#15d3ba",
                                   relief=RIDGE,
                                   height=2, width=45, fg="black", anchor="center", command=None)
        self.order_button.grid(row=4, column=2, padx=10, pady=10)

        # Call housecleaning button
        self.house_cleaning_button = Button(bottom, text="CALL HOUSECLEANING", font=("Times", "20", "bold"),
                                            bg="#15d3ba",
                                            relief=RIDGE,
                                            height=2, width=45, fg="black", anchor="center", command=None)
        self.house_cleaning_button.grid(row=5, column=2, padx=10, pady=10)

        # Billing button
        self.billing_button = Button(bottom, text="CHECK / PAY THE BILL", font=("Times", "20", "bold"), bg="#15d3ba",
                                     relief=RIDGE,
                                     height=2, width=45, fg="black", anchor="center", command=None)
        self.billing_button.grid(row=6, column=2, padx=10, pady=10)

        # Exit button
        self.billing_button = Button(bottom, text="EXIT", font=('', 20), bg="#15d3ba",
                                     relief=RIDGE,
                                     height=2, width=45, fg="red", anchor="center", command=quit)
        self.billing_button.grid(row=7, column=2, padx=10, pady=10)


def home_ui():
    root = Tk()
    application = Hotel(root)
    root.mainloop()


if __name__ == '__main__':
    home_ui()
