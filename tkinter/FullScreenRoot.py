from tkinter import *

class FullScreenRoot(Tk):
    """
    A class inherited from Tk, with <Esc> or <F11> to toggle fullscreen mode
    """
    def __init__(self):
        Tk.__init__(self)
        self.attributes('-fullscreen', True)
        self.bind("<F11>", self.toggle_fullscreen)
        self.bind("<Escape>", self.toggle_fullscreen)
        
    def toggle_fullscreen(self, event=None):
        self.attributes('-fullscreen',
                        not self.attributes('-fullscreen'))

if __name__ == '__main__':
    root = FullScreenRoot()
    Label(root, text="Press <Esc> or <F11> to toggole fullscreen mode").pack(
        expand=YES, fill=BOTH)
    root.mainloop()
