import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups) -> None:
        super().__init__(*groups)
        
        self.image = pygame.image.load("img/Player.png").convert_alpha()
        # self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(leftbottom = (50, 50))
        
        self.speed = 30
    
        