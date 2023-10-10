#Program No.2 Text boxes, label and button 
from tkinter import *

window = Tk()
window.geometry("400x400")
window.configure(bg='blue')
window.title("COMP1753 GUI2")
input_text = Entry(window, width=20)
input_text.grid(column=20, row=10)

def clicked():
    lbl.configure(text="Button was clicked")
    lbl.grid(column=50,row=6)
    res = "Hello" + input_text.get()
    lbl.configure(text=res)

lbl = Label(window, text= "Hello", font=("Arial Bold", 20))
lbl.grid(column=1, row=2) #FOR doing in the first right corner


lb2 = Label(window, text="Hello", font=("Arial Bold", 20))
lb2.grid(column=2, row=4)

lb3 = Label(window, text="Everyone", font=("Arial Bold", 20))
lb3.grid(column=2, row=4)


btn1 = Button(window, text="Click Me", font=("Arial Bold", 30), bg="yellow", fg="black", command=clicked)
btn1.grid(column=100, row=100)

window.mainloop()