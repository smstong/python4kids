import tkinter as tk
import random
import pprint

class Game(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.timerInterval = 1000
        self.title("Tetris game")
        self.isRunning = True
        self.timerHandlers = []
        
        self.pg = Playground(self)

        self.bind('<space>', self.on_key_space)
        self.after(self.timerInterval, self.on_timer)
        
        self.mainloop()

    # use Space key to toggle game running/stop
    def on_key_space(self, event):
        self.isRunning = not self.isRunning
    
    def on_timer(self):
        if self.isRunning:
            for handler in self.timerHandlers:
                handler()
            
        self.after(self.timerInterval, self.on_timer)

# A filled cell of the play area
class Block:
    def __init__(self, x, y, uiObj):
        self.x = x
        self.y = y
        self.uiObj = uiObj

# The play area        
class Playground(tk.Canvas):
    def __init__(self, parent, cols=10, rows=20, blockSize=30):
        self.cols = cols
        self.rows = rows
        self.blockSize = blockSize
        self.staticBlocks = [] # existing static blocks
        self.quad = None
        self.game = parent
                
        width = self.blockSize * self.cols
        height = self.blockSize * self.rows
        tk.Canvas.__init__(self, parent, bg='black', width=width, height=height)
        self.pack(expand=tk.YES, fill=tk.BOTH)
        
        self.bind('<Up>', self.on_key_up)
        self.bind('<Down>', self.on_key_down)
        self.bind('<Left>', self.on_key_left)
        self.bind('<Right>', self.on_key_right)
        self.focus_set()
        parent.timerHandlers.append(self.on_timer)

    def on_timer(self):
        if self.quad is None:
            self.new_quad()
            
        self.quad.move_down()

    # return all blocks at row nRow
    def get_row_blocks(self, nRow):
        blocksInRow = []
        for sb in self.staticBlocks:
            if sb.y == nRow:
                blocksInRow.append(sb)
        return blocksInRow

    # return all blocks at col nCol
    def get_col_blocks(self, nCol):
        blocksInCol = []
        for sb in self.staticBlocks:
            if sb.x == nCol:
                locksInCol.append(sb)
        return blocksInCol

    # return the block at (nRow, nCol), or None if not existing
    def get_block(self, nRow, nCol):
        for sb in self.staticBlocks:
            if sb.x == nCol and sb.y == nRow:
                return sb
        return None
    
    def new_quad(self):
        colors = ['red', 'green', 'yellow']
        color = random.choice(colors)
        shapes = ['T', 'Z', 'RZ', 'L', 'RL', 'Line', 'Square']
        shape = random.choice(shapes)
        shape = 'Line'

        if shape == 'L':
            self.quad = LQuad(self, color=color)
        elif shape == 'RL':
            self.quad = ReverseLQuad(self, color=color)
        elif shape == 'Z':
            self.quad = ZQuad(self, color=color)
        elif shape == 'RZ':
            self.quad = ReverseZQuad(self, color=color)
        elif shape == 'T':
            self.quad = TQuad(self, color=color)
        elif shape == 'Line':
            self.quad = LineQuad(self, color=color)
        elif shape == 'Square':
            self.quad = SquareQuad(self, color=color)
        else:
            pass
        
    def freeze_quad(self):
        self.staticBlocks.extend(self.quad.blocks)

        # find FULL rows
        fullRows = []
        for row in range(self.rows):
            blocksInRow = self.get_row_blocks(row)
            if len(blocksInRow) == self.cols:
                fullRows.append(row)
                
        # remove full rows
        for fr in fullRows:
            self.remove_row(fr)

        self.quad = None
        
    def print_all(self):
        print('============')
        for sb in self.staticBlocks:
            print(f'({sb.y}, {sb.x}): {sb.uiObj}')
            
    def remove_row(self, nRow):
        print(f'Removing row {nRow}...')
        rowBlocks = self.get_row_blocks(nRow)
        for rb in rowBlocks:
            self.delete(rb.uiObj) # UI will update automatically by tkinter
            self.staticBlocks.remove(rb)
    
        # move down all static blocks above the deleted row
        for sb in self.staticBlocks:
            if sb.y < nRow:
                sb.y += 1
        self.update_ui()
        
    def update_ui(self):
        for sb in self.staticBlocks:
            uiX = sb.x * self.blockSize
            uiY = sb.y * self.blockSize
            self.moveto(sb.uiObj, uiX, uiY)
            
    def on_key_up(self, event):
        if self.quad:
            self.quad.rotate()
        
    def on_key_down(self, event):
        if self.quad:
            self.quad.move_down()
    
    def on_key_left(self, event):
        if self.quad:
            self.quad.move_left()
        
    def on_key_right(self, event):
        if self.quad:
            self.quad.move_right()

        
# A quad is a shape consisting of 4 blocks
class Quad:
    def __init__(self, playground, color='red', direction=0):
        self.playground = playground
        self.canvas = playground
        self.color = color
        self.direction = direction
        self.blocks = []
        for i in range(4):
            x = self.playground.cols//2
            y = 0
            uiX = x*self.playground.blockSize
            uiY = y*self.playground.blockSize
            uiObj = self.canvas.create_rectangle(uiX,
                                                 uiY,
                                                 uiX + self.playground.blockSize,
                                                 uiY + self.playground.blockSize,
                                                 fill=self.color, width=0)
            self.blocks.append(Block(x, y, uiObj))

        self.moveto(self.init_shape())

    # sub class must implement this method
    def init_shape(self):
        pass
    
    # must be implemented by sub classes
    def next_shape(self):
        pass    

    # param: points = [[x0,y0], [x1,y1], [x2,y2], [x3,y3]]
    def moveto(self, points):
        for i in range(4):
            self.blocks[i].x = points[i][0]
            self.blocks[i].y = points[i][1]

        self.update_ui()
        
    def update_ui(self):
        for block in self.blocks:
            uiX = block.x * self.playground.blockSize
            uiY = block.y * self.playground.blockSize
            self.canvas.moveto(block.uiObj, uiX, uiY)

    def rotate(self):
        newBlocks = self.next_shape()
        # if the new shape will hit border or other static blocks, cancel rotating
        for nb in newBlocks:
            if nb[0] < 0 or nb[0] >= self.playground.cols or nb[1] >= self.playground.rows:
                return
            if self.playground.get_block(nb[1], nb[0]) is not None:
                return
        
        self.moveto(newBlocks)
        
        self.direction = (self.direction +1) % 4
    
    def move_down(self):
        willHit = False
        # if the move will hit border or another static block, cancel moving
        for block in self.blocks:
            newY = block.y + 1
            if newY >= self.playground.rows:
                willHit = True
                break
            if self.playground.get_block(newY, block.x) is not None:
                willHit = True
                break
            
        # if not, move one step
        if not willHit:
            for block in self.blocks:
                block.y += 1
            self.update_ui()
        # if will hit, freeze it
        else:
            self.playground.freeze_quad()
        
    def move_right(self):
        # if the move will hit border or another static block, cancel moving
        for block in self.blocks:
            newX = block.x + 1
            if newX >= self.playground.cols:
                return
            if self.playground.get_block(block.y, newX) is not None:
                return
        # if not, move one step    
        for block in self.blocks:
            block.x += 1
        self.update_ui()
        
    def move_left(self):
        # if the move will hit border or another static block, cancel moving
        for block in self.blocks:
            newX = block.x - 1
            if newX < 0:
                return
            if self.playground.get_block(block.y, newX) is not None:
                return
        # if not, move one step    
        for block in self.blocks:
            block.x -= 1
        self.update_ui()
        
# Line shaped quad
class LineQuad(Quad):
    def __init__(self, playground, color='red', direction=0):
        Quad.__init__(self, playground, color, direction)
    
    def init_shape(self):
        x0 = self.playground.cols//2
        y0 = 0
        x1 = x0
        y1 = y0 + 1
        x2 = x1
        y2 = y1 + 1
        x3 = x2
        y3 = y2 + 1

        return [[x0,y0], [x1,y1], [x2,y2], [x3,y3]]
        
    def next_shape(self):
        if self.direction == 0:
            x1, y1 = self.blocks[1].x, self.blocks[1].y
            x0, y0 = x1-1, y1
            x2, y2 = x1+1, y1
            x3, y3 = x2+1, y2
            
        elif self.direction == 1:
            x1, y1 = self.blocks[1].x, self.blocks[1].y
            x0, y0 = x1, y1-1
            x2, y2 = x1, y1+1
            x3, y3 = x2, y2+1
            
        elif self.direction == 2:
            x1, y1 = self.blocks[1].x, self.blocks[1].y
            x0, y0 = x1-1, y1
            x2, y2 = x1+1, y1
            x3, y3 = x2+1, y2
            
        elif self.direction == 3:
            x1, y1 = self.blocks[1].x, self.blocks[1].y
            x0, y0 = x1, y1-1
            x2, y2 = x1, y1+1
            x3, y3 = x2, y2+1
        else:
            pass
        
        return [[x0,y0], [x1,y1], [x2,y2], [x3,y3]]
        
# Square shaped quad    
class SquareQuad(Quad):
    def __init__(self, playground, color='red', direction=0):
        Quad.__init__(self, playground, color, direction)

    def init_shape(self):
        x0 = self.playground.cols//2
        y0 = 0
        x1 = x0 + 1
        y1 = y0
        x2 = x1
        y2 = y1 + 1
        x3 = x2 - 1
        y3 = y2
        return [[x0,y0], [x1,y1], [x2,y2], [x3,y3]]

    # square quad has no rotation effects
    def next_shape(self):
        return [[self.block[0].x, self.block[0].y],
                [self.block[1].x, self.block[1].y],
                [self.block[2].x, self.block[2].y],
                [self.block[3].x, self.block[3].y]]
        
# T-shaped quad
class TQuad(Quad):
    def __init__(self, playground, color='red', direction=0):
        Quad.__init__(self, playground, color, direction)
        
    def init_shape(self):
        x0 = self.playground.cols//2
        y0 = 0
        x1 = x0
        y1 = y0 + 1
        x2 = x1 -1
        y2 = y1
        x3 = x1 + 1
        y3 = y1
        return [[x0,y0], [x1,y1], [x2,y2], [x3,y3]]
    
    def next_shape(self):
        if self.direction == 0:
            x1, y1 = self.blocks[1].x, self.blocks[1].y
            x0, y0 = x1+1, y1
            x2, y2 = x1, y1-1
            x3, y3 = x1, y1+1
            
        elif self.direction == 1:
            x1, y1 = self.blocks[1].x, self.blocks[1].y
            x0, y0 = x1, y1+1
            x2, y2 = x1-1, y1
            x3, y3 = x1+1, y1
            
        elif self.direction == 2:
            x1, y1 = self.blocks[1].x, self.blocks[1].y
            x0, y0 = x1-1, y1
            x2, y2 = x1, y1-1
            x3, y3 = x1, y1+1
            
        elif self.direction == 3:
            x1, y1 = self.blocks[1].x, self.blocks[1].y
            x0, y0 = x1, y1-1
            x2, y2 = x1-1, y1
            x3, y3 = x1+1, y1
        else:
            pass
        
        return [[x0,y0], [x1,y1], [x2,y2], [x3, y3]]

# L-shaped quad
class LQuad(Quad):
    def __init__(self, playground, color='red', direction=0):
        Quad.__init__(self, playground, color, direction)
        
    def init_shape(self):
        x0 = self.playground.cols//2
        y0 = 0
        x1 = x0
        y1 = y0 + 1
        x2 = x1
        y2 = y1 + 1
        x3 = x2 + 1
        y3 = y2
        return [[x0,y0], [x1,y1], [x2,y2], [x3,y3]]

    def next_shape(self):
        if self.direction == 0:
            x2, y2 = self.blocks[2].x, self.blocks[2].y
            x0, y0 = x2+2, y2
            x1, y1 = x2+1, y2
            x3, y3 = x2, y2+1
            
        elif self.direction == 1:
            x2, y2 = self.blocks[2].x, self.blocks[2].y
            x0, y0 = x2, y2+2
            x1, y1 = x2, y2+1
            x3, y3 = x2-1, y2
            
        elif self.direction == 2:
            x2, y2 = self.blocks[2].x, self.blocks[2].y
            x0, y0 = x2-2, y2
            x1, y1 = x2-1, y2
            x3, y3 = x2, y2-1
            
        elif self.direction == 3:
            x2, y2 = self.blocks[2].x, self.blocks[2].y
            x0, y0 = x2, y2-2
            x1, y1 = x2, y2-1
            x3, y3 = x2+1, y2
        else:
            pass
        
        return [[x0,y0], [x1,y1], [x2,y2], [x3, y3]]

# Reversed L shaped quad
class ReverseLQuad(Quad):
    def __init__(self, playground, color='red', direction=0):
        Quad.__init__(self, playground, color, direction)
        
    def init_shape(self):
        x0 = self.playground.cols//2
        y0 = 0
        x1 = x0
        y1 = y0 + 1
        x2 = x1
        y2 = y1 + 1
        x3 = x2 - 1
        y3 = y2
        return [[x0,y0], [x1,y1], [x2,y2], [x3,y3]]
    
    def next_shape(self):
        if self.direction == 0:
            x2, y2 = self.blocks[2].x, self.blocks[2].y
            x0, y0 = x2+2, y2
            x1, y1 = x2+1, y2
            x3, y3 = x2, y2-1
            
        elif self.direction == 1:
            x2, y2 = self.blocks[2].x, self.blocks[2].y
            x0, y0 = x2, y2+2
            x1, y1 = x2, y2+1
            x3, y3 = x2+1, y2
            
        elif self.direction == 2:
            x2, y2 = self.blocks[2].x, self.blocks[2].y
            x0, y0 = x2-2, y2
            x1, y1 = x2-1, y2
            x3, y3 = x2, y2+1
            
        elif self.direction == 3:
            x2, y2 = self.blocks[2].x, self.blocks[2].y
            x0, y0 = x2, y2-2
            x1, y1 = x2, y2-1
            x3, y3 = x2-1, y2
        else:
            pass
        
        return [[x0,y0], [x1,y1], [x2,y2], [x3, y3]]

# Z-shaped quad
class ZQuad(Quad):
    def __init__(self, playground, color='red', direction=0):
        Quad.__init__(self, playground, color, direction)
        
    def init_shape(self):
        x0 = self.playground.cols//2
        y0 = 0
        x1 = x0 + 1
        y1 = y0
        x2 = x1
        y2 = y1 + 1
        x3 = x2 + 1
        y3 = y2
        return [[x0,y0], [x1,y1], [x2,y2], [x3,y3]]

    def next_shape(self):
        if self.direction == 0:
            x2, y2 = self.blocks[2].x, self.blocks[2].y
            x1, y1 = x2+1, y2
            x3, y3 = x2, y2+1
            x0, y0 = x1, y1-1
            
        elif self.direction == 1:
            x2, y2 = self.blocks[2].x, self.blocks[2].y
            x1, y1 = x2, y2+1
            x3, y3 = x2-1, y2
            x0, y0 = x1+1, y1
            
        elif self.direction == 2:
            x2, y2 = self.blocks[2].x, self.blocks[2].y
            x1, y1 = x2-1, y2
            x3, y3 = x2, y2-1
            x0, y0 = x1, y1+1
            
        elif self.direction == 3:
            x2, y2 = self.blocks[2].x, self.blocks[2].y
            x1, y1 = x2, y2-1
            x3, y3 = x2+1, y2
            x0, y0 = x1-1, y1
        else:
            pass
        
        return [[x0,y0], [x1,y1], [x2,y2], [x3, y3]]


# Reversed Z-shaped quad
class ReverseZQuad(Quad):
    def __init__(self, playground, color='red', direction=0):
        Quad.__init__(self, playground, color, direction)

    def init_shape(self):
        x0 = self.playground.cols//2
        y0 = 0
        x1 = x0 - 1
        y1 = y0
        x2 = x1
        y2 = y1 + 1
        x3 = x2 - 1
        y3 = y2
        return [[x0,y0], [x1,y1], [x2,y2], [x3,y3]]
    
    def next_shape(self):
        if self.direction == 0:
            x2, y2 = self.blocks[2].x, self.blocks[2].y
            x3, y3 = x2, y2-1
            x1, y1 = x2+1, y2
            x0, y0 = x1, y1+1
            
        elif self.direction == 1:
            x2, y2 = self.blocks[2].x, self.blocks[2].y
            x3, y3 = x2+1, y2
            x1, y1 = x2, y2+1
            x0, y0 = x1-1, y1
            
        elif self.direction == 2:
            x2, y2 = self.blocks[2].x, self.blocks[2].y
            x3, y3 = x2, y2+1
            x1, y1 = x2-1, y2
            x0, y0 = x1, y1-1
            
        elif self.direction == 3:
            x2, y2 = self.blocks[2].x, self.blocks[2].y
            x3, y3 = x2-1, y2
            x1, y1 = x2, y2-1
            x0, y0 = x1+1, y1
        else:
            pass
        
        return [[x0,y0], [x1,y1], [x2,y2], [x3, y3]]


############ main ########
# UI
game = Game()

