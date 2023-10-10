#Program No.3 Text entry
from tkinter import *
window = Tk ()
window.geometry("350x200")
window.configure(bg="cyan")
window.title("Text Entry GUI")

input_txt = Entry(window,width= 40)
input_txt.grid(column=5,row=500)

def clicked():
    res = "Hello" + input_txt.get()
    out.set(res)

btn = Button(window, text="Click Me", font=("Arial Bold",20),command=clicked)
btn.grid(column=10,row=20)
output = StringVar()
txt = Entry(window,width=30,textvariable=output)
txt.grid(column=2,row=5)
window.mainloop()
