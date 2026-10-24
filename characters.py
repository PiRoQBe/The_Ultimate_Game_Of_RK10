import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups) -> None:
        super().__init__(*groups)
        
        self.image = pygame.image.load("img/Player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_frect(bottomleft = (50,550))
        
        self.speed = 75
    
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        move = pygame.Vector2((keys[pygame.K_d] - keys[pygame.K_a]), 0)
        if move.length() > 0:
            self.rect.center += move.normalize() * self.speed * dt
    
    def get_plater_pos(self) -> pygame.Vector2:
        return self.rect.center
    
class Bullet(pygame.sprite.Sprite):
    def __init__(self, player_pos: pygame.Vector2, *groups) -> None:
        super().__init__(*groups)
        
        self.image = pygame.image.load("img/Bullet.png").convert_alpha()
        self.rect = self.image.get_rect(bottom=player_pos)

        self.speed = 200
        
    def update(self, dt) -> None:
        move = pygame.Vector2(0, 1)
        self.rect.center += move.normalize() * self.speed * dt