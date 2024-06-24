import pygame
import random
from settings import *
from sprites import *

def load_sprites(png, width, height, rows, columns):
    sprites = []
    image_width, image_height = png.get_size()

    for row in range(rows):
        for col in range(columns):
            x = col * width
            y = row * height
            
            if x + width <= image_width and y + height <= image_height:
                sprite = png.subsurface(pygame.Rect(x, y, width, height))
                sprites.append(sprite)
            else:
                print(f"Advertencia: Subimagen fuera de los límites en fila {row}, columna {col}")

    return sprites

def animacion_func(frames, image_frame):
    global siguiente_frame, animacion_speed, ataque, ataque_en_aire
    image_frame
    siguiente_frame += animacion_speed
    if siguiente_frame >= len(frames):
        siguiente_frame = 0
        ataque = False
        ataque_en_aire = False
    image_frame = frames[int(siguiente_frame)]
    
def salto_func():
    global speed_y, dist_caida, suelo, roto
    if suelo and not roto:
        speed_y = -20
        dist_caida = 0
        suelo = False
        
def egg_roto(rect, frames, img_frame):
    global roto, vidas
    roto = True
    vidas -= 1
    if vidas > 0:
        rect.center = (WIDTH // 2, HEIGHT // 2)
        roto = False
    else:
        animacion_func(frames,img_frame)
        print("Game Over")
    
def ataque_func():
    global ataque, ataque_en_aire
    if not roto and not ataque_en_aire:
        if suelo:
            ataque = True
        else:
            ataque_en_aire = True
            
def coins_puntos(num_items):
    from main import platforms
    SPRITE_WIDTH = 32
    SPRITE_HEIGHT = 32
    global  items
    for platform in platforms:
        for _ in range(num_items):
            item_x = random.randint(platform.left, platform.right)
            item_y = platform.top - random.randint(30, 100)
            items.append(pygame.Rect(item_x, item_y, SPRITE_WIDTH, SPRITE_HEIGHT))

def spawn_enemies(num_enemies):
    SPRITE_WIDTH = 32
    SPRITE_HEIGHT = 32
    global enemigos
    for _ in range(num_enemies):
        enemy_x = random.randint(0, WIDTH - SPRITE_WIDTH)
        enemy_y = random.randint(0, HEIGHT - SPRITE_HEIGHT)
        enemigos.append(pygame.Rect(enemy_x, enemy_y, SPRITE_WIDTH, SPRITE_HEIGHT))

def launch_projectile():
    SPRITE_WIDTH = 32
    SPRITE_HEIGHT = 32
    global cuchillos
    proj_x = random.randint(799,WIDTH)
    cuchillo = pygame.Rect(proj_x, random.randint(120, HEIGHT-50), SPRITE_WIDTH, SPRITE_HEIGHT)
    cuchillos.append(cuchillo)
    
