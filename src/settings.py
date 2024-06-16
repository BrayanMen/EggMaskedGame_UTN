WIDTH = 800
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)
x = WIDTH // 2
y = HEIGHT // 2

# Frame per Second
FPS = 60

WHITE = (255, 255, 255)

# Variables globales para el juego
speed = 0
dist_caida = 0
frame_index = 0
animacion_speed = 0.1
siguiente_frame = 0
puntaje = 0
vidas = 3

# Estados del juego
suelo = False
roto = False
ataque = False
ataque_en_aire = False
is_running = True

# Listas para elementos del juego
items = []
enemigos = []
cuchillos = []