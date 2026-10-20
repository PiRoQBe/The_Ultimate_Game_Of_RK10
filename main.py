import pygame, sys
from random import randint

class Circle:
    GRAVITY = 0.3
    
    def __init__(self, pos) -> None:
        self.pose_x   = pos[0] + randint(-2, 2)
        self.pose_y   = pos[1] + randint(-2, 2)
        self.radius   = 2
        self.color = [randint(0, 255), randint(0, 255), randint(0, 255)]
        self.speedx   = randint(-10, 10)
        self.speedy   = randint(-10, 10)
        self.todelete = False 
    
    def update(self, window: pygame.Window) -> None:
        self.speedy += Circle.GRAVITY
        self.pose_x += self.speedx
        self.pose_y += self.speedy
        if (
            self.pose_x - self.radius < 0 or
            self.pose_x + self.radius > window.size[0] or
            self.pose_y + self.radius > window.size[1]
        ): self.todelete = True
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, (self.pose_x, self.pose_y), self.radius)        
                
def main():
    is_running = 1
    pygame.init()
    window = pygame.Window(size=(800, 800), title="Test circle faling", position=(10, 50))
    screen = window.get_surface()
    
    clock = pygame.time.Clock()
    
    circles = list()
    
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = 0
        
        if pygame.mouse.get_pressed()[0]:
            for i in range(5):
                circles.append(Circle(pygame.mouse.get_pos()))
        todelete = list()
        for p in circles:
            p.update(window)
            if p.todelete:
                todelete.append(p)
        for p in todelete:
            circles.remove(p)
        
        screen.fill("white")
        for p in circles:
            p.draw(screen)
            
        window.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    main()