import pygame

class PVEWindow: #Player vs Computer

    def __init__(self):
        self.create()


    def create(self):

        pygame.init()

        icon = pygame.image.load('chessIcon.png')

        gameWindow = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("PvE Chess")
        pygame.display.set_icon(icon)

        running = True
        while running:  # game loop

            for event in pygame.event.get():  # exits game loop when window is closed
                if event.type == pygame.QUIT:
                    running = False

        pygame.draw.rect(gameWindow, (193, 75, 31), (0, 0, 800, 800))  # draws the game board

        pygame.display.update()  # update all visuals

        pygame.quit()