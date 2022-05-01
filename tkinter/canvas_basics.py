import tkinter as tk

root = tk.Tk()
root.geometry("800x600")

cv = tk.Canvas(root)
cv.pack(expand=tk.YES, fill=tk.BOTH)

cv.configure(background='yellow')

# coordinates: left top is (0,0)

# draw a text
cv.create_text(100,100, text="Ham")

# add a line
cv.create_line(0,0, 100,100)

# rectangle
cv.create_rectangle(0,0,100,100)

# draw an ellipse
cv.create_oval(0,0,100,100)

# draw an arc(partial ellipse)
cv.create_arc(100,50, 500,300, start=90, extent=45, fill='red')

# draw an image
img = tk.PhotoImage(file='images/bird.gif')
cv.create_image(300,0,image=img, anchor=tk.NW)

# embed a Button widget
def on_click():
    lblName['text'] = "clicked"
btnTest = tk.Button(cv, text="Test", fg="white", bg="black")
btnTest['command'] = on_click
cv.create_window(0,300,window=btnTest, anchor=tk.NW)

# embed a Label widget
lblName = tk.Label(cv, text="name")
cv.create_window(0, 350, window=lblName, anchor=tk.NW)

root.mainloop()
