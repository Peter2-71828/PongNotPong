import pygame, sys, random
from pong_game.ball_actions import ball_restart, ball_animation
from pong_game.paddle import player_animation, opponent_ai

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 960
score_section = 100
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Z~P~ $$$$$$$")

# Game Rectangles
player = pygame.Rect(screen_width - 20, screen_height/2 -70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)

bg_color = pygame.Color('grey12')
orange = (255,165,0)

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 10

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
        player_speed += 7
      if event.key == pygame.K_UP:
        player_speed -= 7

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_DOWN:
        player_speed -= 7
      if event.key == pygame.K_UP:
        player_speed += 7

  ball_animation(player, opponent, ball)
  player_animation(player)
  opponent_ai(opponent, ball)

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
