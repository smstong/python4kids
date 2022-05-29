from tkinter import *
from quitter import Quitter

def fetch():
    print('Input => %s' % ent.get()) # get content in entry(string)
    print(var.get())

root = Tk()
ent = Entry(root)
ent.delete(0, END)         # clear all content in entry
ent.insert(0, 'Type words here') # set content in entry
ent.pack(side=TOP, fill=X)

var = IntVar()
ent.config(textvariable=var)
var.set('Enter an int')

ent.focus()
ent.bind('<Return>', lambda event: fetch())
btn=Button(root, text='Fetch', command=fetch)
btn.pack(side=LEFT)
Quitter(root).pack(side=RIGHT)
root.mainloop()
