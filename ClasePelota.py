import pygame

class Pelota():

    def __init__(self):
        self.posx=590
        self.posy=241
        self.superficie=(pygame.Rect(self.posx,self.posy,20,20))

    def pintar(self,ventana):
        self.superficie=(pygame.Rect(self.posx,self.posy,20,20))
        pygame.draw.rect(ventana,"white",self.superficie)

    def set(self,x,y):
        self.posx+=x
        self.posy+=y

    def getX(self):
        return self.posx

    def getY(self):
        return self.posy

    def setX(self,x):
        self.posx=x

    def setY(self,y):
        self.posy=y
