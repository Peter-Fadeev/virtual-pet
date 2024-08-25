import pygame

import settings

fon = pygame.image.load("images/background.png")
fon = pygame.transform.scale(fon, [settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])

dog = pygame.image.load("images/dog.png")
dog = pygame.transform.scale(dog, [300, 450])

money = pygame.image.load("images/money.png")
money = pygame.transform.scale(money, [100, 100])

golod = pygame.image.load("images/satiety.png")
golod = pygame.transform.scale(golod, [100, 100])

radost = pygame.image.load("images/happiness.png")
radost = pygame.transform.scale(radost, [100, 100])

hp = pygame.image.load("images/health.png")
hp = pygame.transform.scale(hp, [100, 100])

button = pygame.image.load("images/button.png")
button = pygame.transform.scale(button, [250, 75] )

buttonclicked = pygame.image.load("images/button_clicked.png")
buttonclicked = pygame.transform.scale(buttonclicked, [250, 75] )