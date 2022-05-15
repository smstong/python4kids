import tkinter as tk
import random
import glob

imgdir = './images/'


class ButtonPicsDemo(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.pack()
        self.lbl = tk.Label(self, text="none", bg='blue', fg='red')
        self.pix = tk.Button(self, text="Press me", command=self.draw, bg='white')
        self.lbl.pack(fill=tk.BOTH)
        self.pix.pack(pady=10)
        files = glob.glob(imgdir + "*.gif")
        print(files)
        self.images = [(x, tk.PhotoImage(file=x)) for x in files]

    def draw(self):
        name, photo = random.choice(self.images)
        self.lbl.config(text = name)
        self.pix.config(image=photo)

if __name__ == "__main__":
    ButtonPicsDemo().mainloop()
