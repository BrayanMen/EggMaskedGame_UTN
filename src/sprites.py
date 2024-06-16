import pygame
import os
from settings import *
from funciones_juego import *

SPRITE_WIDTH = 32
SPRITE_HEIGHT = 32
ROWS = 4
COLUMNS = 4

base_path = os.path.dirname(__file__)
eggmasked_path = os.path.join(base_path, "assets/eggmasked.png")
knife_path = os.path.join(base_path, "assets/knife.png")

def load_sprites(png, width, height, rows, columns):
    sprites = []
    image_width, image_height = png.get_size()  # Obtener dimensiones de la imagen

    for row in range(rows):
        for col in range(columns):
            x = col * width
            y = row * height
            # Verificar si la subimagen está dentro de los límites de la imagen
            if x + width <= image_width and y + height <= image_height:
                sprite = png.subsurface(pygame.Rect(x, y, width, height))
                sprites.append(sprite)
            else:
                print(f"Advertencia: Subimagen fuera de los límites en fila {row}, columna {col}")

    return sprites

def cargar_sprites():
    pygame.init()
    pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("El Huevo Enmascarado")
    
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

# Egg Animaciones
EGG_RESPIRACION = [egg_sprite[0],egg_sprite[1]]
EGG_CAMINAR = [egg_sprite[2],egg_sprite[1],egg_sprite[3]]
EGG_SALTO = [egg_sprite[4]]
EGG_CAIDA = [egg_sprite[6]]
EGG_ATAQUE= [egg_sprite[7],egg_sprite[8],egg_sprite[9]]
EGG_SALTO_ATAQUE = [egg_sprite[10],egg_sprite[11],egg_sprite[12]]
EGG_MUERTO = [egg_sprite[13],egg_sprite[14],egg_sprite[15]]

image_egg = EGG_RESPIRACION[0]
rect = image_egg.get_rect(center=(x, y))

# Cuchiillo Animacion
KNIFE_LEFT = [knife_sprite[0]]
KNIFE_RIGHT = [knife_sprite[1]]
