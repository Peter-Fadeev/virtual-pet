import pygame
import images
import main
import pygame.freetype

class Knopki:
    def __init__(self, text, x, y, game):
        self.kartinka = images.button
        self.hitbox = pygame.Rect([x, y], self.kartinka.get_size())
        self.text = text
        self.game = game
        self.timeclick = 0
        self.shrift = pygame.freetype.Font("shrift.ttf", 28)
        kartinkaihitbox = self.shrift.render(text)
        self.kartinkatxt = kartinkaihitbox[0]
        self.hitboxtxt = kartinkaihitbox[1]
        self.hitboxtxt.center = self.hitbox.center
    def otrisovka(self):
        self.game.screen.blit(self.kartinka, self.hitbox)
        self.game.screen.blit(self.kartinkatxt, self.hitboxtxt)
              
    def click(self):
        self.kartinka = images.buttonclicked
        self.timeclick = pygame.time.get_ticks()
    def logic(self):
        if pygame.time.get_ticks() - self.timeclick >= 500:
            self.kartinka = images.button