import pygame
from unweighted_grid import *
from weighted_grid import *
from bfs import *
from dfs import *
from sp import *
from minimum_weight import *
pygame.init()

class Controls :
    def __init__(self , algorithm ):

        self.colored_cells = []
        if algorithm == "dijkstra" : self.grid = Weighted_grid()
        else : self.grid = Unweighted_grid()
        self.click = True
        click_counter = 0

        run = True
        while run :

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RETURN :
                        self.click = False
                        if algorithm == 'bfs' :
                            Bfs(self)
                            SP(self)
                        elif algorithm == 'dfs' :
                            Dfs(self)
                            SP(self)
                        else : Dijkstra(self)

                if not self.click : continue
                if event.type == pygame.MOUSEBUTTONDOWN :
                    click_counter += 1
                    position = pygame.mouse.get_pos()
                    self.colored_cells.append(position)

                if click_counter == 1 :
                    self.grid.color_click_position(position , "green" )
                elif click_counter == 2 :
                    self.grid.color_click_position(position , "blue" )
                elif click_counter >= 3 :
                    self.grid.color_click_position(position , "black")

            pygame.display.update()

    def pass_position(self , pos , color ) :
        self.grid.color_click_position( pos , color )

