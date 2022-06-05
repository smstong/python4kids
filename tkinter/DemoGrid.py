import tkinter as tk

root = tk.Tk()

table = tk.Frame(root, bg='grey')
table.pack(expand=tk.YES, fill=tk.BOTH)

rows = []
for i in range(5):
    row = []
    for j in range(4):
        ent = tk.Entry(table)
        ent.grid(row = i, column=j, sticky=tk.NSEW)
        ent.insert(tk.END, '%d,%d' %(i,j))
        row.append(ent)
    rows.append(row)

# make grid strechable
for i,_ in enumerate(rows):
    table.rowconfigure(i, weight=1)
for j, _ in enumerate(rows[0]):
    table.columnconfigure(j, weight=1)

def on_press():
    for row in rows:
        for ent in row:
            print(ent.get(), end=' ')
        print()
        
tk.Button(root, text="Print", command=on_press).pack()

tk.mainloop()
