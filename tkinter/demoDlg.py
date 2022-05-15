"""
Demo for different standard/common dialogs
"""
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.colorchooser import askcolor
from tkinter.messagebox import askquestion, showerror
from tkinter.simpledialog import askfloat
import quitter

demos = {
    'Open': askopenfilename,
    'Color': askcolor,
    'Query': lambda: askquestion('Warning', "You typed 'rm *'\nConfirm?"),
    'Error': lambda: showerror("Error!", "He is dead, Jim"),
    'Input': lambda: askfloat('Entry', 'Enter score'),
    
    }

class Demo(Frame):
    def __init__(self, parent=None, **kargs):
        Frame.__init__(self, parent, **kargs)
        self.pack()
        Label(self, text="Basic demos").pack()
        for (key, value) in demos.items():
            Button(self, text=key,
                   command=(lambda fun=value: print('returned:', fun()))).pack(
                       side=TOP, fill=BOTH)
        quitter.Quitter(self).pack(side=TOP, fill=BOTH)


if __name__ == '__main__':
    Demo().mainloop()
