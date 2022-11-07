import pygame
import numpy as np
import random


class Field:
    def __init__(self, width, height, scale, offset):
        self.scale = scale

        self.columns = int(height / scale)
        self.lines = int(width / 2)
        self.size = (self.lines, self.columns)
        self.array = np.ndarray(shape = self.size)

        self.offset = offset

    def randField(self):
        for x in range(self.lines):
            for y in range(self.columns):
                self.array[x][y] = random.randint(0, 1)

    def gameOfLife(self, cellColor, offColor, surface, pause):
        for x in range(self.lines):
            for y in range(self.columns):
                y_pos = self.scale * y
                x_pos = self.scale * x

                if self.array[x][y] == 1:
                    pygame.draw.rect(surface,
                                     cellColor,
                                     [x_pos, y_pos, self.scale - self.offset, self.scale - self.offset])
                elif self.array[x][y] == 0:
                    pygame.draw.rect(surface,
                                     offColor,
                                     [x_pos, y_pos, self.scale - self.offset, self.scale - self.offset])

        newField = np.ndarray(shape = self.size)
        if pause:
            for x in range(self.lines):
                for y in range(self.columns):
                    current = self.array[x][y]
                    neighbours = self.countNeigbours(x, y)
                    if current == 0 and neighbours == 3:
                        newField[x][y] = 1
                    elif current == 1 and (neighbours < 2 or neighbours > 3):
                        newField[x][y] = 0
                    else:
                        newField[x][y] = current

            self.array = newField

    def countNeigbours(self, x, y):
        counter = 0

        for n in range(-1, 2):
            for m in range(-1, 2):
                x0 = (n + x + self.lines) % self.lines
                y0 = (m + y + self.columns) % self.columns

                counter += self.array[x0][y0]

        counter -= self.array[x][y]
        return counter

    def isEnd(self):
        if 1 in self.array:
            return False
        else:
            return True

    def mouse(self, x, y):
        x0 = x // self.scale
        y0 = y // self.scale

        if self.array[x0][y0] == 0:
            self.array[x0][y0] = 1
        else:
            self.array[x0][y0] = 0
