import pygame, sys
from pong_game.projectile import Projectile
from pong_game.player import Player
from pong_game.window import *

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Z~P~ $$$$$$$")

# Game Rectangles
player = pygame.Rect(screen_width - 20, screen_height/2 -70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

projectile = Projectile()
player_real = Player()
player_cpu = Player(10)

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)

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

  projectile.ball_animation(player, opponent, ball)
  player_real.player_animation(player)
  player_cpu.opponent_ai(opponent, ball)

  # Visuals
  screen.fill(bg_color)
  pygame.draw.rect(screen,orange, player)
  pygame.draw.rect(screen,orange, opponent)
  pygame.draw.ellipse(screen,orange, ball)
  pygame.draw.aaline(screen, orange, (screen_width/2, 0), (screen_width/2,screen_height))
  pygame.draw.aaline(screen, orange, (screen_width ,score_section), (0,score_section))
  font = pygame.font.Font(None, 74)
  text = font.render(str(f"Computer - {playerA_score}"), 1, orange)
  screen.blit(text, (screen_width / 6, 25))
  text = font.render(str(f"{player_1} - {playerB_score}"), 1, orange)
  screen.blit(text, ((screen_width / 6) * 4, 25))

  # Updating the window
  pygame.display.flip()
  clock.tick(60)
