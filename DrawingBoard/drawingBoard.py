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
        # grid
        self.gridWidth = 10
        self.gridHeight = 10
        # mouse
        pygame.mouse.set_visible(False)
        self.mouseWidth = 10
        self.mouseHeight = 10
        self.mouseX = -1
        self.mouseY = -1
        # pixels
        self.pixels = []
        self.pixelWidth = 5
        self.pixelHeight = 5
        self.pixelColor = self.colors.green

    def __draw__(self):
        self.getMousePosition()
        self.window.fill(self.colors.white)
        # self.drawGrid(self.colors.blue)
        self.storePixels()
        self.drawPixels()
        self.changePixelColor()
        self.drawMouse(self.mouseX, self.mouseY, self.colors.black)

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

    def changePixelColor(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_g]:
            self.pixelColor = self.colors.green
        elif keys[pygame.K_r]:
            self.pixelColor = self.colors.red
        elif keys[pygame.K_b]:
            self.pixelColor = self.colors.blue
        elif keys[pygame.K_y]:
            self.pixelColor = self.colors.yellow
        elif keys[pygame.K_a]:
            self.pixelColor = self.colors.aqua
        elif keys[pygame.K_p]:
            self.pixelColor = self.colors.pink

    def drawPixels(self):
        for p in self.pixels:
            self.drawRect(p['x'], p['y'],
                          self.pixelWidth,
                          self.pixelHeight,
                          p['color'], 0, 50)

    def storePixels(self):
        if pygame.mouse.get_pressed(3)[0]:
            p = {
                'x': self.mouseX-self.mouseWidth//2,
                'y': self.mouseY-self.mouseHeight//2,
                'color': self.pixelColor
            }
            if p not in self.pixels:
                self.pixels.append(p)

    def getMousePosition(self):
        self.mouseX, self.mouseY = pygame.mouse.get_pos()

    def drawMouse(self, x: int, y: int, color):
        self.drawRect(x-self.mouseWidth//2,
                      y-self.mouseHeight//2,
                      self.mouseWidth,
                      self.mouseHeight,
                      color, 0, 50)

    def drawGrid(self, color):
        for i in range(0, self.windowWidth, self.gridWidth):
            for j in range(0, self.windowHeight, self.gridHeight):
                self.drawRect(i, j, self.gridWidth,
                              self.gridHeight, color, 1, -1)

    def drawRect(self, x: int, y: int, w: int, h: int, color, cw: int, br: int):
        pygame.draw.rect(self.window, color, (x, y, w, h),
                         cw, border_radius=br)

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
        self.yellow = (255, 255, 0)
        self.pink = (255, 0, 255)
        self.aqua = (0, 255, 255)
