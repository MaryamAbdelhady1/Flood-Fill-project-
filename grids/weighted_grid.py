import pygame
import random

class Weighted_grid :
    def __init__(self):
        self.grid_width = 600
        self.grid_height = 600
        self.block_width = 30
        self.block_height = 30
        self.grid_color = (255, 255, 255)
        self.block_color = (0, 0, 0)
        self.rows = self.grid_height // self.block_height
        self.columns = self.grid_width // self.block_width
        self.weights = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.font = pygame.font.Font(None, 20)
        self.grid = pygame.display.set_mode((self.grid_width, self.grid_height))
        self.draw_grid()

    def draw_grid(self):
        self.grid.fill(self.grid_color)

        for row in range(self.rows):
            for column in range(self.columns):
                x = column * self.block_width
                y = row * self.block_height
                rect = pygame.Rect(x, y, self.block_width, self.block_height)
                pygame.draw.rect(self.grid, self.block_color, rect, 1)

                weight = random.choice(range(1 , 11 , 1))
                self.weights[row][column] = weight

                text_surface = self.font.render(str(weight), True, (0, 0, 255))
                text_rect = text_surface.get_rect(center=rect.center)
                self.grid.blit(text_surface, text_rect)


    def color_click_position(self , position , color ):
        [row , column] = position
        row = ( row // self.block_width ) * self.block_width
        column = ( column // self.block_height ) * self.block_height
        rect = pygame.Rect(row , column, self.block_width, self.block_height)
        pygame.draw.rect(self.grid, color , rect)

