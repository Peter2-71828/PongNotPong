import pygame, random

score_section = 100
screen_width = 1280
screen_height = 960
ball_speed_x = 7
ball_speed_y = 7

def ball_restart(ball):
  ball.center = (screen_width/2, screen_height/2)
  ball_speed_x = 7
  ball_speed_y = 7
  ball_speed_y *= random.choice((1, -1))
  ball_speed_x *= random.choice((1, -1))

def ball_animation(player, opponent, ball):

  score_section = 100
  screen_width = 1280
  screen_height = 960
  ball_speed_x = 7
  ball_speed_y = 7

  ball.x += ball_speed_x
  ball.y += ball_speed_y

  if ball.top <= score_section or ball.bottom >= screen_height:
    ball_speed_y *= -1

  if ball.left <= 0:
    # playerB_score += 1
    ball_restart(ball)

  if ball.right >= screen_width:
    # playerA_score += 1
    ball_restart(ball)

  if ball.colliderect(player) or ball.colliderect(opponent):
    ball_speed_y += 1
    ball_speed_x += 1
    ball_speed_x *= -1
