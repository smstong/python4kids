import tkinter as tk
import shelve

class DbUI(tk.Frame):
    def __init__(self, parent=None, **options):
        tk.Frame.__init__(self, parent, **options)
        self.table = None
        self.pack(expand=tk.YES, fill=tk.BOTH)
        
    def loadData(self, data):
        if self.table:
            self.table.forget()
            
        self.table = tk.Frame(self, bg='white')
        self.table.pack(expand=tk.YES, fill=tk.BOTH)
        
        rows = len(data)
        cols = max([len(row) for row in data])
        for row in range(rows):
            self.rowconfigure(row, weight=1)
        for col in range(cols):
            if col % 2 == 1:
                self.table.columnconfigure(col, weight=10)
            else:
                self.table.columnconfigure(col, weight=2)

        for i, (rowK, rowV) in enumerate(data.items()):
            for j, (k,v) in enumerate(rowV.items()):
                tk.Label(self.table, text=str(k)).grid(row=i, column=2*j, sticky=tk.NSEW)
                ent = tk.Entry(self.table)
                ent.grid(row=i, column=2*j+1, sticky=tk.NSEW)
                ent.insert('0', str(v))
            
if __name__ == '__main__':
    root = tk.Tk()
    ui = DbUI(root)
    
    def load_db(fname):
        db = shelve.open(fname)
        ui.loadData(db)
        db.close()
        
    tk.Button(root, text="employeeDB", command=lambda : load_db('employees')).pack()
    tk.Button(root, text="fruitDB", command=lambda: load_db('fruits')).pack()

    
    root.mainloop()
