import pygame

pygame.init()
Pantalla = pygame.display.set_mode((500, 500))
reloj = pygame.time.Clock()

x,y = 250, 250
velocidad = 5
Ejecutado = True

while Ejecutado:
    Pantalla.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Ejecutado = False

Teclas = pygame.Key.get_Pressed()

if Teclas[pygame.K_LEFT]:
    x -= velocidad
if Teclas[pygame.K_RIGHT]:
    x += velocidad
if Teclas[pygame.K_UP]:
    y -= velocidad
if Teclas[pygame.K_DOWN]:
    y += velocidad

pygame.draw.circle(Pantalla, (0,255,0), (x,y), 5)
pygame.display.update()
reloj.tick(30)
pygame.quit()