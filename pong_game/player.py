import pygame
from pong_game.window import Window

class Player():

    def __init__(self, speed=0):
        self.speed = speed

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
