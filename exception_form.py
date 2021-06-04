from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Exception Handling")
root.geometry("500x500")
root.config(bg="black")

# Labels and Entry
amount_lab = Label(root, text="Enter your amount in your account", bg="black", fg="lightblue", font=("Consolas 15 bold"))
amount_lab.place(x=20, y=10)
amount_entry = Entry(root)
amount_entry.place(x=25, y=40, width=220, height=30)


# Function and Button
def status():
    funds = amount_entry.get()
    try:
        funds = int(funds)
        if funds < 3000:
            messagebox.showerror(title="Status Feedback", message="Please deposit more funds for this excursion.")
        else:
            messagebox.showinfo(title="Status Feedback", message="Congratulations. You qualify for the trip to Malaysia")
    except ValueError:
        messagebox.showerror(title="Status Feedback", message="Error,Please insert a number.")


check_btn = Button(root, text="Check qualification", command=status, bg="Black", fg="Lightblue", borderwidth="30", font=("Consolas 13 bold"))
check_btn.place(x=25, y=100)
root.mainloop()