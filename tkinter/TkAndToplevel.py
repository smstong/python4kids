from tkinter import *
## About Tk
# - A Tk window has no parent
# - You can get a default Tk without explictly creating it
# - More than 1 Tk window may be created
# - The app exits if all Tk windows are closed

## About Toplevel
# - Toplevel is similar to Tk but it has parent
# - The app still run when all Toplevel windows are closed

## FAQ

# How to get the monitor size?
root = Tk()
screenWidth, screenHeight = root.maxsize()
print(screenWidth, screenHeight)

root.geometry("%dx%d" % (screenWidth,screenHeight))
root.attributes("-fullscreen", True)

root.mainloop()
