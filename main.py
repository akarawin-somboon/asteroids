import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # 1. Create the groups first
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    # 2. Set the containers for the Player class
    Player.containers = (updatable, drawable)
    
    # 3. Create the player instance after setting containers
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable,)

    # Create an asteroid field
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    # 4. Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player.shoot()

        # Clear screen
        screen.fill("black")
        
        # Draw all sprites in drawable group
        for sprite in drawable:
            sprite.draw(screen)
        
        # Update display
        pygame.display.flip()

        # Calculate time delta and update all sprites
        dt = clock.tick(60) / 1000
        updatable.update(dt)

        for asteroid in asteroids:
            if player.checkCollision(asteroid):
                print("Game over!")
                import sys
                sys.exit()

if __name__ == "__main__":
    main()
