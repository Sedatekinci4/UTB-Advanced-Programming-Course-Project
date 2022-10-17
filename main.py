from tkinter import *
import check_in
import check_out
import show_customer_info
import room_info


def home_ui():
    root = Tk()
    root.title("SEDAT HOTEL HOMEPAGE")
    root.geometry("950x950")

    top = Frame(root)
    top.pack(side="top")

    bottom = Frame(root)
    bottom.pack(side="top")

    label = Label(top, font=('arial', 50, 'bold italic'), text="----------WELCOME----------", fg="#34A2FE",
                  anchor="center")
    label.grid(row=0, column=3)

    # Check in button
    check_in_button = Button(bottom, text="CHECK IN", font=("Times", "20", "bold"), bg="#15d3ba", relief=RIDGE,
                             height=2,
                             width=45, fg="black", anchor="center", command=check_in.check_in_ui)
    check_in_button.grid(row=0, column=2, padx=10, pady=10)

    # Check out button
    check_out_button = Button(bottom, text="CHECK OUT", font=("Times", "20", "bold"), bg="#15d3ba",
                              relief=RIDGE,
                              height=2, width=45, fg="black", anchor="center", command=check_out.check_out_ui)
    check_out_button.grid(row=1, column=2, padx=10, pady=10)

    # Room info button
    get_info_button = Button(bottom, text="INFORMATION OF ALL GUESTS", font=("Times", "20", "bold"),
                             bg="#15d3ba",
                             relief=RIDGE,
                             height=2, width=45, fg="black", anchor="center", command=show_customer_info.customer_info)
    get_info_button.grid(row=2, column=2, padx=10, pady=10)

    # Guest info button
    room_info_button = Button(bottom, text="INFORMATION OF ROOMS", font=("Times", "20", "bold"), bg="#15d3ba",
                              relief=RIDGE,
                              height=2, width=45, fg="black", anchor="center", command=room_info.room_info_ui)
    room_info_button.grid(row=3, column=2, padx=10, pady=10)

    # Order sth button
    order_button = Button(bottom, text="ORDERS (FOOD / DRINK)", font=("Times", "20", "bold"), bg="#15d3ba",
                          relief=RIDGE,
                          height=2, width=45, fg="black", anchor="center", command=None)
    order_button.grid(row=4, column=2, padx=10, pady=10)

    # Call housecleaning button
    house_cleaning_button = Button(bottom, text="CALL HOUSECLEANING", font=("Times", "20", "bold"),
                                   bg="#15d3ba",
                                   relief=RIDGE,
                                   height=2, width=45, fg="black", anchor="center", command=None)
    house_cleaning_button.grid(row=5, column=2, padx=10, pady=10)

    # Billing button
    billing_button = Button(bottom, text="CHECK / PAY THE BILL", font=("Times", "20", "bold"), bg="#15d3ba",
                            relief=RIDGE,
                            height=2, width=45, fg="black", anchor="center", command=None)
    billing_button.grid(row=6, column=2, padx=10, pady=10)

    # Exit button
    exit_button = Button(bottom, text="EXIT", font=('', 20), bg="#15d3ba",
                         relief=RIDGE,
                         height=2, width=45, fg="red", anchor="center", command=quit)
    exit_button.grid(row=7, column=2, padx=10, pady=10)

    root.mainloop()


if __name__ == '__main__':
    home_ui()
