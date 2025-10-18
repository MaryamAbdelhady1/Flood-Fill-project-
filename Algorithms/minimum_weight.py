import heapq
from weighted_grid import *
from collections import *

class Dijkstra :
    def __init__(self , grid ):
        [self.x_start, self.y_start] = grid.colored_cells[0]
        [self.x_end, self.y_end] = grid.colored_cells[1]
        self.block_size = 30
        self.x_start //= self.block_size
        self.y_start //= self.block_size
        self.x_end //= self.block_size
        self.y_end //= self.block_size
        self.rows = 600 // self.block_size
        self.columns = 600 // self.block_size
        self.distance = [[float('inf') for _ in range(self.columns)] for _ in range(self.rows)]
        self.parent = [[[0, 0] for _ in range(self.columns)] for _ in range(self.rows)]
        self.visited = [[False for _ in range(self.columns)] for _ in range(self.rows)]
        self.weights = grid.grid.weights

        for (x, y) in grid.colored_cells:
            self.visited[x // self.block_size][y // self.block_size] = True

        self.visited[self.x_start][self.y_start] = False
        self.visited[self.x_end][self.y_end] = False

        self.dx = [0, 0, 1, -1]
        self.dy = [1, -1, 0, 0]

        pq = []
        heapq.heappush( pq , ( 0 , self.x_start, self.y_start))
        self.visited[self.x_start][self.y_start] = True
        self.distance[self.x_start][self.y_start] = 0

        while pq :
            ( dis , x, y ) = heapq.heappop(pq)
            if (x, y) == (self.x_end, self.y_end):
                break

            if self.distance[x][y] < dis :
                continue

            for i in range(4):
                new_x = x + self.dx[i]
                new_y = y + self.dy[i]
                if self.valid(new_x, new_y) and self.distance[new_x][new_y] >= self.weights[new_x][new_y] + dis :
                    self.distance[new_x][new_y] = self.weights[new_x][new_y] + dis
                    self.parent[new_x][new_y] = [x, y]
                    heapq.heappush( pq , ( self.distance[new_x][new_y] , new_x, new_y))
                    if new_x != self.x_end or new_y != self.y_end:
                        grid.pass_position((new_x * self.block_size, new_y * self.block_size), "yellow")
                        pygame.time.delay(20)
                        pygame.display.update()

        self.path_weight = self.distance[self.x_end][self.y_end]
        if self.path_weight != float('inf') : self.color_shortest_path(grid, self.parent[self.x_end][self.y_end])
        self.display_path_weight(grid)

    def valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.columns and not self.visited[x][y]

    def color_shortest_path(self, grid, node):
        [x, y] = node

        grid.pass_position((x * self.block_size , y * self.block_size ), "red")
        pygame.time.delay(20)
        pygame.display.update()
        if (self.parent[x][y] == [self.x_start, self.y_start] or self.parent == [0 , 0] ):
            return

        return self.color_shortest_path(grid, self.parent[x][y])

    def display_path_weight(self, grid):
        font = pygame.font.SysFont("arial", 36, bold=True)
        if self.path_weight == float('inf'):
            text = font.render("No Path Found!", True, (0, 0, 0))
        else:
            text = font.render(f"Path Weight = {self.path_weight}", True, (0, 0, 0))

        grid.grid.grid.blit(text, (10, 10))
        pygame.display.update()
