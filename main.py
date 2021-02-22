import pygame

pygame.init()

# initializing window and loading images
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load("images/track1.png")
car = pygame.image.load("images/tesla.png")

carWidth = 30
carHeight = 60
carX = 150
carY = 280

camRadius = 5
camThickness = 5
camColor = (0, 255, 0)
camFocalDist = 20

car = pygame.transform.scale(car, (carWidth, carHeight))

clock = pygame.time.Clock()

while True:
    clock.tick(60)

    # camera at front of car
    camX = carX + carWidth / 2
    camY = carY + carWidth / 2

    # checking the path with white color
    upPixel = window.get_at((int(camX), int(camY) - camFocalDist))[0]
    if upPixel == 255:
        carY -= 1

    # drawing track, car and window
    window.blit(track, (0, 0))
    window.blit(car, (carX, carY))
    pygame.draw.circle(window, camColor, (camX, camY), camRadius, camThickness)

    pygame.display.update()
