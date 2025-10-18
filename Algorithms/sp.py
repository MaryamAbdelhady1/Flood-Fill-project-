from collections import deque
import pygame
from controls import *

class SP :
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
        self.distance = [[float('inf') for _ in range(self.columns)] for _ in range(self.rows)]
        self.parent = [[[0,0] for _ in range(self.columns)] for _ in range(self.rows)]
        self.visited = [[False for _ in range(self.columns)] for _ in range(self.rows)]
        for (x, y) in grid.colored_cells:
            self.visited[x // self.block_size][y // self.block_size] = True

        self.visited[self.x_start][self.y_start] = False
        self.visited[self.x_end][self.y_end] = False

        self.directions = [ [0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0] ]

        q = deque()
        q.append((self.x_start, self.y_start))
        self.visited[self.x_start][self.y_start] = True
        self.distance[self.x_start][self.y_start] = 0

        while q:
            x, y = q.popleft()
            if (x, y) == (self.x_end, self.y_end):
                break

            for (dx , dy) in self.directions :
                new_x = x + dx
                new_y = y + dy
                if self.valid(new_x, new_y) and self.distance[new_x][new_y] == float('inf'):
                    self.distance[new_x][new_y] = self.distance[x][y] + 1
                    self.parent[new_x][new_y] = [x , y]
                    q.append((new_x, new_y))

        self.path_length = self.distance[self.x_end][self.y_end]
        if self.path_length != float('inf'): self.color_shortest_path( grid , self.parent[self.x_end][self.y_end])
        self.display_path_length(grid)

    def valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.columns and not self.visited[x][y]

    def color_shortest_path(self , grid , node ) :
        [x , y] = node

        grid.pass_position((x * self.block_size , y * self.block_size ) , "red" )
        pygame.time.delay(20)
        pygame.display.update()
        if ( self.parent[x][y] == [self.x_start, self.y_start] ) :
            return

        return self.color_shortest_path( grid , self.parent[x][y] )

    def display_path_length(self, grid):
        font = pygame.font.SysFont("arial", 36, bold=True)
        if self.path_length == float('inf'): text = font.render("No Path Found!", True, (0 , 0, 0))
        else : text = font.render(f"Shortest Path Length = {self.path_length}", True, (0 , 0, 0) )
        grid.grid.grid.blit(text, (10, 10))
        pygame.display.update()
