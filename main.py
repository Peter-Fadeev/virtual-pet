import pygame as pg
import settings
import images
import dog
import pygame.freetype
import characters
import random
import knopki

# Инициализация pg
pg.init()

# Размеры окна

class Game:
    def __init__(self):

        # Создание окна
        self.screen = pg.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pg.display.set_caption("Виртуальный питомец")

        self.c = True

        self.dog = dog.Dog(self)

        self.money = characters.Characters(self, images.money, 35, 50, 0)
        self.golod = characters.Characters(self, images.golod, 35, 150, 100)        
        self.radost = characters.Characters(self, images.radost, 35, 250, 100)
        self.hp = characters.Characters(self, images.hp, 35, 350, 100)

        self.sobitiegolod = pg.USEREVENT
        self.sobitieradost = pg.USEREVENT + 1
        self.sobitiehp = pg.USEREVENT + 2

        pygame.time.set_timer(self.sobitiegolod, random.randint(5000, 20000))
        pygame.time.set_timer(self.sobitieradost, random.randint(10000, 25000))
        pygame.time.set_timer(self.sobitiehp, random.randint(5000, 15000))

        self.buttonfood = knopki.Knopki("еда", 630, 50, self)
        self.buttonclothes = knopki.Knopki("одежда", 630, 175, self)
        self.buttonigra = knopki.Knopki("игра", 630, 300, self)
        self.buttonupgrades = knopki.Knopki("улучшения", 630, 425, self)

        self.buttons = [self.buttonfood, self.buttonclothes, self.buttonigra, self.buttonupgrades]
        self.run()

    def run(self):
        while self.c:
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.c = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.dog.hitbox.collidepoint(event.pos) == True:
                    self.money.chislo = self.money.chislo + 1
                for button in self.buttons:
                    if button.hitbox.collidepoint(event.pos) == True:
                        button.click()
            if event.type == self.sobitiegolod:
                self.golod.chislo = self.golod.chislo - random.randint(1, 10)
            if event.type == self.sobitieradost:
                self.radost.chislo = self.radost.chislo - random.randint(1, 6)
            if event.type == self.sobitiehp:
                if self.golod.chislo <= 20 or self.radost.chislo <= 20:                
                    self.hp.chislo = self.hp.chislo - random.randint(1,5)                               

    def update(self):
        for button in self.buttons:
            button.logic()
            

    def draw(self):
        self.screen.blit(images.fon, [0, 0])
        self.dog.draw()
        self.money.draw()
        self.golod.draw()
        self.radost.draw()
        self.hp.draw()
        for button in self.buttons:
            button.otrisovka()
        pg.display.flip()


if __name__ == "__main__":
    Game()