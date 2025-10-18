import pygame
from controls import *
class Dfs :
    def __init__(self , grid ):
        [self.x_start, self.y_start] = grid.colored_cells[0]
        [self.x_end, self.y_end] = grid.colored_cells[1]
        self.block_size = 30
        self.x_start //= self.block_size
        self.y_start //= self.block_size
        self.x_end //= self.block_size
        self.y_end //= self.block_size

        self.rows = 810 // self.block_size
        self.columns = 600 // self.block_size
        self.visited = [[False for _ in range(self.columns)] for _ in range(self.rows)]
        self.parent = [[[-1,-1] for _ in range(self.columns)] for _ in range(self.rows)]
        for (x, y) in grid.colored_cells:
            self.visited[x // self.block_size][y // self.block_size] = True

        self.visited[self.x_start][self.y_start] = False
        self.visited[self.x_end][self.y_end] = False
        self.directions = [[0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0]]

        self.answer = float('inf')
        self.dfs(self.x_start, self.y_start, 0, grid)

    def dfs(self, x, y, distance, grid):
        self.visited[x][y] = True
        if x == self.x_end and y == self.y_end:
            self.answer = distance
            return True

        random.shuffle(self.directions)
        for (dx , dy) in self.directions :
            new_x = x + dx
            new_y = y + dy

            if (self.valid(new_x, new_y)):
                if new_x != self.x_end or new_y != self.y_end:
                    grid.pass_position((new_x * self.block_size , new_y * self.block_size), "yellow")
                    pygame.time.delay(20)
                    pygame.display.update()

                if self.dfs(new_x, new_y, distance + 1, grid) :
                    return True

        return False


    def valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.columns and not self.visited[x][y]

