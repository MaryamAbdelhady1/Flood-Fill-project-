import pygame

class Unweighted_grid :
    def __init__(self):
        self.grid_width = 810
        self.grid_height = 600
        self.block_width = 30
        self.block_height = 30
        self.grid_color = (255, 255, 255)
        self.block_color = (0, 0, 0)
        self.grid = pygame.display.set_mode((self.grid_width, self.grid_height))
        self.draw_grid()

    def draw_grid(self):
        self.grid.fill(self.grid_color)
        for x in range(0, self.grid_width, self.block_width):
            for y in range(0, self.grid_height, self.block_height):
                rect = pygame.Rect(x, y, self.block_width, self.block_height)
                pygame.draw.rect(self.grid, self.block_color, rect, 1)

    def color_click_position(self , position , color ):
        [row , column] = position
        row = ( row // self.block_width ) * self.block_width
        column = ( column // self.block_height ) * self.block_height
        rect = pygame.Rect(row , column, self.block_width, self.block_height)
        pygame.draw.rect(self.grid, color , rect)

