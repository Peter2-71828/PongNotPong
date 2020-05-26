import pygame, sys
import time
from pong_game.player import Player
from pong_game.window import Window


class Menu():

  def __init__(self, player1_paddle_size = 200, max_score = 5):
    self.player1_paddle_size = player1_paddle_size
    self.max_score = max_score
    self.button_width = 250
    self.button_height = 200
    self.click = False
    self.font = pygame.font.SysFont(None, 80)
    self.title_font = pygame.font.SysFont(None, 100)

  def draw_text(self, text, font, color, surface, x, y):
    textobj = self.font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

    # def winner_menu(self, window, winner):
    # winner_string = '{} is the winner!'.format(winner)

  def main(self, window, screen, mx, my):

    button_easy = pygame.Rect((window.w/4) - self.button_width / 2, window.h/3, self.button_width, self.button_height)
    button_medium = pygame.Rect((window.w - self.button_width)/2, window.h/3, self.button_width, self.button_height)
    button_hard = pygame.Rect(((window.w/4) * 3) - (self.button_width/2), window.h/3, self.button_width, self.button_height)

    pygame.draw.rect(screen, (255, 0, 0), button_easy)
    pygame.draw.rect(screen, (255, 0, 0), button_medium)
    pygame.draw.rect(screen, (255, 0, 0), button_hard)

    self.draw_text('Pong Not Pong', self.title_font, (255,255,255), screen, window.w/2, window.h/6)
    self.draw_text('Easy', self.font, (255,255,255), screen, window.w/4, (self.button_height/2 + window.h/3))
    self.draw_text('Medium', self.font, (255,255,255), screen, window.w/2, (self.button_height/2 + window.h/3))
    self.draw_text('Hard', self.font, (255,255,255), screen, (window.w/4) * 3, (self.button_height/2 + window.h/3))


    if button_easy.collidepoint((mx, my)):
      if self.click:
        self.player1_paddle_size = 400
        self.click = True
    if button_medium.collidepoint((mx, my)):
      if self.click:
        self.player1_paddle_size = 200
        self.click = True
    if button_hard.collidepoint((mx, my)):
      if self.click:
        self.player1_paddle_size = 40
        self.click = True

  def menu(self, window):
    self.click = False
    screen = pygame.display.set_mode((window.w, window.h),0,32)
    clock = pygame.time.Clock()

    while self.click == False:
        screen.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()

        self.main(window, screen, mx, my)

        self.click = False
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
              pygame.quit()
              sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
              self.click = True

        pygame.display.update()
        clock.tick(60)

# while True:

  # screen.fill((0,0,0))

  # mx, my = pygame.mouse.get_pos()

  # button_easy = pygame.Rect((window.w/4) - self.button_width / 2, window.h/3, self.button_width, self.button_height)
  # button_medium = pygame.Rect((window.w - self.button_width)/2, window.h/3, self.button_width, self.button_height)
  # button_hard = pygame.Rect(((window.w/4) * 3) - (self.button_width/2), window.h/3, self.button_width, self.button_height)

  # pygame.draw.rect(screen, (255, 0, 0), button_easy)
  # pygame.draw.rect(screen, (255, 0, 0), button_medium)
  # pygame.draw.rect(screen, (255, 0, 0), button_hard)
  #
  # draw_text('Pong Not Pong', title_font, (255,255,255), screen, window.w/2, window.h/6)
  # draw_text('Easy', font, (255,255,255), screen, window.w/4, (self.button_height/2 + window.h/3))
  # draw_text('Medium', font, (255,255,255), screen, window.w/2, (self.button_height/2 + window.h/3))
  # draw_text('Hard', font, (255,255,255), screen, (window.w/4) * 3, (self.button_height/2 + window.h/3))
  #
  #
  # if button_easy.collidepoint((mx, my)):
  #   if self.click:
  #     self.player1_paddle_size = 400
  #     break
  # if button_medium.collidepoint((mx, my)):
  #   if self.click:
  #     self.player1_paddle_size = 200
  #     break
  # if button_hard.collidepoint((mx, my)):
  #   if self.click:
  #     self.player1_paddle_size = 40
  #     break
  #
  # self.click = False
  # for event in pygame.event.get():
  #   if event.type == pygame.QUIT:
  #     pygame.quit()
  #     sys.exit()
  #   if event.type == pygame.KEYDOWN:
  #     if event.key == pygame.K_ESCAPE:
  #       pygame.quit()
  #       sys.exit()
  #   if event.type == pygame.MOUSEBUTTONDOWN:
  #     if event.button == 1:
  #       self.click = True
  #
  # pygame.display.update()
  # clock.tick(60)

# while True:
#
#   screen.fill((0,0,0))
#
#   mx, my = pygame.mouse.get_pos()
#
#   button_low = pygame.Rect((window.w/4) - self.button_width / 2, window.h/3, self.button_width, self.button_height)
#   button_mid = pygame.Rect((window.w - self.button_width)/2, window.h/3, self.button_width, self.button_height)
#   button_high = pygame.Rect(((window.w/4) * 3) - (self.button_width/2), window.h/3, self.button_width, self.button_height)
#
#   pygame.draw.rect(screen, (255, 0, 0), button_low)
#   pygame.draw.rect(screen, (255, 0, 0), button_mid)
#   pygame.draw.rect(screen, (255, 0, 0), button_high)
#
#   draw_text('Select Max score:', title_font, (255,255,255), screen, window.w/2, window.h/6)
#   draw_text('2', font, (255,255,255), screen, window.w/4, (self.button_height/2 + window.h/3))
#   draw_text('5', font, (255,255,255), screen, window.w/2, (self.button_height/2 + window.h/3))
#   draw_text('7', font, (255,255,255), screen, (window.w/4) * 3, (self.button_height/2 + window.h/3))
#
#
#   if button_low.collidepoint((mx, my)):
#     if self.click:
#       self.max_score = 2
#       break
#   if button_mid.collidepoint((mx, my)):
#     if self.click:
#       self.max_score = 5
#       break
#   if button_high.collidepoint((mx, my)):
#     if self.click:
#       self.max_score = 7
#       break
#
#   self.click = False
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       pygame.quit()
#       sys.exit()
#     if event.type == pygame.KEYDOWN:
#       if event.key == pygame.K_ESCAPE:
#         pygame.quit()
#         sys.exit()
#     if event.type == pygame.MOUSEBUTTONDOWN:
#       if event.button == 1:
#         self.click = True
#
#   pygame.display.update()
#   clock.tick(60)

# while True:
#
#   screen.fill((0,0,0))
#
#   mx, my = pygame.mouse.get_pos()
#
#   button_restart = pygame.Rect((window.w/3) - self.button_width / 2, window.h/3, self.button_width, self.button_height)
#   button_exit = pygame.Rect((2*window.w/3) - self.button_width/2, window.h/3, self.button_width, self.button_height)
#
#   pygame.draw.rect(screen, (255, 0, 0), button_restart)
#   pygame.draw.rect(screen, (255, 0, 0), button_exit)
#
#   draw_text(winner_string, title_font, (255,255,255), screen, window.w/2, window.h/6)
#   draw_text('Restart', font, (255,255,255), screen, window.w/3, (self.button_height/2 + window.h/3))
#   draw_text('Exit', font, (255,255,255), screen, (2*window.w)/3, (self.button_height/2 + window.h/3))
#
#
#   if button_restart.collidepoint((mx, my)):
#     if self.click:
#       break
#   if button_exit.collidepoint((mx, my)):
#     if self.click:
#       pygame.quit()
#       sys.exit()
#       break
#
#   self.click = False
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       pygame.quit()
#       sys.exit()
#     if event.type == pygame.KEYDOWN:
#       if event.key == pygame.K_ESCAPE:
#         pygame.quit()
#         sys.exit()
#     if event.type == pygame.MOUSEBUTTONDOWN:
#       if event.button == 1:
#         self.click = True
#
#   pygame.display.update()
#   clock.tick(60)
