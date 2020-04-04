import pygame

score_section = 100
screen_width = 1280
screen_height = 960
ball_speed_x = 7
ball_speed_y = 7
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 -70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

def ball_animation():
  ball.x += ball_speed_x
  ball.y += ball_speed_y

if ball.top <= score_section or ball.bottom >= screen_height:
  ball_speed_y *= -1

if ball.left <= 0:
  playerB_score += 1
  ball_restart()

if ball.right >= screen_width:
  playerA_score += 1
  ball_restart()

if ball.colliderect(player) or ball.colliderect(opponent):
  ball_speed_y += 1
  ball_speed_x += 1
  ball_speed_x *= -1
