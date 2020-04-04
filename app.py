import pygame, sys
from pong_game.projectile import Projectile
from pong_game.player import Player
from pong_game.window import Window

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
pygame.display.set_caption("Z~P~ $$$$$$$")

window = Window()

# Game Rectangles
player = pygame.Rect(window.w - 20, window.h/2 -70, 10, 140)
opponent = pygame.Rect(10, window.h/2 - 70, 10, 140)

projectile = Projectile()
player_real = Player()
player_cpu = Player(10)

ball = pygame.Rect(window.w/2 - 15, window.h/2 - 15, 30, 30)

bg_color = pygame.Color('grey12')
orange = (255,165,0)

# Game scores
player_1 = input("Enter your name: ")
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
        player_real.speed += 7
      if event.key == pygame.K_UP:
        player_real.speed -= 7

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_DOWN:
        player_real.speed -= 7
      if event.key == pygame.K_UP:
        player_real.speed += 7

    if event.type == pygame.VIDEORESIZE:
      window.resize(event.w, event.h)
      player = pygame.Rect(window.w - 20, window.h/2 -70, 10, 140)
      opponent = pygame.Rect(10, window.h/2 - 70, 10, 140)

  projectile.ball_animation(player, opponent, ball, window)
  player_real.player_animation(player, window)
  player_cpu.opponent_ai(opponent, ball, window)

  # Visuals
  window.game_display.fill(bg_color)
  pygame.draw.rect(window.game_display,orange, player)
  pygame.draw.rect(window.game_display,orange, opponent)
  pygame.draw.ellipse(window.game_display,orange, ball)
  pygame.draw.aaline(window.game_display, orange, (window.w/2, 0), (window.w/2,window.h))
  pygame.draw.aaline(window.game_display, orange, (window.w ,window.score_size), (0,window.score_size))
  font = pygame.font.Font(None, 74)
  text = font.render(str(f"Computer - {playerA_score}"), 1, orange)
  window.game_display.blit(text, (window.w / 6, 25))
  text = font.render(str(f"{player_1} - {playerB_score}"), 1, orange)
  window.game_display.blit(text, ((window.w / 6) * 4, 25))

  # Updating the window
  pygame.display.flip()
  clock.tick(60)
