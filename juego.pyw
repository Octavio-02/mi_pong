import pygame, sys
import ClaseResultado
import ClaseJugador
import ClasePelota
import inicio

########################################################### Inicialización de pygame ##########################################################################
pygame.init()

########################################################### Dibuja línea Divisoria ############################################################################
def dibujaLinea(ventana):
    for i in range(0,30,2):
        pygame.draw.line(ventana,"white",(600,0+(i*20)),(600,20+(i*20)), 2)

########################################################### Pantalla Ganador ##################################################################################
def final(ventana,jugador):
    ventana.fill("black")
    superficie=pygame.Rect(330,200,450,100)
    pygame.draw.rect(ventana,"white",superficie)
    if jugador==1:
        imagen=pygame.image.load("Images/Jugador 1 gana.png")
    if jugador==2:
        imagen=pygame.image.load("Images/Jugador 2 gana.png")
    ventana.blit(imagen,(350,150))
    pygame.display.flip()

########################################################### Main del Juego ####################################################################################
def juegos():
    #Variables Globales
    inc_x=-2
    inc_y=2
    flag=0

    #Creamos la ventana
    pygame.display.init()
    ventana=pygame.display.set_mode(size=(1200,582))
    pygame.display.set_caption("Herramientas")

    #Crear Jugador 1
    jugador_uno=ClaseJugador.Jugador(10,50)
    jugador_uno.pintar(ventana)

    #Crear Jugador 2
    jugador_dos=ClaseJugador.Jugador(1175,50)
    jugador_dos.pintar(ventana)

    #Crear Pelota
    pelota=ClasePelota.Pelota()
    pelota.pintar(ventana)

    #Creamos el resultado
    resultado_uno=ClaseResultado.Resultado(500,0)
    resultado_dos=ClaseResultado.Resultado(650,0)

    #Determino los parámetros de repetición de teclas
    pygame.key.set_repeat(10,100)

    #Establezco el reloj del juego
    reloj=pygame.time.Clock()

    while 1:
        pygame.time.wait(5)                     #Realentizar el tiempo
        for event in pygame.event.get():        #Buscar Eventos
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    jugador_uno.moveDown()
                elif event.key == pygame.K_w:
                    jugador_uno.moveUp()
                elif event.key == pygame.K_DOWN:
                    jugador_dos.moveDown()
                elif event.key == pygame.K_UP:
                    jugador_dos.moveUp()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        #Detección de gol
        if pelota.getX() <= 0:
            flag=1
            resultado_dos.sumar()
            if resultado_dos.getPuntaje()==5:
                final(ventana,2)
                pygame.time.wait(1000)
                inicio.iniciar()
        elif pelota.getX() >= 1200:
            flag=1
            resultado_uno.sumar()
            if resultado_uno.getPuntaje()==5:
                final(ventana,1)
                pygame.time.wait(1000)
                inicio.iniciar()

        #Detección de colisiones vertivales
        if pelota.getY()<=0:
            inc_y=+2
        if pelota.getY()>=565:
            inc_y=-2
        #Detección de colisiones con jugadores
        if pelota.getX()<=jugador_uno.getX()+15 and ( (pelota.getY()>jugador_uno.getY() and pelota.getY()<jugador_uno.getY()+100) or (pelota.getY()+20<jugador_uno.getY()+100 and pelota.getY()+20>jugador_uno.getY()) ):
            inc_x=+2
            if pelota.getY()>(jugador_uno.getY()+50):
                inc_y=2
            else:
                inc_y=-2
        if pelota.getX()+20>=jugador_dos.getX() and ( (pelota.getY()>jugador_dos.getY() and pelota.getY()<jugador_dos.getY()+100) or (pelota.getY()+20<jugador_dos.getY()+100 and pelota.getY()+20>jugador_dos.getY()) ):
            inc_x-=2
            if pelota.getY()>(jugador_dos.getY()+50):
                inc_y=2
            else:
                inc_y=-2

        #Actualización de posición de la pelota
        pelota.set(inc_x,inc_y)

        #Actualización extra en caso de gol
        if flag==1:
            pelota.setX(590)
            pelota.setY(241)
            jugador_uno.setX(10)
            jugador_uno.setY(50)
            jugador_dos.setX(1175)
            jugador_dos.setY(50)
            flag=0

        #Actualización de Ventana
        ventana.fill("black")
        dibujaLinea(ventana)
        pelota.pintar(ventana)
        jugador_uno.pintar(ventana)
        jugador_dos.pintar(ventana)
        resultado_uno.pintar(ventana)
        resultado_dos.pintar(ventana)
        pygame.display.flip()
        reloj.tick(10000)
