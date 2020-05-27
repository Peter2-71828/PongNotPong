import pygame, sys
from pong_game.player import Player

def move(position, player1, player2, window):
    if position <= 90:
        player1.speed -= 7

    if position >= 110:
        player1.speed += 7

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
