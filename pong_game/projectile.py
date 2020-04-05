import pygame, random
from pong_game.window import Window

class Projectile():

    def __init__(self, window):
        self.position = pygame.Rect(window.w/2 - 15, window.h/2 - 15, 30, 30)
        self.speed_x = 7
        self.speed_y = 7

    def ball_animation(self, player1, player2, ball, window):
      ball.x += self.speed_x
      ball.y += self.speed_y

      if ball.top <= window.score_size or ball.bottom >= window.h:
        self.speed_y *= -1

      if ball.left <= 0:
        player2.score += 1
        self.ball_restart(ball, window)

      if ball.right >= window.w:
        player1.score += 1
        self.ball_restart(ball, window)

      if ball.colliderect(player1.position) or ball.colliderect(player2.position):
        self.speed_y += 1
        self.speed_x += 1
        self.speed_x *= -1

    def ball_restart(self, ball, window):
      ball.center = (window.w/2, window.h/2)
      self.spee_x = random.choice((7, -7))
      self.spee_y = random.choice((7, -7))
