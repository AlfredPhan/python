#Program No.4 Check box and Radio Button and Combo box form__controls
from tkinter import * #Package used for normal graphics
from tkinter.ttk import * #Theme Tkinter (Advanced)

window = Tk()
window.geometry("400x400")
window.title("Advanced GUI Controls")
window.configure(bg="light blue")

chk_state = BooleanVar()
chk_state.set(True)

chk = Checkbutton(window,text="Choose",var=chk_state)
chk.grid(column=0,row=0)

combo = Combobox(window,width=30)
combo["values"] = ["Python","C","C++","C#","JAVA","UNIX"]
combo.current(4)
combo.grid(column=3,row=5)

selected = IntVar()
selected.set(1)

rad1 = Radiobutton(window,text="BE",value=0,variable=selected)
rad1.grid(column=4,row=1)
window.mainloop()