from tkinter import *
import sys

class RedButton(Button):
    def __init__(self, parent=None, **kargs):
        Button.__init__(self, parent)
        self.config(background="red", text="Red")
        self.config(command=self.onClick)
        self.pack(expand=YES, fill=X)
        self.config(cursor="hand2")

    def onClick(self):
        print("You clicked me")
        win = Tk()
        print(win.maxsize())
    
if __name__ == '__main__':
    RedButton().mainloop()
