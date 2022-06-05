import tkinter as tk
class Demo(tk.Frame):
    def __init__(self, parent=None, **kargs):
        tk.Frame.__init__(self, parent, **kargs)
        self.pack()


if __name__ == '__main__':
    Demo().mainloop()
