import pygame
from pong_game.window import Window
from pong_game.projectile import Projectile

class Player():

    def __init__(self, window, x_position, name, speed=0):
        self.position = pygame.Rect(x_position, window.h/2 -70, 10, window.h/7)
        self.speed = speed
        self.name = name
        self.score = 0

    def change_score(score = 1):
        self.score += score

    def update_player(self, window, x_position):
        self.position = pygame.Rect(x_position, window.h/2 -70, 10, window.h/7)

    def player_animation(self, player, window):
      player.y += self.speed
      if player.top <= window.score_size:
        player.top = window.score_size
      if player.bottom >= window.h:
        player.bottom = window.h

    def opponent_ai(self, opponent, ball, window):
      if opponent.top < ball.y:
        opponent.top += self.speed
      if opponent.bottom > ball.y:
        opponent.bottom -= self.speed
      if opponent.top <= window.score_size:
        opponent.top = window.score_size
      if opponent.bottom >= window.h:
        opponent.bottom = window.h
