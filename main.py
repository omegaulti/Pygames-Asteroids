import pygame
from constants import *
from logger import log_state
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from logger import log_event
import sys
from shot import *



def main():


    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    my_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 0)
    field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for a in asteroids:
            if a.collides_with(my_player) == True:
                log_event("player_hit")
                print("Game_over!")
                sys.exit()
        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        if my_player.cooldown > 0:
            my_player.cooldown -= dt
        pygame.display.flip()
        
        dt = clock.tick(60) /1000

if __name__ == "__main__":
    main()
