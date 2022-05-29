from tkinter import *
def showPosEvent(event):
    print('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))

def showAllEvent(event):
    for attr in dir(event):
        if not attr.startswith('__'):
            print(attr, '=>', getattr(event, attr))

def onKeyPress(event):
    print("Got key press:", event.char)

def onArrowKey(event):
    print("Got up key press")

def onReturnKey(event):
    print("Got Return key press")

def onLeftClick(event):
    print("Got left mouse click:", end=' ')
    showPosEvent(event)

def onRightClick(event):
    print('Got right mouse click:', end=' ')
    showPosEvent(event)

def onMiddleClick(event):
    print('Got middle mouse click:', end=' ')
    showPosEvent(event)
    showAllEvent(event)

def onLeftDrag(event):
    print('Got left mouse button drag:', end=' ')
    showPosEvent(event)

def onDoubleLeftClick(event):
    print('Got double left mouse click', end=' ')
    showPosEvent(event)
    tkroot.destroy()

tkroot = Tk()
labelFont = ('courier', 20, 'bold')
lbl = Label(tkroot, text='Hello bind world', font=labelFont, bg='red', height=5, width=20)
lbl.pack(expand=YES, fill=BOTH)

lbl.bind('<Button-1>', onLeftClick)
lbl.bind('<Button-3>', onRightClick)
lbl.bind('<Button-2>', onMiddleClick)
lbl.bind('<Double-1>', onDoubleLeftClick)
lbl.bind('<B1-Motion>', onLeftDrag)
lbl.bind('<KeyPress>', onKeyPress)
lbl.bind('<Up>', onArrowKey)
lbl.bind('<Return>', onReturnKey)


lbl.focus()

tkroot.title('Click Me')
tkroot.mainloop()
print("88")
