from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Trip Login")
root.geometry("600x500")
root.config(bg="Grey")

# Labels and Entry
head_lab = Label(root, text="Please enter login details", bg="Grey", font=("Consolas 15 bold"))
head_lab.place(x=120, y=10)
username_lab = Label(root, text="Username", bg="Grey", font=("Consolas 15 bold"))
username_lab.place(x=200, y=100)
username_entry = Entry(root)
username_entry.place(x=150, y=125, height=30, width=220)
password_lab = Label(root, text="Password", bg="Grey", font=("Consolas 15 bold"))
password_lab.place(x=200, y=180)
password_entry = Entry(root, show="*")
password_entry.place(x=150, y=205, width=220, height=30)

names = ["Zipho", "Masi", "Mzwai", "Thando"]
password = "1111", "2222", "3333", "4444"


# Functions
def login():
    if username_entry.get() != names or password_entry.get() != password:
        messagebox.showinfo(title="Out-put", message="Go Through")
        root.destroy()
        import exception_form


login_btn = Button(root, text="Login", borderwidth="10", command=login, font=("Consolas 13 bold"), bg="Grey", fg="Red")
login_btn.place(x=200, y=240)


root.mainloop()