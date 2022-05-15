import os, sys
import tkinter as tk
from PIL.ImageTk import PhotoImage

imgdir = "images"
if len(sys.argv) > 1: imgdir = sys.argv[1]
imgfiles = os.listdir(imgdir)

main = tk.Tk()
main.title("viewer")
btnQuit = tk.Button(main, text="Quit", command=main.quit, font=("courier", 24))
btnQuit.pack()

savephotos = []

for imgfile in imgfiles:
    imgpath = os.path.join(imgdir, imgfile)
    win = tk.Toplevel()
    win.title(imgfile)
    try:
        imgobj = PhotoImage(file=imgpath)
        tk.Label(win, image=imgobj).pack()
        print(imgpath, imgobj.width(), imgobj.height())
        savephotos.append(imgobj)
    except:
        errmsg = "skiping %s\n%s" % (imgfile, sys.exc_info()[1])
        tk.Label(win, text=errmsg).pack()

main.mainloop()
