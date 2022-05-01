import tkinter as tk
root = tk.Tk()
root.title("canvas tags")
root.geometry("800x600")

cv = tk.Canvas(root)
cv.config(bg='yellow')
cv.pack(expand=tk.YES, fill=tk.BOTH)

cv.create_rectangle(0,0,100,100, tag="red", fill='red')
cv.create_rectangle(0,100,100,200, tag="blue", fill='blue')
cv.create_oval(100,0,200,100, tag="red", fill='red')
cv.create_oval(100,100,200,200, tag="blue", fill='blue')

reds = cv.find_withtag('red')
blues = cv.find_withtag('blue')

def move_red():
    cv.move('red', 200, 0)

def move_blue():
    cv.move('blue', 200, 0)

btnMoveRed = tk.Button(cv, text='Red->', command=move_red)
btnMoveBlue = tk.Button(cv, text='Blue->', command=move_blue)
cv.create_window(0,300,window=btnMoveRed, anchor=tk.NW)
cv.create_window(0,350,window=btnMoveBlue, anchor=tk.NW)

root.mainloop()
