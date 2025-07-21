import pygame
from constants import *
from player import *
from asteroidfield import *
from shot import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    i = 1

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    AsteroidField.containers = (updatable,)
    asteroid_field =  AsteroidField()
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable,drawable)
    
    shots = pygame.sprite.Group()
    Shot.containers = (shots,updatable,drawable)
    
    Player.containers = (updatable,drawable)
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)

  
    
    
    
    while i > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            
        screen.fill("black")
        updatable.update(dt)
        
        
        
        
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("GAME OVER!")
                pygame.quit()
                exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()
        
        
        
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000
    

    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
