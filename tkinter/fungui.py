import tkinter as tk
import random

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'cyan', 'purple']
fontSize = 12

def onSpam():
    popup = tk.Toplevel()
    color = random.choice(colors)
    tk.Label(popup, text="Popup", bg='black', fg=color).pack(fill=tk.BOTH)
    mainLabel.config(fg=color)

def onFlip():
    mainLabel.config(fg=random.choice(colors))
    main.after(250, onFlip)

def onGrow():
    global fontSize
    fontSize += 5
    mainLabel.config(font=('arial', fontSize, 'italic'))
    main.after(100, onGrow)

main = tk.Tk()
mainLabel = tk.Label(main, text='Fun Gui!', relief=tk.RAISED)
mainLabel.config(font=('arial', 12, 'italic'), fg='cyan', bg='navy')
mainLabel.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)
tk.Button(main, text='spam', command=onSpam).pack(fill=tk.X)
tk.Button(main, text='flip', command=onFlip).pack(fill=tk.X)
tk.Button(main, text='grow', command=onGrow).pack(fill=tk.X)

main.mainloop()
