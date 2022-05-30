import tkinter as tk
import random as rand
import shapes

class Block:
    def __init__(self, x, y, color=None):
        self.x = x
        self.y = y
        self.color = color

class Figure:
    def __init__(self, shape=None, state=0, x=0, y=0):
        self.x = x 
        self.y = y
        if shape is None:
            shape = rand.choice(shapes.shapeList)
        self.allBlocks = self.load_blocks(shape)
        self.state = state
        self.stateCount = len(shape)

    # calculate and save all the blocks offset coords, the shape's top-left is (0,0)
    def load_blocks(self, shape):
        blocks = []
        for stateData in shape:
            stateBlocks = []
            for y, row in enumerate(stateData):
                for x, cell in enumerate(row):
                    if cell == 'o':
                        stateBlocks.append(Block(x,y))
            blocks.append(stateBlocks) 
        return blocks

    def next_state(self):
        self.state = (self.state+1) % self.stateCount

    def shape_blocks(self):
        return self.allBlocks[self.state]

    def cur_blocks(self):
        stateBlocks = []
        for blk in self.allBlocks[self.state]:
            stateBlocks.append(Block(blk.x + self.x, blk.y + self.y, blk.color))
        return stateBlocks

    def offset_blocks(self, offsetX=0, offsetY=0):
        stateBlocks = []
        for blk in self.allBlocks[self.state]:
            stateBlocks.append(Block(blk.x + self.x + offsetX, blk.y + self.y + offsetY, blk.color))
        return stateBlocks

    def left_blocks(self):
        return self.offset_blocks(offsetX=-1)

    def right_blocks(self):
        return self.offset_blocks(offsetX=1)

    def down_blocks(self):
        return self.offset_blocks(offsetY=1)

    def next_blocks(self):
        nextState = (self.state+1)%self.stateCount
        stateBlocks = []
        for blk in self.allBlocks[nextState]:
            stateBlocks.append(Block(blk.x+self.x, blk.y+self.y, blk.color))
        return stateBlocks


class Playground:
    def __init__(self, rows=20, cols=10):
        self.rows = rows
        self.cols = cols
        self.blocks = [] # collection of (x,y) 
        self.score = 0

    def detect_collision(self, figBlocks):
        # hit border detection
        for blk in figBlocks:
            if blk.x < 0 or blk.x >= self.cols or blk.y >= self.rows:
                return True
        # collision with existing blocks detection
        for blk in figBlocks:
            for blk2 in self.blocks:
                if blk.x == blk2.x and blk.y == blk2.y:
                    return True

        return False

    def rotate_fig(self, fig):
        if not self.detect_collision(fig.next_blocks()):
            fig.next_state()
            return True
        return False

    def move_fig_left(self, fig):
        if not self.detect_collision(fig.left_blocks()):
            fig.x -= 1
            return True
        return False

    def move_fig_right(self, fig):
        if not self.detect_collision(fig.right_blocks()):
            fig.x += 1
            return True
        return False

    def move_fig_down(self, fig):
        if not self.detect_collision(fig.down_blocks()):
            fig.y += 1
            return True
        return False

    def freeze_fig(self, fig):
       self.blocks.extend(fig.cur_blocks()) 

    def find_full_rows(self):
        fullRows=[]
        for row in range(self.rows):
            rowBlks = []
            for blk in self.blocks:
                if blk.y == row:
                    rowBlks.append(blk)
            if len(rowBlks) == self.cols:
                fullRows.append(row)

        return fullRows

    def delete_full_row(self, row):
        for blk in self.blocks:
            if blk.y == row:
                self.blocks.remove(blk)
            if blk.y < row:
                blk.y += 1
        self.score += 1

    def delete_full_rows(self):
        fullRows = self.find_full_rows()
        for row in fullRows:
            self.delete_full_row(row)

