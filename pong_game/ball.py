import pygame

class Ball():
  def __init__(self):
    self = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)

  def ball_animation():
    global ball_speed_x, ball_speed_y, playerA_score, playerB_score
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