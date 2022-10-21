from tkinter import *
import sqlite3
from tkinter import messagebox


def order_ui():
    root = Tk()
    root.title("ORDERS")
    root.geometry("500x500")

    top = Frame(root)
    top.pack(side="top")

    side_left = Frame(root)
    side_left.pack(side="top", anchor="nw")

    # Title
    label = Label(top, font=('arial', 30, 'bold italic'), text="----------ORDERS----------", fg="#34A2FE",
                  anchor="center")
    label.grid(row=0, column=0)

    # Hamburger button
    hamburger_button = Button(side_left, text="HAMBURGER MENU ---- $10\nHamburger(100g)\nChips(100g)\nPepsi",
                              font=("Times", "10", "bold"), bg="#15d3ba", relief=RIDGE,
                              height=5,
                              width=25, fg="black", anchor="center", command=None)
    hamburger_button.grid(row=1, column=1, padx=30)

    # hot_dog button
    hot_dog_button = Button(side_left, text="HOT-DOG MENU --> $15\nHot-Dog(150g)\nChips(100g)\nPepsi",
                            font=("Times", "10", "bold"), bg="#15d3ba", relief=RIDGE,
                            height=5,
                            width=25, fg="black", anchor="center", command=None)
    hot_dog_button.grid(row=1, column=2, padx=30)

    root.mainloop()

    # close button to destroy the order ui
    def close_it():
        root.destroy()


if __name__ == '__main__':
    order_ui()
