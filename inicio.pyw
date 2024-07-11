import pygame, sys
import juego

def iniciar():

    #Creación de ventana
    VENTANA=pygame.display.set_mode(size=(1200,900))

    ########################################### Creación de Menú de juego ##################################################
    #Título
    TITULO=pygame.Rect(400,200,350,100)
    pygame.draw.rect(VENTANA,"white",TITULO)
    titulo=pygame.image.load("Images\Tetris.png")
    VENTANA.blit(titulo, (400,200))


    #Botón Jugar
    FONDO_JUGAR=pygame.Rect(405,495,150,50)
    pygame.draw.rect(VENTANA,"grey",FONDO_JUGAR,border_radius=7)
    BOTON_JUGAR=pygame.Rect(400,500,150,50)
    pygame.draw.rect(VENTANA,"white",BOTON_JUGAR,border_radius=7)
    jugar=pygame.image.load("Images\jugar.png")
    VENTANA.blit(jugar,(400,500))

    #Botón Salir
    FONDO_EXIT=pygame.Rect(605,495,150,50)
    pygame.draw.rect(VENTANA,"grey",FONDO_EXIT,border_radius=7)
    BOTON_EXIT=pygame.Rect(600,500,150,50)
    pygame.draw.rect(VENTANA,"white",BOTON_EXIT,border_radius=7)
    salir=pygame.image.load("Images\salir.png")
    VENTANA.blit(salir, (600,500))

    ########################################### Main Loop ####################################################################

    while 1:
        #Obtener posición del mouse
        MOUSEPOSITION=pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_RETURN:
                    juego.juegos()
            if MOUSEPOSITION[0]>400 and MOUSEPOSITION[0]<555 and MOUSEPOSITION[1]>495 and MOUSEPOSITION[1]<550:
                pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    juego.juegos()
            elif MOUSEPOSITION[0]>600 and MOUSEPOSITION[0]<755 and MOUSEPOSITION[1]>495 and MOUSEPOSITION[1]<550:
                pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    sys.exit()
            else:
                pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))


        pygame.display.flip()

if __name__ == "__main__":
    iniciar()
