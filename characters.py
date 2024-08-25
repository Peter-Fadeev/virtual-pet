import pygame
import images
import pygame.freetype

class Characters:
    def __init__(self, game, kartinka, x, y, chislo):
        self.kartinka = kartinka
        self.chislo = chislo
        self.hitbox = pygame.Rect([x, y], self.kartinka.get_size())
        self.game = game
        self.shrift = pygame.freetype.Font("shrift.ttf", 48)
    def draw(self):
        self.shrift.render_to(self.game.screen, [self.hitbox.x + 100, self.hitbox.y+30], str(self.chislo))
        self.game.screen.blit(self.kartinka, self.hitbox)
        
 