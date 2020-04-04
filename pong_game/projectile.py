import pygame, random

class Projectile():

    def __init__(self):
        screen_width = 1280
        screen_height = 960
        self.speed_x = 7
        self.speed_y = 7

    def ball_animation(self, player, opponent, ball):

      score_section = 100
      screen_width = 1280
      screen_height = 960

      ball.x += self.speed_x
      ball.y += self.speed_y

      if ball.top <= score_section or ball.bottom >= screen_height:
        self.speed_y *= -1

      if ball.left <= 0:
        # playerB_score += 1
        self.ball_restart(ball)

      if ball.right >= screen_width:
        # playerA_score += 1
        self.ball_restart(ball)

      if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_y += 1
        ball_speed_x += 1
        ball_speed_x *= -1

    def ball_restart(self, ball):
      screen_width = 1280
      screen_height = 960
      ball.center = (screen_width/2, screen_height/2)
      self.spee_x = random.choice((7, -7))
      self.spee_y = random.choice((7, -7))
