import pygame, sys
import time
from pong_game.player import Player
from pong_game.window import Window


class Menu():

  def __init__(self, player1_paddle_size = 200, max_score = 5):
    self.player1_paddle_size = player1_paddle_size
    self.max_score = max_score

  def main_menu(self, window):
    click = False
    button_width = 250
    button_height = 200
    screen = pygame.display.set_mode((window.w, window.h),0,32)
    font = pygame.font.SysFont(None, 80)
    title_font = pygame.font.SysFont(None, 100)
    clock = pygame.time.Clock()

    def draw_text(text, font, color, surface, x, y):
      textobj = font.render(text, 1, color)
      textrect = textobj.get_rect()
      textrect.center = (x, y)
      surface.blit(textobj, textrect)

    while True:

      screen.fill((0,0,0))

      mx, my = pygame.mouse.get_pos()

      button_easy = pygame.Rect((window.w/4) - button_width / 2, window.h/3, button_width, button_height)
      button_medium = pygame.Rect((window.w - button_width)/2, window.h/3, button_width, button_height)
      button_hard = pygame.Rect(((window.w/4) * 3) - (button_width/2), window.h/3, button_width, button_height)

      pygame.draw.rect(screen, (255, 0, 0), button_easy)
      pygame.draw.rect(screen, (255, 0, 0), button_medium)
      pygame.draw.rect(screen, (255, 0, 0), button_hard)

      draw_text('Pong Not Pong', title_font, (255,255,255), screen, window.w/2, window.h/6)
      draw_text('Easy', font, (255,255,255), screen, window.w/4, (button_height/2 + window.h/3))
      draw_text('Medium', font, (255,255,255), screen, window.w/2, (button_height/2 + window.h/3))
      draw_text('Hard', font, (255,255,255), screen, (window.w/4) * 3, (button_height/2 + window.h/3))


      if button_easy.collidepoint((mx, my)):
        if click:
          self.player1_paddle_size = 400
          break
      if button_medium.collidepoint((mx, my)):
        if click:
          self.player1_paddle_size = 200
          break
      if button_hard.collidepoint((mx, my)):
        if click:
          self.player1_paddle_size = 40
          break

      click = False
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
            click = True

      pygame.display.update()
      clock.tick(60)

  def score_menu(self, window):
    click = False
    window.w = window.w
    window.h = window.h
    button_width = 250
    button_height = 200
    screen = pygame.display.set_mode((window.w, window.h),0,32)
    font = pygame.font.SysFont(None, 80)
    title_font = pygame.font.SysFont(None, 100)
    clock = pygame.time.Clock()

    while True:

      screen.fill((0,0,0))

      mx, my = pygame.mouse.get_pos()

      button_low = pygame.Rect((window.w/4) - button_width / 2, window.h/3, button_width, button_height)
      button_mid = pygame.Rect((window.w - button_width)/2, window.h/3, button_width, button_height)
      button_high = pygame.Rect(((window.w/4) * 3) - (button_width/2), window.h/3, button_width, button_height)

      pygame.draw.rect(screen, (255, 0, 0), button_low)
      pygame.draw.rect(screen, (255, 0, 0), button_mid)
      pygame.draw.rect(screen, (255, 0, 0), button_high)

      draw_text('Select Max score:', title_font, (255,255,255), screen, window.w/2, window.h/6)
      draw_text('2', font, (255,255,255), screen, window.w/4, (button_height/2 + window.h/3))
      draw_text('5', font, (255,255,255), screen, window.w/2, (button_height/2 + window.h/3))
      draw_text('7', font, (255,255,255), screen, (window.w/4) * 3, (button_height/2 + window.h/3))


      if button_low.collidepoint((mx, my)):
        if click:
          self.max_score = 2
          break
      if button_mid.collidepoint((mx, my)):
        if click:
          self.max_score = 5
          break
      if button_high.collidepoint((mx, my)):
        if click:
          self.max_score = 7
          break

      click = False
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
            click = True

      pygame.display.update()
      clock.tick(60)

  def winner_menu(self, window, winner):
    winner_string = '{} is the winner!'.format(winner)
    click = False
    button_width = 250
    button_height = 200
    screen = pygame.display.set_mode((window.w, window.h),0,32)
    font = pygame.font.SysFont(None, 80)
    title_font = pygame.font.SysFont(None, 100)
    clock = pygame.time.Clock()

    def draw_text(text, font, color, surface, x, y):
      textobj = font.render(text, 1, color)
      textrect = textobj.get_rect()
      textrect.center = (x, y)
      surface.blit(textobj, textrect)

    while True:

      screen.fill((0,0,0))

      mx, my = pygame.mouse.get_pos()

      button_restart = pygame.Rect((window.w/3) - button_width / 2, window.h/3, button_width, button_height)
      button_exit = pygame.Rect((2*window.w/3) - button_width/2, window.h/3, button_width, button_height)

      pygame.draw.rect(screen, (255, 0, 0), button_restart)
      pygame.draw.rect(screen, (255, 0, 0), button_exit)

      draw_text(winner_string, title_font, (255,255,255), screen, window.w/2, window.h/6)
      draw_text('Restart', font, (255,255,255), screen, window.w/3, (button_height/2 + window.h/3))
      draw_text('Exit', font, (255,255,255), screen, (2*window.w)/3, (button_height/2 + window.h/3))


      if button_restart.collidepoint((mx, my)):
        if click:
          break
      if button_exit.collidepoint((mx, my)):
        if click:
          pygame.quit()
          sys.exit()
          break

      click = False
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
            click = True

      pygame.display.update()
      clock.tick(60)
