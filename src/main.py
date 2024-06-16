import pygame
from settings import *
from funciones_juego import *
from sprites import *

# pygame.init()
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
# pygame.display.set_caption("El Huevo Enmascarado")

clock = pygame.time.Clock()

def main():
    global is_running, clock
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    salto_func()
                if event.key == pygame.K_a:
                    ataque_func()                  
                
        pygame.display.flip()
        SCREEN.fill(WHITE)
        clock.tick(FPS)
                
if __name__ == "__main__":
    main()