from tkinter import *
import math

class Cal(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        
        self.btns = [
            ["(", ")", "**", "AC"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ]
        self.font = ('Times', 20, 'bold')
        
        self.init_ui()
        
    def init_ui(self):
        self.pack(expand=YES, fill=BOTH)
        
        ent = Entry(self, bg='white', fg='green', font=self.font)
        ent.pack(expand=YES, fill=BOTH)
        self.entVar = StringVar()
        ent.configure(textvariable=self.entVar)
        
        table = Frame(self)
        table.pack(expand=YES, fill=BOTH)
        
        for i,_ in enumerate(self.btns):
            table.rowconfigure(i, weight=1)
            
        for j,_ in enumerate(self.btns[0]):
            table.columnconfigure(j, weight=1)
            
        for i, row in enumerate(self.btns):
            for j, v in enumerate(row):
                btn = Button(table, text=v, font=self.font, bd=5, fg='grey')
                btn.grid(row=i, column=j, sticky=NSEW)
                btn.configure(command=lambda v=v: self.onClick(v))
        self.table = table
        
    def onClick(self, v):
        if v == '=':
            try:
                result = eval(self.entVar.get())
            except:
                result = "ERROR"
            finally:
                self.entVar.set(result)
        elif v == 'AC':
            self.entVar.set('')
            
        else:
            self.entVar.set(self.entVar.get() + v)
        
if __name__ == '__main__':
    Cal().mainloop()
