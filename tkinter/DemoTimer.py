import tkinter as tk
import sys

class Alarm(tk.Frame):
    def __init__(self, parent=None, msecs=1000, **options):
        tk.Frame.__init__(self, parent, **options)
        self.msecs = msecs
        self.pack()

        self.btn = tk.Button(self, text='Stop', command=lambda: sys.exit(0))
        self.btn.pack()
        self.btn.config(bg='navy', fg='white', bd=8)
        self.repeat()

    def repeat(self):
        self.bell()
        self.btn.flash()
        self.after(self.msecs, self.repeat)


if __name__ == '__main__':
    Alarm().mainloop()
