import tkinter as tk

# Text rows start from 1, while cols start from 0.
 
root = tk.Tk()
img = tk.PhotoImage(file='images/bird.gif')

txtContent = tk.Text(root, bg='white', fg='red')
txtContent.delete('1.0', tk.END) 
txtContent.insert('1.0', "Here is the content.\nThis is second line.")
txtContent.image_create('2.2', image=img) # insert a picture at row 2 col 2
txtContent.pack(expand=tk.YES, fill=tk.BOTH)


def on_fetch():
    print(txtContent.get('1.0', tk.END))
    
tk.Button(root, text="Fetch", command=on_fetch).pack()

root.mainloop()
