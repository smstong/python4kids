import tkinter as tk
import random

# tkinter color value format "#RRGGBB", or "red",...
def rand_color():
    return ("#%02X%02X%02X" %
            (random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255)))

root = tk.Tk()

rows = 10
cols = 10

# Both row and column indices start from 0
# sticky=tk.NSEW makes the widget streched to fill the grid cell
for r in range(rows):
    for c in range(cols):
        tk.Label(root, text=f'({r}, {c}', bg=rand_color()).grid(
            row=r, column=c, sticky=tk.NSEW)

# Girds expandable when resizing enclosing window
# weight makes row/col expandable (default to 0/no expand)
for r in range(rows):
    root.rowconfigure(r, weight=1)
for c in range(cols):
    root.columnconfigure(c, weight=1)
    
root.mainloop()
