import tkinter as tk


class GuiOutput(tk.Frame):
    def __init__(self, parent=None, **options):
        tk.Frame.__init__(self, parent, **options)
        self.pack()
        self.lbl = tk.Label(self, text="")
        self.lbl.pack()

    def write(self, data):
        self.lbl['text'] += data

import sys
print("Before")
sys.stdout = GuiOutput()
print("After")

def onClick():
    print("clicked")
    
tk.Button(text="Click", command=onClick).pack()
tk.mainloop()
