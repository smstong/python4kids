from tkinter import *

root=Tk()
var = IntVar()
Checkbutton(text="Enabled", variable=var).pack()
var.set(1)

var2 = StringVar(root,'green')
for i in ['red','green','blue']:
    Radiobutton(width=8, text=i, value=i, variable=var2).pack()

mainloop()

print(var2.get())
