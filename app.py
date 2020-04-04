import pygame, sys, random
from pong_game.ball import ball, ball_animation

def player_animation():
  player.y += player_speed
  if player.top <= score_section:
    player.top = score_section
  if player.bottom >= screen_height:
    player.bottom = screen_height

def opponent_ai():
  if opponent.top < ball.y:
    opponent.top += opponent_speed
  if opponent.bottom > ball.y:
    opponent.bottom -= opponent_speed
  if opponent.top <= score_section:
    opponent.top = score_section
  if opponent.bottom >= screen_height:
    opponent.bottom = screen_height

def ball_restart():
  global ball_speed_y, ball_speed_x
  ball.center = (screen_width/2, screen_height/2)
  ball_speed_x = 7
  ball_speed_y = 7
  ball_speed_y *= random.choice((1, -1))
  ball_speed_x *= random.choice((1, -1))

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

  ball_animation()
  player_animation()
  opponent_ai()

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
