import pygame
from pygame.locals import *
import sys


class DrawingBoard():
    def __init__(self, windowWidth: int, windowHeight: int) -> None:
        # Initialize pygame
        pygame.init()
        #  Colors
        self.colors = Color()
        # Window dimensions
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        # Clock and Frame/second
        self.clock = pygame.time.Clock()
        self.fps = 60
        # Window instance
        self.window = pygame.display.set_mode(
            (self.windowWidth, self.windowHeight))
        # state
        self.run = True

    def __draw__(self):
        self.window.fill(self.colors.white)

    def start(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.run = False
            self.__draw__()
            self.update()

    def update(self):
        pygame.display.update()
        self.clock.tick(self.fps)

    def quit(self):
        pygame.quit()
        sys.exit(0)


class Color():
    def __init__(self):
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
