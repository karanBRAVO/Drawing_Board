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
        self.pixelWidth = 10
        self.pixelHeight = 10
        self.pixelColor = self.colors.black
        # keys
        self.keys = None

    def __draw(self):
        self.__getPressedKey()
        self.__getMousePosition()
        self.window.fill(self.colors.white)
        self.__drawGrid(self.colors.blue)
        self.__storePixels()
        self.__removePixel()
        self.__drawPixels()
        self.__changePixelColor()
        self.__drawMouse(self.mouseX, self.mouseY, self.pixelColor)

    def start(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.run = False
            self.__draw()
            self.__update()
        self.quit()

    def __removePixel(self):
        if self.keys[pygame.K_LCTRL]:
            pass

    def __changePixelColor(self):
        if self.keys[pygame.K_g]:
            self.pixelColor = self.colors.green
        elif self.keys[pygame.K_r]:
            self.pixelColor = self.colors.red
        elif self.keys[pygame.K_b]:
            self.pixelColor = self.colors.blue
        elif self.keys[pygame.K_y]:
            self.pixelColor = self.colors.yellow
        elif self.keys[pygame.K_a]:
            self.pixelColor = self.colors.aqua
        elif self.keys[pygame.K_p]:
            self.pixelColor = self.colors.pink

    def __getPressedKey(self):
        self.keys = pygame.key.get_pressed()

    def __drawPixels(self):
        for p in self.pixels:
            self.__drawRect(p['x'], p['y'],
                            self.pixelWidth,
                            self.pixelHeight,
                            p['color'], 0, -1)

    def __storePixels(self):
        if pygame.mouse.get_pressed(3)[0]:
            x = self.mouseX
            y = self.mouseY
            if x < 0:
                x = 0
            if x > self.windowWidth-self.pixelHeight:
                x = self.windowWidth - self.pixelHeight
            if y < 0:
                y = 0
            if y > self.windowHeight-self.pixelHeight:
                y = self.windowHeight - self.pixelHeight
            p = {
                'x': x,
                'y': y,
                'color': self.pixelColor
            }
            if p not in self.pixels:
                self.pixels.append(p)

    def __getMousePosition(self):
        self.mouseX, self.mouseY = pygame.mouse.get_pos()

    def __drawMouse(self, x: int, y: int, color):
        self.__drawRect(x, y,
                        self.mouseWidth,
                        self.mouseHeight,
                        color, 0, -1)

    def __drawGrid(self, color):
        for i in range(0, self.windowWidth, self.gridWidth):
            for j in range(0, self.windowHeight, self.gridHeight):
                self.__drawRect(i, j, self.gridWidth,
                                self.gridHeight, color, 1, -1)

    def __drawRect(self, x: int, y: int, w: int, h: int, color, cw: int, br: int):
        pygame.draw.rect(self.window, color, (x, y, w, h),
                         cw, border_radius=br)

    def __update(self):
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
