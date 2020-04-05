import pygame, sys
from pong_game.projectile import Projectile
from pong_game.player import Player
from pong_game.window import Window

pygame.init()
pygame.display.set_caption("Pong Not Pong")
clock = pygame.time.Clock()

window = Window()
projectile = Projectile()
player1 = Player(window, (window.w - 20))
player2 = Player(window, 10, 10)

ball = pygame.Rect(window.w/2 - 15, window.h/2 - 15, 30, 30)

bg_color = pygame.Color('grey12')
orange = (255,165,0)

# Game scores
player1_name = input("Enter your name: ")
playerA_score = 0
playerB_score = 0

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
      player1.update()
      player2.update()

  projectile.ball_animation(player1.position, player2.position, ball, window)
  player1.player_animation(player1.position, window)
  player2.opponent_ai(player2.position, ball, window)

  # Visuals
  window.game_display.fill(bg_color)
  pygame.draw.rect(window.game_display,orange, player1.position)
  pygame.draw.rect(window.game_display,orange, player2.position)
  pygame.draw.ellipse(window.game_display,orange, ball)
  pygame.draw.aaline(window.game_display, orange, (window.w/2, 0), (window.w/2,window.h))
  pygame.draw.aaline(window.game_display, orange, (window.w ,window.score_size), (0,window.score_size))
  font = pygame.font.Font(None, 74)
  text = font.render(str(f"Computer - {playerA_score}"), 1, orange)
  window.game_display.blit(text, (window.w / 6, 25))
  text = font.render(str(f"{player1_name} - {playerB_score}"), 1, orange)
  window.game_display.blit(text, ((window.w / 6) * 4, 25))

  # Updating the window
  pygame.display.flip()
  clock.tick(60)
