from tkinter import *

win = Tk()
win.title("GUI APP")
win.geometry("300x300")
win.configure(bg="green")


def test_function():
    mytext="siphenkosi"
    text_input.insert(9, mytext)
    return None


my_label = Label(win, text="Greetings to you all", relief="solid")
my_label.pack()
text_input = Entry(win, width=30)
text_input.pack()
my_button = Button(win, text="Click me", bg="blue", command=test_function)
my_button.pack()


win.mainloop()