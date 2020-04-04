import pygame

class Player():

    def __init__(self, speed=0):
        self.speed = speed

    def player_animation(self, player):
      score_section = 100
      screen_width = 1280
      screen_height = 960
      player.y += self.speed
      if player.top <= score_section:
        player.top = score_section
      if player.bottom >= screen_height:
        player.bottom = screen_height

    def opponent_ai(self, opponent, ball):
      score_section = 100
      screen_width = 1280
      screen_height = 960
      if opponent.top < ball.y:
        opponent.top += self.speed
      if opponent.bottom > ball.y:
        opponent.bottom -= self.speed
      if opponent.top <= score_section:
        opponent.top = score_section
      if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
