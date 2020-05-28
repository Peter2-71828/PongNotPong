import pygame

class Window():

    def __init__(self, width=1280, height=960, score_size=96):
        self.game_display = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        self.w = width
        self.h = height
        self.score_size = height / 10
        self.font = pygame.font.Font(None, 74)
        self.bg_color = pygame.Color('grey12')
        self.orange = (255,165,0)

    def resize(self, width, height):
        self.game_display = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        self.w = width
        self.h = height
        self.score_size = height / 10
        self.font = pygame.font.Font(None, int(width*74/1280))

    def update_display(self, player1, player2, ball):
        self.game_display.fill(self.bg_color)
        pygame.draw.rect(self.game_display,self.orange, player1.position)
        pygame.draw.rect(self.game_display,self.orange, player2.position)
        pygame.draw.ellipse(self.game_display,self.orange, ball)
        pygame.draw.aaline(self.game_display, self.orange, (self.w/2, 0), (self.w/2,self.h))
        pygame.draw.aaline(self.game_display, self.orange, (self.w ,self.score_size), (0,self.score_size))
        text = self.font.render(str(f"Computer - {player1.score}"), 1, self.orange)
        self.game_display.blit(text, (self.w / 6, 25))
        text = self.font.render(str(f"{player1.name} - {player2.score}"), 1, self.orange)
        self.game_display.blit(text, ((self.w / 6) * 4, 25))

    # def menu(self, player1, player2, ball):
