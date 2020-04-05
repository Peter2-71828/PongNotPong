import pygame

score_section = 100
screen_width = 1280
screen_height = 960
player_speed = 0
opponent_speed = 10

def player_animation(player):
  player.y += player_speed
  if player.top <= score_section:
    player.top = score_section
  if player.bottom >= screen_height:
    player.bottom = screen_height

def opponent_ai(opponent, ball):
  if opponent.top < ball.y:
    opponent.top += opponent_speed
  if opponent.bottom > ball.y:
    opponent.bottom -= opponent_speed
  if opponent.top <= score_section:
    opponent.top = score_section
  if opponent.bottom >= screen_height:
    opponent.bottom = screen_height
