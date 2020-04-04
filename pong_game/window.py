import pygame

class Window():

    def __init__(self, width=1280, height=960, score_size=96):
        self.game_display = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        self.w = width
        self.h = height
        self.score_size = height / 10

    def resize(self, width, height):
        self.game_display = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        self.w = width
        self.h = height
        self.score_size = height / 10
