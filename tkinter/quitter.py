"""
A quit button that verifies exit requests

"""
from tkinter import *
from tkinter.messagebox import *

class Quitter(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        btnQuit = Button(self, text="Quit", command=self.quit)
        btnQuit.pack(side=LEFT, expand=YES, fill=BOTH)

    def quit(self):
        ans = askokcancel("Verify exit", "Really quit?")
        if ans:
            self.master.destroy()

if __name__ == "__main__":
    Quitter().mainloop()
