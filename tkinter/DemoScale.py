# Scale (ProgressBar) Demo

import tkinter as tk

root = tk.Tk()

# callback when the Scale is changed,
# both arg v and bound variable are with the same value
def onScale(v):
    print(f'arg: {v}, var: {varS1.get()}')

varS1 = tk.IntVar()
s1 = tk.Scale(root,
              label="Pic demo number",  # Label
              command=onScale,          # callback, proto (value)
              variable=varS1,           # bound variable
              from_=0, to=10,           # min, max value
              resolution = 2,           # step
              tickinterval = 2,         # tick step
              length = 200,             # widget size
              orient='horizontal')      # orientation
s1.pack()

s2 = tk.Scale(root,
              label = "sync",
              variable=varS1)  # s2 and s1 bind to the same variable
s2.pack()


root.mainloop()
