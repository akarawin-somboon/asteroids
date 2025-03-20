import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # 1. Create the groups first
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # 2. Set the containers for the Player class
    Player.containers = (updatable, drawable)
    
    # 3. Create the player instance after setting containers
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # 4. Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

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

if __name__ == "__main__":
    main()
