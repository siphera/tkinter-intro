from tkinter import *
import tkinter

window = Tk()
window.geometry("300x250")
window.title("Register")
# window.configure(background="grey")

fields = {}
# Name
name_label = Label(window, text="Name")
name_field = Entry(window)
fields['name'] = name_field

name_label.grid(row=0, column=0)
name_field.grid(row=0, column=1)

# Surname
surname_label = Label(window, text="Surname")
surname_field = Entry(window)
fields['surname'] = name_field

surname_label.grid(row=1, column=0)
surname_field.grid(row=1, column=1)


# Email
email_label = Label(window, text="Email")
email_field = Entry(window)
fields['email'] = name_field

email_label.grid(row=2, column=0)
email_field.grid(row=2, column=1)

# Contact number
contact_label = Label(window, text="Contact number")
contact_field = Entry(window)
fields['contact'] = name_field

contact_label.grid(row=3, column=0)
contact_field.grid(row=3, column=1)


# Submit button functionality
def submit_command():
    output = "User data:\n"
    for key in fields.keys():
        output += f"{key}: {fields[key].get()}\n"
    print(output)


submit = Button(window, text="Submit", command=submit_command)
submit.grid(row=4, column=0)


window.mainloop()