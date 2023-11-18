import tkinter
from tkinter import messagebox

# WINDOW CONFIGURATION

window = tkinter.Tk()
window.title("PLD ASSIGNMENT 2")
window.geometry("600x400")
window.configure(bg="#333333")

# FUNCTIONALITIES

def login():
    print("Form Submitted")
    fullname = fullname_entry.get()
    print ("Username is '" + fullname + "'")
    age = age_entry.get()
    print ("Age is '" + age + "y/0'")
    address = address_entry.get()
    print ("Address is '" + address+ "'")
    if not fullname or not age or not address:
        messagebox.showerror(title="Form Declined", message="Please fill in all the required fields.")
    else:
        messagebox.showinfo(title="Login Success", message="Information received & saved. Thank you.")

    fullname_entry.delete(0, "end")
    age_entry.delete(0, "end")
    address_entry.delete(0, "end")
def enable_button():
    if CheckVar1.get():
        print("Verified")

CheckVar1 = tkinter.IntVar()


# FRAME
frame = tkinter.Frame(bg="#333333")

# LABELS

headingA_label = tkinter.Label(
    frame, text="CINCODE:", bg="#333333", fg="#EE4B2B", font="EngraversOldEnglishBT-Regular 30")
headingB_label = tkinter.Label(
    frame, text="Information Sheet", bg="#333333", fg="#FFFFFF", font="Cambria 27")
fullname_label = tkinter.Label(
    frame, text="Full Name:", bg="#333333", fg="#FFFFFF", font="Franklin 12 bold")
fullname_entry = tkinter.Entry(frame, font="Arial 12")
age_label = tkinter.Label(
    frame, text="Age:", bg="#333333", fg="#FFFFFF", font="Franklin 12 bold")
age_entry = tkinter.Entry(frame, font="Arial 12")
address_label = tkinter.Label(
    frame, text="Address:", bg="#333333", fg="#FFFFFF", font="Franklin 12 bold")
address_entry= tkinter.Entry(frame, font="Arial 12")
button_check = tkinter.Checkbutton(
    frame, text = "VERIFY", bg="#333333", font="Franklin 12 bold", variable = CheckVar1, onvalue = 1, offvalue = 0, command = enable_button)
submit_button = tkinter.Button(
    frame, text="SUBMIT", bg="#880808", fg="#FFFFFF", font="Franklin 12 bold", command = login)

# WIDGET POSITIONS

headingA_label.grid(row=0, column=0, sticky="news", pady=40)
headingB_label.grid(row=0, column=1)
fullname_label.grid(row=1, column=0)
fullname_entry.grid(row=1, column=1, pady= 15)
age_label.grid(row=2, column=0)
age_entry.grid(row=2, column=1, pady=15)
address_label.grid(row=3, column=0)
address_entry.grid(row=3, column=1, pady=15)
button_check.grid(row=4, column=0, columnspan=2, pady=20)
submit_button.grid(row=5, column=0, columnspan=2)


frame.pack()

window.mainloop()