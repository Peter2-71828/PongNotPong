import pygame, sys
from pong_game.projectile import Projectile
from pong_game.player import Player
from pong_game.window import Window
from pong_game.user_in import move
from pong_game.menu import Menu
from tracking.object_tracker import movement
from multiprocessing import Process, Queue
import multiprocessing as mp
import time

if __name__ == '__main__':
  mp.set_start_method('spawn')
  q = Queue()
  p = Process(target=movement, args=(q,))
  p.start()

  pygame.init()
  pygame.display.set_caption("Pong Not Pong")
  clock = pygame.time.Clock()
  window = Window()

  projectile = Projectile(window)
  ball = projectile.position

  menu = Menu()
  menu.main_menu(window)

  player1 = Player(window, window.w - 20, 'Player', menu.player1_paddle_size)
  player2 = Player(window, 10, 'cpu', 100, 10)

  # player1_name = input("Enter your name: ")

  while True:
    print(f"player1 = {player1.score}, player2 = {player2.score}")
    position = q.get()
    move(position, player1, player2)

    projectile.ball_animation(player1, player2, ball, window)
    player1.player_animation(player1.position, window)
    player2.opponent_ai(player2.position, ball, window)

    window.update_display(player1, player2, ball)

    player1.speed = player1.speed/2

    pygame.display.flip()
    clock.tick(60)
