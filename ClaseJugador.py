import pygame

class Jugador():

    def __init__(self,posx,posy):
        self.posx=posx
        self.posy=posy
        self.superficie=pygame.Rect(self.posx,self.posy,15,100)

    def pintar(self,ventana):
        self.superficie=pygame.Rect(self.posx,self.posy,15,100)
        pygame.draw.rect(ventana,"white",self.superficie)

    def moveDown(self):
        if self.posy<470:
            self.posy+=15
            self.superficie=pygame.Rect(self.posx,self.posy,15,100)

    def moveUp(self):
        if self.posy>5:
            self.posy-=15
            self.superficie=pygame.Rect(self.posx,self.posy,15,100)

    def getX(self):
        return self.posx

    def getY(self):
        return self.posy

    def setX(self,x):
        self.posx=x

    def setY(self,y):
        self.posy=y
