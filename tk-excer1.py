from tkinter import *

window = Tk()
window.geometry("400x300")
window.title("Register")
window.configure(bg="yellow")


# add function
def add_function():
    num1 = int(fnumber_field.get())
    num2 = int(snumber_field.get())
    res = num1 + num2
    answer_field.configure(text=res)
# clear function
def clear_function():
    fnumber_field.delete(0, 'end')
    snumber_field.delete(0, 'end')
    answer_field.configure(text="")


# first number
fnumber_label = Label(window, text="First number")
fnumber_field = Entry(window)

fnumber_label.grid(row=0, column=0)
fnumber_field.grid(row=0, column=1)

# second number
snumber_label = Label(window, text="Second number")
snumber_field = Entry(window)

snumber_label.grid(row=1, column=0)
snumber_field.grid(row=1, column=1)

# your answer
answer_label = Label(window, text="Result :")
answer_field = Label(window, width=20)

answer_label.grid(row=2, column=0)
answer_field.grid(row=2, column=1)

# add buttons
submit = Button(window, text="Add", command=add_function)
submit.grid(row=3, column=0)

# clear button
submit = Button(window, text="Clear", command=clear_function)
submit.grid(row=3, column=1)


window.mainloop()