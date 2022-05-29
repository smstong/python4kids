import tkinter as tk
import random

class Game:
    def __init__(self):
        self.timerInterval = 1000
        self.root = tk.Tk()
        self.root.title("Tetris game")
        self.pg = Playground(self.root)

    def on_key_up(self, event):
        self.quad.rotate()
        
    def on_key_down(self, event):
        self.quad.move_down()
    
    def on_key_left(self, event):
        self.quad.move_left()
        
    def on_key_right(self, event):
        self.quad.move_right()

    def new_quad(self):
        colors = ['red', 'green', 'yellow']
        color = random.choice(colors)
        shapes = ['T', 'Z', 'RZ', 'L', 'RL', 'Line']
        shape = random.choice(shapes)

        if shape == 'L':
            self.quad = LQuad(self.pg, color=color)
        elif shape == 'RL':
            self.quad = ReverseLQuad(self.pg, color=color)
        elif shape == 'Z':
            self.quad = ZQuad(self.pg, color=color)
        elif shape == 'RZ':
            self.quad = ReverseZQuad(self.pg, color=color)
        elif shape == 'T':
            self.quad = TQuad(self.pg, color=color)
        elif shape == 'Line':
            self.quad = LineQuad(self.pg, color=color)
        else:
            pass
        
    def start(self): 
        self.new_quad()
        
        self.root.after(self.timerInterval, self.on_timer)
        
        self.root.bind('<Up>', self.on_key_up)
        self.root.bind('<Down>', self.on_key_down)
        self.root.bind('<Left>', self.on_key_left)
        self.root.bind('<Right>', self.on_key_right)
        
        self.root.mainloop()

    def on_timer(self):
        self.quad.move_down()
        
        self.root.after(self.timerInterval, self.on_timer)
    
        
class Playground(tk.Canvas):
    def __init__(self, parent, cols=10, rows=20, blockSize=30):
        
        self.cols = cols
        self.rows = rows
        self.blockSize = blockSize
        self.staticBlocks = [] # existing static blocks

        width = self.blockSize * self.cols
        height = self.blockSize * self.rows
       
        tk.Canvas.__init__(self, parent, bg='black', width=width, height=height)
        self.pack(expand=tk.YES, fill=tk.BOTH)
        
# A quad is a shape consisting of 4 blocks
class Quad:
    def __init__(self, playground, color='red', direction=0):
        self.playground = playground
        self.canvas = playground
        self.color = color
        self.direction = direction
        self.blocks = [[playground.cols/2, 0]]
        self.uiObjs = []

    def create_ui(self):
        for block in self.blocks:
            x0 = block[0]*self.playground.blockSize
            y0 = block[1]*self.playground.blockSize
            x1 = x0 + self.playground.blockSize
            y1 = y0 + self.playground.blockSize
            self.uiObjs.append(self.canvas.create_rectangle(x0, y0, x1, y1,fill=self.color, width=0))
            
    def update_ui(self):
        for i, block in enumerate(self.blocks):
            x0 = block[0]*self.playground.blockSize
            y0 = block[1]*self.playground.blockSize
            x1 = x0 + self.playground.blockSize
            y1 = y0 + self.playground.blockSize
            self.canvas.moveto(self.uiObjs[i], x0, y0)
            
    def rotate(self):
        pass
    
    def move_down(self):
        hit = False
        for block in self.blocks:
            y = block[1]
            y += 1
            # check if it hitting another block
            
            # check if it is hitting border
            if block[1] >= self.playground.rows:
                self.playground.staticBlocks.extend(self.blocks)
                hit = True
                break
            
        if not hit:
            for block in self.blocks:
                block[1] += 1
            self.update_ui()
        
        
    def move_up(self):
        for block in self.blocks:
            block[1] -= 1
        self.update_ui()
        
    def move_right(self):
        for block in self.blocks:
            block[0] += 1
        self.update_ui()
        
    def move_left(self):
        for block in self.blocks:
            block[0] -= 1
        self.update_ui()
        
# Line shaped quad
class LineQuad(Quad):
    def __init__(self, playground, color='red', direction=0):
        Quad.__init__(self, playground, color, direction)
        x0 = self.blocks[0][0]
        y0 = self.blocks[0][1]
        x1 = x0
        y1 = y0 + 1
        x2 = x1
        y2 = y1 + 1
        x3 = x2
        y3 = y2 + 1
        self.blocks = [[x0,y0], [x1,y1], [x2,y2], [x3,y3]]
        self.create_ui()

    
    def rotate(self):
        if self.direction == 0:
            x1, y1 = self.blocks[1]
            x0, y0 = x1-1, y1
            x2, y2 = x1+1, y1
            x3, y3 = x2+1, y2
            
        elif self.direction == 1:
            x1, y1 = self.blocks[1]
            x0, y0 = x1, y1-1
            x2, y2 = x1, y1+1
            x3, y3 = x2, y2+1
            
        elif self.direction == 2:
            x1, y1 = self.blocks[1]
            x0, y0 = x1-1, y1
            x2, y2 = x1+1, y1
            x3, y3 = x2+1, y2
            
        elif self.direction == 3:
            x1, y1 = self.blocks[1]
            x0, y0 = x1, y1-1
            x2, y2 = x1, y1+1
            x3, y3 = x2, y2+1
        else:
            pass
        
        self.blocks = [[x0,y0], [x1,y1], [x2,y2], [x3,y3]]
        self.direction = (self.direction +1) % 4
        self.update_ui()
        
# Square shaped quad    
class SquareQuad(Quad):
    def __init__(self, playground, color='red', direction=0):
        Quad.__init__(self, playground, color, direction)
        x0 = self.blocks[0][0]
        y0 = self.blocks[0][1]
        x1 = x0 + 1
        y1 = y0
        x2 = x1
        y2 = y1 + 1
        x3 = x2 - 1
        y3 = y2
        self.blocks = [[x0,y0], [x1,y1], [x2,y2], [x3,y3]]
        self.create_ui()

    # square quad has no rotation effects
    def rotate(self):
        self.direction = (self.direction +1) % 4
        
# T-shaped quad
class TQuad(Quad):
    def __init__(self, playground, color='red', direction=0):
        Quad.__init__(self, playground, color, direction)
        x0 = self.blocks[0][0]
        y0 = self.blocks[0][1]
        x1 = x0
        y1 = y0 + 1
        x2 = x1 -1
        y2 = y1
        x3 = x1 + 1
        y3 = y1
        self.blocks = [[x0,y0], [x1,y1], [x2,y2], [x3,y3]]
        self.create_ui()

    
    def rotate(self):
        if self.direction == 0:
            x1, y1 = self.blocks[1]
            x0, y0 = x1+1, y1
            x2, y2 = x1, y1-1
            x3, y3 = x1, y1+1
            
        elif self.direction == 1:
            x1, y1 = self.blocks[1]
            x0, y0 = x1, y1+1
            x2, y2 = x1-1, y1
            x3, y3 = x1+1, y1
            
        elif self.direction == 2:
            x1, y1 = self.blocks[1]
            x0, y0 = x1-1, y1
            x2, y2 = x1, y1-1
            x3, y3 = x1, y1+1
            
        elif self.direction == 3:
            x1, y1 = self.blocks[1]
            x0, y0 = x1, y1-1
            x2, y2 = x1-1, y1
            x3, y3 = x1+1, y1
        else:
            pass
        
        self.blocks = [[x0,y0], [x1,y1], [x2,y2], [x3,y3]]
        self.direction = (self.direction +1) % 4
        self.update_ui()

# L-shaped quad
class LQuad(Quad):
    def __init__(self, playground, color='red', direction=0):
        Quad.__init__(self, playground, color, direction)
        x0 = self.blocks[0][0]
        y0 = self.blocks[0][1]
        x1 = x0
        y1 = y0 + 1
        x2 = x1
        y2 = y1 + 1
        x3 = x2 + 1
        y3 = y2
        self.blocks = [[x0,y0], [x1,y1], [x2,y2], [x3,y3]]
        self.create_ui()

    
    def rotate(self):
        if self.direction == 0:
            x2, y2 = self.blocks[2]
            x0, y0 = x2+2, y2
            x1, y1 = x2+1, y2
            x3, y3 = x2, y2+1
            
        elif self.direction == 1:
            x2, y2 = self.blocks[2]
            x0, y0 = x2, y2+2
            x1, y1 = x2, y2+1
            x3, y3 = x2-1, y2
            
        elif self.direction == 2:
            x2, y2 = self.blocks[2]
            x0, y0 = x2-2, y2
            x1, y1 = x2-1, y2
            x3, y3 = x2, y2-1
            
        elif self.direction == 3:
            x2, y2 = self.blocks[2]
            x0, y0 = x2, y2-2
            x1, y1 = x2, y2-1
            x3, y3 = x2+1, y2
        else:
            pass
        
        self.blocks = [[x0,y0], [x1,y1], [x2,y2], [x3,y3]]
        self.direction = (self.direction +1) % 4
        self.update_ui()


# Reversed L shaped quad
class ReverseLQuad(Quad):
    def __init__(self, playground, color='red', direction=0):
        Quad.__init__(self, playground, color, direction)
        x0 = self.blocks[0][0]
        y0 = self.blocks[0][1]
        x1 = x0
        y1 = y0 + 1
        x2 = x1
        y2 = y1 + 1
        x3 = x2 - 1
        y3 = y2
        self.blocks = [[x0,y0], [x1,y1], [x2,y2], [x3,y3]]
        self.create_ui()

    
    def rotate(self):
        if self.direction == 0:
            x2, y2 = self.blocks[2]
            x0, y0 = x2+2, y2
            x1, y1 = x2+1, y2
            x3, y3 = x2, y2-1
            
        elif self.direction == 1:
            x2, y2 = self.blocks[2]
            x0, y0 = x2, y2+2
            x1, y1 = x2, y2+1
            x3, y3 = x2+1, y2
            
        elif self.direction == 2:
            x2, y2 = self.blocks[2]
            x0, y0 = x2-2, y2
            x1, y1 = x2-1, y2
            x3, y3 = x2, y2+1
            
        elif self.direction == 3:
            x2, y2 = self.blocks[2]
            x0, y0 = x2, y2-2
            x1, y1 = x2, y2-1
            x3, y3 = x2-1, y2
        else:
            pass
        
        self.blocks = [[x0,y0], [x1,y1], [x2,y2], [x3,y3]]
        self.direction = (self.direction +1) % 4
        self.update_ui()

# Z-shaped quad
class ZQuad(Quad):
    def __init__(self, playground, color='red', direction=0):
        Quad.__init__(self, playground, color, direction)
        x0 = self.blocks[0][0]
        y0 = self.blocks[0][1]
        x1 = x0 + 1
        y1 = y0
        x2 = x1
        y2 = y1 + 1
        x3 = x2 + 1
        y3 = y2
        self.blocks = [[x0,y0], [x1,y1], [x2,y2], [x3,y3]]
        self.create_ui()

    
    def rotate(self):
        if self.direction == 0:
            x2, y2 = self.blocks[2]
            x1, y1 = x2+1, y2
            x3, y3 = x2, y2+1
            x0, y0 = x1, y1-1
            
        elif self.direction == 1:
            x2, y2 = self.blocks[2]
            x1, y1 = x2, y2+1
            x3, y3 = x2-1, y2
            x0, y0 = x1+1, y1
            
        elif self.direction == 2:
            x2, y2 = self.blocks[2]
            x1, y1 = x2-1, y2
            x3, y3 = x2, y2-1
            x0, y0 = x1, y1+1
            
        elif self.direction == 3:
            x2, y2 = self.blocks[2]
            x1, y1 = x2, y2-1
            x3, y3 = x2+1, y2
            x0, y0 = x1-1, y1
        else:
            pass
        
        self.blocks = [[x0,y0], [x1,y1], [x2,y2], [x3,y3]]
        self.direction = (self.direction +1) % 4
        self.update_ui()


# Reversed Z-shaped quad
class ReverseZQuad(Quad):
    def __init__(self, playground, color='red', direction=0):
        Quad.__init__(self, playground, color, direction)
        x0 = self.blocks[0][0]
        y0 = self.blocks[0][1]
        x1 = x0 - 1
        y1 = y0
        x2 = x1
        y2 = y1 + 1
        x3 = x2 - 1
        y3 = y2
        self.blocks = [[x0,y0], [x1,y1], [x2,y2], [x3,y3]]
        self.create_ui()

    
    def rotate(self):
        if self.direction == 0:
            x2, y2 = self.blocks[2]
            x3, y3 = x2, y2-1
            x1, y1 = x2+1, y2
            x0, y0 = x1, y1+1
            
        elif self.direction == 1:
            x2, y2 = self.blocks[2]
            x3, y3 = x2+1, y2
            x1, y1 = x2, y2+1
            x0, y0 = x1-1, y1
            
        elif self.direction == 2:
            x2, y2 = self.blocks[2]
            x3, y3 = x2, y2+1
            x1, y1 = x2-1, y2
            x0, y0 = x1, y1-1
            
        elif self.direction == 3:
            x2, y2 = self.blocks[2]
            x3, y3 = x2-1, y2
            x1, y1 = x2, y2-1
            x0, y0 = x1+1, y1
        else:
            pass
        
        self.blocks = [[x0,y0], [x1,y1], [x2,y2], [x3,y3]]
        self.direction = (self.direction +1) % 4
        self.update_ui()



############ main ########
# UI
game = Game()
game.start()

