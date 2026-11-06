import sys
import time

# import config as cfg
from typing import Any, final

# from random import randint
import pygame

import characters


@final
class Game:
    FPS = 60
    deltatime = 1.0 / FPS
    SPAWN = 15
    WINDOW = pygame.Rect(0, 0, 1000, 600)
    all_sprites: pygame.sprite.Group[Any] = pygame.sprite.Group()

    def __init__(self) -> None:
        _init_game = pygame.init()
        self.window: pygame.Window = pygame.Window(
            size=self.WINDOW.size, title="Game ver 0.0.1"
        )
        self.screen: pygame.Surface = self.window.get_surface()
        self.clock: pygame.Clock = pygame.time.Clock()
        self.running = True
        self.counter = 0
        self.player_bullets: pygame.sprite.Group[Any] = pygame.sprite.Group()
        self.player: characters.Player = characters.Player(
            self.player_bullets, self.all_sprites
        )

    def run(self) -> None:
        time_prev = time.time()
        while self.running:
            self.watch_for_events()
            self.update()
            self.draw()
            _tick = self.clock.tick(self.FPS)
            time_curr = time.time()
            self.deltatime = time_curr - time_prev
            time_prev = time_curr

    def watch_for_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self) -> None:
        self.all_sprites.update(self.FPS / 1000)

    def draw(self) -> None:
        _screen_rect = self.screen.fill((255, 255, 255))
        _list_sprites = self.all_sprites.draw(self.screen)
        self.window.flip()


def main(game: Game) -> None:
    game.run()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    game = Game()
    main(game)
