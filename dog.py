import images

import pygame

class Dog:
    def __init__(self, game):
        self.kartinka = images.dog
        self.hitbox = pygame.Rect([290, 200], self.kartinka.get_size())
        self.game = game
    def draw(self):
        self.game.screen.blit(self.kartinka, self.hitbox)
