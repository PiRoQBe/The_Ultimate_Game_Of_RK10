import pygame, sys, time
from random import randint
import config as cfg
import characters

class Game:
    FPS = 60
    DELTATIME = 1.0 / FPS
    SPAWN = 15
    WINDOW = pygame.Rect(0, 0, 1000, 600)
    all_sprites = pygame.sprite.Group()
    
    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.Window(size=self.WINDOW.size, title="Game ver 0.0.1")
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()
        self.running = True
        self.counter = 0
        self.player = characters.Player(self.all_sprites)
    
    def run(self) -> None:
        time_prev = time.time()
        while self.running:
            self.watch_for_events()
            self.update()
            self.draw()
            self.clock.tick(self.FPS)
            time_curr = time.time()
            self.DELTATIME = time_curr - time_prev
            time_prev = time_curr
            
    def watch_for_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self) -> None:
        self.all_sprites.update(self.FPS / 1000)
        
    
    def draw(self) -> None:
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        self.window.flip()        
        
def main(game: Game) -> None:
    game.run()
    pygame.quit()
    sys.exit()

if  __name__ == "__main__":
    game = Game()
    main(game)
    