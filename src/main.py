import pygame
import os
import random
from settings import *
from funciones_juego import *
from sprites import *

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("El Huevo Enmascarado")

SPRITE_WIDTH = 32
SPRITE_HEIGHT = 32
ROWS = 4
COLUMNS = 4

base_path = os.path.dirname(__file__)
eggmasked_path = os.path.join(base_path, "assets/eggmasked.png")
bg_spring_path = os.path.join(base_path, "assets/bg/primavera.png")
bg_autumn_path = os.path.join(base_path, "assets/bg/autumn.png")
knife_path = os.path.join(base_path, "assets/knife.png")

tiles_path = os.path.join(base_path, "assets/tiles/sheet (1).png")
tiles_image = pygame.image.load(tiles_path).convert_alpha()
tiles_sprites = load_sprites(tiles_image, 16, 16, 8, 7)
tiles_sprites_scaled = [pygame.transform.scale(tile, (100, 200)) for tile in tiles_sprites]


def cargar_sprites():  
    global load_sprites
    eggmasked = pygame.image.load(eggmasked_path).convert_alpha()
    knife = pygame.image.load(knife_path).convert_alpha()

    egg_sprites = load_sprites(eggmasked, SPRITE_WIDTH, SPRITE_HEIGHT, ROWS, COLUMNS)
    knife_sprites = load_sprites(knife, 30, 31.5, 2, 1)

    return {
        'egg': egg_sprites,
        'knife': knife_sprites
    }

sprites = cargar_sprites()
egg_sprite = sprites['egg']
knife_sprite = sprites['knife']
coin_images = []
for i in range(1, 10):
    coin_path = os.path.join(base_path, f"assets/coin/goldCoin{i}.png")
    coin_images.append(pygame.image.load(coin_path).convert_alpha())
    
def animate_coins():
    global coin_index
    coin_index += coin_animation_speed
    if coin_index >= len(coin_images):
        coin_index = 0
    return coin_images[int(coin_index)]

tile_size=200

def cuadricula(screen, tile_size, width, height, color=(255, 255, 255)):
    for linea in range(0, height // tile_size + 1):
        pygame.draw.line(screen, color, (0, linea * tile_size), (width, linea * tile_size))
    for linea in range(0, width // tile_size + 1):
        pygame.draw.line(screen, color, (linea * tile_size, 0), (linea * tile_size, height))

#  world_data = [
#     [1,1,1,1],
#     [0,0,0,0],
#     [tiles_sprites_scaled[0],0,1,1],
# ]

# Egg Animaciones
EGG_RESPIRACION = [egg_sprite[0],egg_sprite[1]]
EGG_CAMINAR = [egg_sprite[2],egg_sprite[1],egg_sprite[3]]
EGG_SALTO = [egg_sprite[4]]
EGG_CAIDA = [egg_sprite[6]]
EGG_ATAQUE= [egg_sprite[7],egg_sprite[8],egg_sprite[9]]
EGG_SALTO_ATAQUE = [egg_sprite[10],egg_sprite[11],egg_sprite[12]]
EGG_MUERTO = [egg_sprite[13],egg_sprite[14],egg_sprite[15]]

image_egg = EGG_RESPIRACION[1]
rect = image_egg.get_rect(center=(100, 100))

# Cuchiillo Animacion
knife_image = knife_sprite[0]
knife_image2 = knife_sprite[1]

platforms = [pygame.Rect(0, 400, 200, 20), pygame.Rect(400, 300, 200, 20)]
bg_spring = pygame.image.load(bg_spring_path)
bg_spring = pygame.transform.scale(bg_spring, SCREEN_SIZE)
bg_autumn = pygame.image.load(bg_autumn_path)
bg_autumn = pygame.transform.scale(bg_autumn, SCREEN_SIZE)

def main():
    global is_running,coins_puntos,salto_func,ataque_func,animacion_func,egg_roto,launch_projectile, clock,speed_y,speed_x, HEIGHT,suelo,dist_caida,y,screen,bg_x,scroll_speed,vidas,puntaje, image_egg,rect

    x=0
    
    coins_puntos(random.randint(1, 3))
    
    while is_running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    rect.y -= 100
                    y = rect.y
                    if suelo and not roto:
                        dist_caida = 0
                        suelo = False
                if event.key == pygame.K_a:
                    ataque_func()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rect.x -= 3
            x = rect.x
            animacion_func(EGG_CAMINAR,rect)
        if keys[pygame.K_RIGHT]:
            rect.x += 3
            x = rect.x
            animacion_func(EGG_CAMINAR,rect)
        
        if not roto:
            speed_y += 1
            if speed_y > 10:
                speed_y= 1
            y += speed_y
            rect.y = y
            x += speed_x
            rect.x = x
            
            if speed_y > 0:
                dist_caida += speed_y
                animacion_func(EGG_CAIDA,image_egg)
            elif speed_y < 0:
                animacion_func(EGG_SALTO,image_egg)
            else:
                dist_caida = 0
                if suelo:
                    if ataque:
                        animacion_func(EGG_ATAQUE,image_egg)
                        ataque=False
                    elif ataque_en_aire:
                        animacion_func(EGG_SALTO_ATAQUE,image_egg)
                        ataque_en_aire = False
                    else:
                        animacion_func(EGG_RESPIRACION,image_egg)
                
            if rect.bottom > HEIGHT:
                if dist_caida > 50:
                    egg_roto(rect,EGG_MUERTO,image_egg)
                rect.bottom = HEIGHT
                y = rect.y
                speed_y = 0
                suelo = True
            else:
                suelo = False
                
            for platform in platforms:
                if rect.colliderect(platform) and speed_y > 0:
                    speed_y = 0
                    y = platform.top - rect.height
                    rect.y = y
                    suelo = True
                    dist_caida = 0
                    
            for item in items[:]:
                if rect.colliderect(item):
                    items.remove(item)
                    puntaje += 10
                    if puntaje >= 100:
                        vidas += 1
                        puntaje -= 100
                        
            for cuchillo in cuchillos[:]:
                # if cuchillo.x < rect.x:
                #     cuchillo.x += 2
                # elif cuchillo.x > rect.x:
                #     cuchillo.x -= 2
                # if cuchillo.y < rect.y:
                #     cuchillo.y += 2
                # elif cuchillo.y > rect.y:
                #     cuchillo.y -= 2
                cuchillo.x -=2
                # cuchillo.y -=2
                if rect.colliderect(cuchillo):
                    vidas -= 1
                    cuchillos.remove(cuchillo)

            if random.randint(0, 100) < 2:
                launch_projectile()

            bg_x -= scroll_speed
            if bg_x <= -WIDTH:
                bg_x = 0
                
        else:
            egg_roto(rect,EGG_MUERTO,image_egg)
                    
        screen.blit(bg_autumn, (0, 0))
        # SCREEN.blit(bg_spring, (bg_x + SCREEN_SIZE[0], 0))
        # bg_x -= scroll_speed
        # if bg_x <= -WIDTH:
        #     bg_x = 0
                           
        for platform in platforms:
            pygame.draw.rect(screen, (0, 0, 0), platform)
        for item in items:
            screen.blit(animate_coins(), item.topleft)
        for cuchillo in cuchillos:
            screen.blit(knife_image, cuchillo.topleft)
        screen.blit(image_egg, rect)  
               
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {puntaje}", True, (0, 0, 0))
        lives_text = font.render(f"Lives: {vidas}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))
             
        cuadricula(screen,tile_size,WIDTH,HEIGHT)
        pygame.display.update()
        clock.tick(FPS)
                
if __name__ == "__main__":
    main()