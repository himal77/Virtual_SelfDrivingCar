import pygame

pygame.init()

# initializing window and loading images
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load("images/track3.png")
car = pygame.image.load("images/tesla.png")

carWidth = 30
carHeight = 60
carX = 150
carY = 280

camRadius = 5
camThickness = 5
camColor = (0, 255, 0)
camFocalDist = 20
camOffsetX = 0
camOffsetY = 0

car = pygame.transform.scale(car, (carWidth, carHeight))

clock = pygame.time.Clock()

isDriving = True
direction = 'up'

while isDriving:
    # to stop if we click in exit button in window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDriving = False

    clock.tick(60)

    # camera at front of car
    camX = carX + camOffsetX + carWidth / 2
    camY = carY + camOffsetY + carWidth / 2

    # checking the path with white color in four direction
    upPixel = window.get_at((int(camX), int(camY) - camFocalDist))[0]
    downPixel = window.get_at((int(camX), int(camY) + camFocalDist))[0]
    rightPixel = window.get_at((int(camX) + camFocalDist, int(camY)))[0]
    leftPixel = window.get_at((int(camX) - camFocalDist, int(camY)))[0]

    # take direction
    if direction == 'up' and upPixel != 255 and rightPixel == 255:
        direction = 'right'
        car = pygame.transform.rotate(car, -90)
        camOffsetX = 30

    # driving
    if direction == 'up' and upPixel == 255:
        carY -= 1
    elif direction == 'right' and rightPixel == 255:
        carX += 1

    # drawing track, car and window
    window.blit(track, (0, 0))
    window.blit(car, (carX, carY))
    pygame.draw.circle(window, camColor, (camX, camY), camRadius, camThickness)

    pygame.display.update()
