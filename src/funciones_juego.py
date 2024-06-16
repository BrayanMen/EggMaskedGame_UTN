import pygame
import random
from settings import *
from sprites import *


def animacion_func(frames):
    global image, siguiente_frame, animacion_speed, ataque, ataque_en_aire
    siguiente_frame += animacion_speed
    if siguiente_frame >= len(frames):
        siguiente_frame = 0
        ataque = False
        ataque_en_aire = False
    image = frames[int(siguiente_frame)]
    
def salto_func():
    global speed, dist_caida, suelo, roto
    if suelo and not roto:
        speed = -15
        dist_caida = 0
        suelo = False
        
def egg_roto():
    global roto
    roto = True
    
def ataque_func():
    global ataque, ataque_en_aire
    if not roto and not ataque_en_aire:
        if suelo:
            ataque = True
        else:
            ataque_en_aire = True
            
# Función para generar coins
def coins_puntos(num_items):
    global SPRITE_HEIGHT, SPRITE_WIDTH, items
    for _ in range(num_items):
        item_x = random.randint(0, WIDTH - SPRITE_WIDTH)
        item_y = random.randint(0, HEIGHT - SPRITE_HEIGHT)
        items.append(pygame.Rect(item_x, item_y, SPRITE_WIDTH, SPRITE_HEIGHT))

# Función para generar enemigos
def spawn_enemies(num_enemies):
    global SPRITE_HEIGHT, SPRITE_WIDTH, enemigos
    for _ in range(num_enemies):
        enemy_x = random.randint(0, WIDTH - SPRITE_WIDTH)
        enemy_y = random.randint(0, HEIGHT - SPRITE_HEIGHT)
        enemigos.append(pygame.Rect(enemy_x, enemy_y, SPRITE_WIDTH, SPRITE_HEIGHT))

# Función para lanzar cubiertos
def launch_projectile():
    global cuchillos, SPRITE_HEIGHT, SPRITE_WIDTH
    proj_x = random.randint(0, WIDTH - SPRITE_WIDTH)
    cuchillos.append(pygame.Rect(proj_x, 0, SPRITE_WIDTH, SPRITE_HEIGHT))