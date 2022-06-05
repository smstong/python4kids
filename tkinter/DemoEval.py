import tkinter as tk
from math import *

root = tk.Tk()

ent = tk.Entry(root)
ent.pack()
ent.delete('0', tk.END)
ent.insert('0', "sin(0.2)")

lbl = tk.Label(root)
lbl.pack()


def on_eval():
    lbl.configure(text=eval(ent.get()))

tk.Button(root, text="eval", command=on_eval).pack()
tk.mainloop()
