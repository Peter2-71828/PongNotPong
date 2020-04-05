import pygame, sys
from pong_game.projectile import Projectile
from pong_game.player import Player
from pong_game.window import Window

pygame.init()
pygame.display.set_caption("Pong Not Pong")
clock = pygame.time.Clock()

window = Window()

projectile = Projectile(window)
ball = projectile.position

player1_name = input("Enter your name: ")
player1 = Player(window, window.w - 20, player1_name)

player2 = Player(window, 10, 'cpu', 10)

while True:
  # Handling input
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN:
        player1.speed += 7
      if event.key == pygame.K_UP:
        player1.speed -= 7

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_DOWN:
        player1.speed -= 7
      if event.key == pygame.K_UP:
        player1.speed += 7

    if event.type == pygame.VIDEORESIZE:
      window.resize(event.w, event.h)
      player1.update_player(window, window.w - 20)
      player2.update_player(window, 10)

  projectile.ball_animation(player1, player2, ball, window)
  player1.player_animation(player1.position, window)
  player2.opponent_ai(player2.position, ball, window)

  window.update_display(player1, player2, ball)

  # Updating the window
  pygame.display.flip()
  clock.tick(60)
