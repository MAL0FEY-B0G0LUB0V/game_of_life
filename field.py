import pygame
import numpy as np
import random


class Field:
    def __init__(self, width, height, scale, offset):
        self.scale = scale

        self.columns = int(height / scale)
        self.lines = int(width / scale)  # исправлено: теперь делим width на scale
        self.size = (self.lines, self.columns)
        self.array = np.zeros(self.size, dtype=int)  # инициализация нулями

        self.offset = offset

    def randField(self):
        self.array = np.random.randint(0, 2, size=self.size)

    def gameOfLife(self, cellColor, offColor, surface, pause):
        # отрисовка клеток
        for x in range(self.lines):
            for y in range(self.columns):
                y_pos = self.scale * y
                x_pos = self.scale * x

                color = cellColor if self.array[x][y] == 1 else offColor

                pygame.draw.rect(
                    surface,
                    color,
                    pygame.Rect(x_pos, y_pos, self.scale - self.offset, self.scale - self.offset)
                )

        if pause:
            newField = np.copy(self.array)
            for x in range(self.lines):
                for y in range(self.columns):
                    current = self.array[x][y]
                    neighbours = self.countNeigbours(x, y)
                    if current == 0 and neighbours == 3:
                        newField[x][y] = 1
                    elif current == 1 and (neighbours < 2 or neighbours > 3):
                        newField[x][y] = 0
                    # иначе — остаётся как есть
            self.array = newField

    def countNeigbours(self, x, y):
        # тороидальная матрица
        total = 0
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx != 0 or dy != 0:
                    x0 = (x + dx) % self.lines
                    y0 = (y + dy) % self.columns
                    total += self.array[x0][y0]
        return total

    def isEnd(self):
        return not np.any(self.array)

    def mouse(self, x, y):
        x0 = x // self.scale
        y0 = y // self.scale

        if 0 <= x0 < self.lines and 0 <= y0 < self.columns:
            self.array[x0][y0] ^= 1  # переключение 0 <-> 1

