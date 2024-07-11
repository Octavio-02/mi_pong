import pygame
import os

class Resultado():

    def __init__(self,x,y):
        self.posx=x
        self.posy=y
        self.puntaje=0
        self.CERO = pygame.image.load(os.path.join("Images","cero.png"))
        self.UNO = pygame.image.load("Images/uno.png")
        self.DOS = pygame.image.load("Images/dos.png")
        self.TRES = pygame.image.load("Images/tres.png")
        self.CUATRO = pygame.image.load("Images/cuatro.png")
        self.CINCO = pygame.image.load("Images/cinco.png")

    def pintar(self,ventana):
        if self.puntaje==0:
            ventana.blit(self.CERO,(self.posx,self.posy))
        elif self.puntaje==1:
            ventana.blit(self.UNO,(self.posx,self.posy))
        elif self.puntaje==2:
            ventana.blit(self.DOS,(self.posx,self.posy))
        elif self.puntaje==3:
            ventana.blit(self.TRES,(self.posx,self.posy))
        elif self.puntaje==4:
            ventana.blit(self.CUATRO,(self.posx,self.posy))
        elif self.puntaje==5:
            ventana.blit(self.CINCO,(self.posx,self.posy))

    def sumar(self):
        self.puntaje+=1

    def getPuntaje(self):
        return self.puntaje
