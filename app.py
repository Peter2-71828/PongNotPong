import pygame, sys
from pong_game.projectile import Projectile
from pong_game.player import Player
from pong_game.window import Window
# from tracking.object_tracker import movement


pygame.init()
pygame.display.set_caption("Pong Not Pong")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 20)
window = Window()
window_width = 1280
window_height = 960
button_width = 500
button_height = 250

screen = pygame.display.set_mode((window_width, window_height),0,32)

projectile = Projectile(window)
ball = projectile.position

# player1_name = input("Enter your name: ")
player1 = Player(window, window.w - 20, 'Player')

player2 = Player(window, 10, 'cpu', 10)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False

def main_menu():
    while True:
 
        screen.fill((0,0,0))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect((window_width - button_width)/2, window_height/3, button_width, button_height)
        button_2 = pygame.Rect((window_width - button_width)/2, 2*window_height/3, button_width, button_height)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
 
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    game()
 
        pygame.display.update()
        clock.tick(60)

def game():
  while True:
    # movement()
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


main_menu()