from tkinter import *
import tkinter
from tkinter import messagebox

top = Tk()
top.title("Choose your pet")
top.geometry("300x200")
top.configure(background="yellow")


def submit_command():
    info = "Your chosen pets: \n"           # You can leave it as a empty string
    if dog_var.get():
        info += "You have selected a dog!\n"
    elif cat_var.get():
        info += "You have selected a cat!\n"
    elif bird_var.get():
        info += "You have selected a bird!\n"
    elif info == "Your chosen pets: \n":        # You can leave it as a empty string
        info = "You didn't choose anything"

    messagebox.showinfo("Chosen Pets", info)


submit_button = Button(top, text="Submit", command=submit_command)

dog_var = BooleanVar()
cat_var = BooleanVar()
bird_var = BooleanVar()

dog_cb = Checkbutton(top, text="Dog", variable=dog_var, onvalue=True, offvalue=False, height=2, width=20)
cat_cb = Checkbutton(top, text="Cat", variable=cat_var, onvalue=True, offvalue=False, height=2, width=20)
bird_cb = Checkbutton(top, text="Bird", variable=bird_var, onvalue=True, offvalue=False, height=2, width=20)

dog_cb.pack()
cat_cb.pack()
bird_cb.pack()
submit_button.pack()

top.mainloop()