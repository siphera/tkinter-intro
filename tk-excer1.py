from tkinter import *
import tkinter

window = Tk()
window.geometry("400x300")
window.title("Register")

# add function
def add_function():
    result = first_number.get() + second_number.get()
    print(result)


# clear function
def clear_function():
    print(add_function())


# exit function
def exit_function():
    print()


first_number = int()
second_number = int()
# first number
fnumber_label = Label(window, text="Please enter first number", textvariable=first_number)
fnumber_field = Entry(window)

fnumber_label.grid(row=0, column=0)
fnumber_field.grid(row=0, column=1)

# second number
snumber_label = Label(window, text="Please enter second number", textvariable=second_number)
snumber_field = Entry(window)

snumber_label.grid(row=1, column=0)
snumber_field.grid(row=1, column=1)

# your answer
answer_label = Label(window, text="Your answer")
answer_field = Entry(window)

answer_label.grid(row=2, column=0)
answer_field.grid(row=2, column=1)


# add buttons
submit = Button(window, text="Add", command=add_function)
submit.grid(row=3, column=0)

# clear button
submit = Button(window, text="Clear", command=clear_function)
submit.grid(row=3, column=1)

# exit button
submit = Button(window, text="Exit", command=exit_function)
submit.grid(row=3, column=2)

window.mainloop()