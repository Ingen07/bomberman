import pygame
import sys
import time
import random
#mediadas de la pantalla
ancho = 900
alto = 700
pygame.mixer.init()
pygame.mixer.music.load('mapas/Rammstein Te Quiero Puta.mp3')
pygame.mixer.music.play(-1)

def menu():
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    AZUL = (0, 0, 255)


    # Funciones de los botones de la pantalla inicial
    def pantalla_personajes():
        def create_button(text, font, color, hover_color, surface, x, y, width, height, action=None):
            mouse_pos = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if x < mouse_pos[0] < x + width and y < mouse_pos[1] < y + height:
                pygame.draw.rect(surface, hover_color, (x, y, width, height))
                if click[0] == 1 and action is not None:
                    action()
            else:
                pygame.draw.rect(surface, color, (x, y, width, height))

            draw_text(text, font, (0, 0, 0), surface, x + width // 2, y + height // 2)

        def draw_text(text, font, color, surface, x, y):
            text_obj = font.render(text, True, color)
            text_rect = text_obj.get_rect()
            text_rect.center = (x, y)
            surface.blit(text_obj, text_rect)

        def open_game_1():
            # Inicializar
            pygame.init()
            tiempo_inicial = time.time()
            puntos = 0
            llaves = 0
            fuente = pygame.font.SysFont(None, 30)
            # Medidas
            ANCHO = 900
            ALTO = 700

            # Tamaño del mapa
            TAMANO_MAPA_X = 13
            TAMANO_MAPA_Y = 9

            # Tamaño del mapa y tamaño de los muros
            ANCHO_MAPA = 600
            ALTO_MAPA = 450

            # Definir dimensiones de la ventana emergente
            VENTANA_EMERGENTE_ANCHO = 400
            VENTANA_EMERGENTE_ALTO = 200

            # Colores
            BLANCO = (255, 255, 255)
            NEGRO = (0, 0, 0)
            ROJO = (255, 0, 0)

            # Tamaño del mapa
            TAMANO_MAPA_X = 13
            TAMANO_MAPA_Y = 9

            # Tamaño del mapa y tamaño de los muros
            ANCHO_MAPA = 600
            ALTO_MAPA = 450
            ANCHO_MURO = ANCHO_MAPA // TAMANO_MAPA_X
            ALTO_MURO = ALTO_MAPA // TAMANO_MAPA_Y



            # Mapa1
            mapa = [
                
                "xxxxxxxxxxxxx",
                "x           x",
                "x x x x x x x",
                "x           x",
                "x x x x x x x",
                "x           x",
                "xxx x x x x x",
                "x          xx",
                "xxxxxxxxxxxxx",
                "             "
            ]
            # Mapa2

            mapa2 = [
                
                "xxxxxxxxxxxxx",
                "xx          x",
                "x x x x x x x",
                "x    x      x",
                "x x x   x x x",
                "x   x       x",
                "xx   x x  x x",
                "x   x   x  xx",
                "xxxxxxxxxxxxx",
                "             "
            ]
            # Mapa1
            mapa3 = [
                
                "xxxxxxxxxxxxx",
                "xx          x",
                "x x x x   x x",
                "x    x      x",
                "x x x   x x x",
                "x   x       x",
                "x x    x  x x",
                "xx  x   x  xx",
                "xxxxxxxxxxxxx",
                "             "
            ]



            # Función para formatear el tiempo en minutos y segundos
            def formatear_tiempo(tiempo):
                minutos = int(tiempo // 60)
                segundos = int(tiempo % 60)
                return f"{minutos:02}:{segundos:02}"
            # Función para dibujar la barra de información con el tiempo formateado
            def dibujar_barra_informacion(superficie, vidas, puntos, llaves, tiempo, x_vida_inicial=20, y_vida=ALTO - 40, espacio_entre_elementos=40):
                # Caso base: si no quedan vidas, terminar la recursión
                if vidas <= 0:
                    # Dibujar el fondo de la barra de información al final de la recursión
                    pygame.draw.rect(superficie, BLANCO, (0, ALTO - 50, ANCHO, 50))
                    # Dibujar el contador de puntos
                    fuente = pygame.font.SysFont(None, 30)
                    texto_puntos = fuente.render("Puntos: " + str(puntos), True, NEGRO)
                    superficie.blit(texto_puntos, (ANCHO - 150, ALTO - 40))
                    # Dibujar el contador de llaves
                    texto_llaves = fuente.render("Llaves: " + str(llaves), True, NEGRO)
                    superficie.blit(texto_llaves, (ANCHO - 280, ALTO - 40))
                    # Dibujar el cronómetro formateado
                    texto_tiempo = fuente.render("Tiempo: " + formatear_tiempo(tiempo), True, NEGRO)
                    superficie.blit(texto_tiempo, (450, ALTO - 40))
                    return
                else:
                    # Dibujar la barra blanca antes de dibujar los corazones y llaves
                    pygame.draw.rect(superficie, BLANCO, (0, ALTO - 50, ANCHO, 50))
                    # Llamar recursivamente para dibujar las vidas restantes
                    dibujar_barra_informacion(superficie, vidas - 1, puntos, llaves, tiempo, x_vida_inicial + espacio_entre_elementos + imagen_vida.get_width(), y_vida, espacio_entre_elementos)
                    # Dibujar una vida después de dibujar las vidas restantes
                    superficie.blit(imagen_vida, (x_vida_inicial, y_vida))



                # Escribir texto en la barra de información
                fuente = pygame.font.SysFont(None, 24)
                texto = ""
                texto_renderizado = fuente.render(texto, True, NEGRO)
                superficie.blit(texto_renderizado, (20, ALTO - 40))


            # Función para construir el mapa recursivamente
            def construir_mapa(mapa, ancho_muro, alto_muro, x=0, y=0):
                # Obtener las dimensiones del mapa
                TAMANO_MAPA_Y = len(mapa)

                # Caso base: si hemos alcanzado el final del mapa, retornar una lista vacía de muros y colisiones
                if y >= TAMANO_MAPA_Y:
                    return [], []

                # Caso recursivo: explorar la siguiente fila del mapa
                muros_fila, colisiones_fila = construir_mapa(mapa, ancho_muro, alto_muro, 0, y + 1)

                # Lista para almacenar los muros y colisiones de esta fila
                muros = []
                colisiones = []

                # Iterar sobre cada columna en la fila actual
                for x_actual, caracter in enumerate(mapa[y]):
                    # Calcular las coordenadas x e y del muro actual
                    x_actual *= ancho_muro
                    x_actual += x
                    y_actual = y * alto_muro

                    if caracter == "x":
                        # Crear un rectángulo para representar el muro
                        rect_muro = pygame.Rect(x_actual, y_actual, ancho_muro, alto_muro)
                        muros.append(rect_muro)
                        # Crear un rectángulo de colisión para el muro (ligeramente más pequeño para evitar superposiciones)
                        rect_colision = pygame.Rect(x_actual + 2, y_actual + 2, ancho_muro - 4, alto_muro - 4)
                        colisiones.append(rect_colision)

                # Combinar los muros y colisiones de esta fila con los de las filas anteriores
                muros.extend(muros_fila)
                colisiones.extend(colisiones_fila)

                return muros, colisiones

            def dibujar_muros(superficie, muros):
                if not muros:  # Caso base: si la lista de muros está vacía, detener la recursión
                    return
                
                # Obtener el primer muro de la lista
                primer_muro = muros[0]
                
                # Dibujar la imagen de muro en la superficie
                superficie.blit(imagen_muro, (primer_muro.x, primer_muro.y))
                
                # Llamar recursivamente a la función con el resto de la lista de muros
                dibujar_muros(superficie, muros[1:])






            def explosion(posicion, rango, muros, cajas, personaje, corazones):
                alcance = [(0, 0)]  # La propia posición de la bomba
                
                muros_a_eliminar = []
                cajas_a_eliminar = []
                jugador_alcanzado = False  # Bandera para verificar si el jugador fue alcanzado por la explosión
                
                # Verificar si la explosión alcanza al personaje
                for x, y in alcance:
                    if personaje.colliderect(pygame.Rect(x * ANCHO_MURO, y * ALTO_MURO, ANCHO_MURO, ALTO_MURO)):
                        jugador_alcanzado = True  # El jugador fue alcanzado por la explosión
                        break
                
                for direccion in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    for i in range(1, rango + 1):
                        nueva_posicion = (posicion[0] + direccion[0] * i, posicion[1] + direccion[1] * i)
                        alcance.append(nueva_posicion)
                        # Romper la explosión si se encuentra un muro
                        for muro in muros:
                            if muro.collidepoint(nueva_posicion):
                                muros_a_eliminar.append(muro)
                                break
                        else:
                            # Romper la explosión si se encuentra una caja
                            for caja in cajas:
                                if caja.collidepoint(nueva_posicion):
                                    cajas_a_eliminar.append(caja)
                                    break
                            continue
                        break
                # Eliminar los muros alcanzados por la explosión
                for muro in muros_a_eliminar:
                    muros.remove(muro)
                # Eliminar las cajas alcanzadas por la explosión
                for caja in cajas_a_eliminar:
                    cajas.remove(caja)
                return alcance, jugador_alcanzado


            #al detectar una colicion no deja que el npc se mueva 
            #cuando lo hay colicion lo deja avanzar a la siguiente posicion 
            def move_colisiones(personaje, dx, dy, colisiones, cajas, indice=0):
                if indice == len(colisiones):
                    # Si no hay más objetos para verificar colisión, devolver la nueva posición
                    return personaje.move(dx, dy)
                
                obj = colisiones[indice]
                nueva_posicion = personaje.move(dx, dy)
                
                # Verificar colisión con las cajas
                for caja in cajas:
                    if nueva_posicion.colliderect(caja):
                        # Si hay colisión con una caja, no mover al personaje
                        return personaje
                
                if nueva_posicion.colliderect(obj):
                    # Si hay colisión con un objeto, no mover al personaje
                    return personaje
                
                # Llamar recursivamente para verificar la siguiente colisión
                return move_colisiones(personaje, dx, dy, colisiones, cajas, indice + 1)

            # Función para mover recursivamente al enemigo
            def mover_enemigo(x, y, destino_x, destino_y, cajas):
                # Caso base: si el enemigo ha alcanzado las coordenadas de destino, retornar las coordenadas actuales
                if x == destino_x and y == destino_y:
                    return x, y

                # Calcular la dirección del movimiento en x e y
                if destino_x > x:
                    nueva_x = min(x + velocidad_x, destino_x)
                elif destino_x < x:
                    nueva_x = max(x - velocidad_x, destino_x)
                else:
                    nueva_x = x

                if destino_y > y:
                    nueva_y = min(y + velocidad_y, destino_y)
                elif destino_y < y:
                    nueva_y = max(y - velocidad_y, destino_y)
                else:
                    nueva_y = y

                # Verificar si hay colisión con las cajas
                for caja in cajas:
                    if pygame.Rect(nueva_x, nueva_y, e_ancho, e_alto).colliderect(caja):
                        # Si hay colisión con una caja, no mover al enemigo
                        return x, y
                
                # Llamar recursivamente a la función mover_enemigo() con las nuevas coordenadas
                return mover_enemigo(nueva_x, nueva_y, destino_x, destino_y, cajas)

            def verificar_colision_jugador_enemigo(jugador_rect, enemigo_x, enemigo_y):
                return jugador_rect.colliderect(pygame.Rect(enemigo_x, enemigo_y, e_ancho, e_alto))




            def dibujar_estrellas(superficie, estrellas_posiciones):
                for pos_estrella_x, pos_estrella_y in estrellas_posiciones:
                    superficie.blit(imagen_estrella, (pos_estrella_x, pos_estrella_y))
                    superficie.blit(imagen_estrella2, (pos_estrella_x, pos_estrella_y))  # Dibujar la segunda estrella en la misma posición
            # Función recursiva para detectar colisiones con las estrellas en diferentes posiciones
            def detectar_colisiones_estrella(personaje_rect, estrellas_posiciones, puntos):
                # Variable para verificar si se detectó una colisión con una estrella
                colision_estrella = False
                
                # Función interna para detectar colisiones
                def detectar_colisiones_recursiva(estrellas_posiciones, puntos, colision_estrella):
                    if not estrellas_posiciones:
                        # Si no quedan estrellas, devolver los puntos actualizados y la lista de posiciones de estrellas
                        return puntos, [], colision_estrella
                    
                    # Extraer la posición de la primera estrella en la lista
                    pos_estrella_x, pos_estrella_y = estrellas_posiciones[0]
                    
                    # Verificar colisión entre el personaje y la estrella
                    if personaje_rect.colliderect(pygame.Rect(pos_estrella_x, pos_estrella_y, ANCHO_MURO, ALTO_MURO)):
                        # Aumentar 100 puntos si hay colisión
                        puntos += 100
                        # Eliminar la posición de la estrella de la lista
                        estrellas_posiciones.pop(0)
                        colision_estrella = True
                        
                        # Hacer la estrella transparente
                        hacer_estrella_transparente()
                        
                        # Llamar recursivamente a la función con la lista actualizada de estrellas
                        return detectar_colisiones_recursiva(estrellas_posiciones, puntos, colision_estrella)
                    
                    else:
                        # Si no hay colisión, llamar recursivamente a la función con la lista restante de estrellas
                        puntos, estrellas_posiciones, colision_estrella = detectar_colisiones_recursiva(estrellas_posiciones[1:], puntos, colision_estrella)
                        return puntos, [(pos_estrella_x, pos_estrella_y)] + estrellas_posiciones, colision_estrella
                
                # Llamar a la función interna para iniciar la detección de colisiones
                return detectar_colisiones_recursiva(estrellas_posiciones, puntos, colision_estrella)
            # Después de obtener los puntos necesarios
            def hacer_estrella_transparente():
                # Cargar la imagen de la estrella con transparencia alfa
                imagen_estrella_transparente = pygame.image.load("mapas/estre.jpg").convert_alpha()
                
                # Ajustar el valor alfa de los píxeles de la imagen para hacerla más transparente
                # Por ejemplo, reducir el valor alfa a la mitad (0 sería completamente transparente, 255 sería opaco)
                factor_transparencia = 2  # Por ejemplo, reducir a la mitad la transparencia original
                imagen_estrella_transparente.set_alpha(factor_transparencia)
                
                # Devolver la imagen de la estrella transparente
                return imagen_estrella_transparente





            def dibujar_llaves(superficie, llaves_posiciones):
                for pos_llave_x, pos_llave_y in llaves_posiciones:
                    superficie.blit(imagen_llave, (pos_llave_x, pos_llave_y))
                    superficie.blit(imagen_llave2, (pos_llave_x, pos_llave_y))
                    superficie.blit(imagen_llave3, (pos_llave_x, pos_llave_y))        
            # Función recursiva para detectar colisiones con las llaves en diferentes posiciones
            def detectar_colisiones_llave(personaje_rect, llaves_posiciones, puntos):
                # Variable para verificar si se detectó una colisión con una llave
                colision_llave = False
                
                # Función interna para detectar colisiones
                def detectar_colisiones_recursiva(llaves_posiciones, puntos, colision_llave):
                    if not llaves_posiciones:
                        # Si no quedan llaves, devolver los puntos actualizados y la lista de posiciones de llaves
                        return puntos, [], colision_llave
                    
                    # Extraer la posición de la primera llave en la lista
                    pos_llave_x, pos_llave_y = llaves_posiciones[0]
                    
                    # Verificar colisión entre el personaje y la llave
                    if personaje_rect.colliderect(pygame.Rect(pos_llave_x, pos_llave_y, ANCHO_MURO, ALTO_MURO)):
                        # Aumentar 100 puntos si hay colisión
                        puntos += 250
                        # Eliminar la posición de la llave de la lista
                        llaves_posiciones.pop(0)
                        colision_llave = True
                        
                        # Hacer la llave transparente
                        hacer_llave_transparente()
                        
                        # Llamar recursivamente a la función con la lista actualizada de llaves
                        return detectar_colisiones_recursiva(llaves_posiciones, puntos, colision_llave)
                    
                    else:
                        # Si no hay colisión, llamar recursivamente a la función con la lista restante de llaves
                        puntos, llaves_posiciones, colision_llave = detectar_colisiones_recursiva(llaves_posiciones[1:], puntos, colision_llave)
                        return puntos, [(pos_llave_x, pos_llave_y)] + llaves_posiciones, colision_llave
                
                # Llamar a la función interna para iniciar la detección de colisiones
                return detectar_colisiones_recursiva(llaves_posiciones, puntos, colision_llave)
            # Después de obtener los puntos necesarios
            def hacer_llave_transparente():
                # Cargar la imagen de la llave con transparencia alfa
                imagen_llave_transparente = pygame.image.load("mapas/llave.jpg").convert_alpha()
                
                # Ajustar el valor alfa de los píxeles de la imagen para hacerla más transparente
                # Por ejemplo, reducir el valor alfa a la mitad (0 sería completamente transparente, 255 sería opaco)
                factor_transparencia = 2  # Por ejemplo, reducir a la mitad la transparencia original
                imagen_llave_transparente.set_alpha(factor_transparencia)
                
                # Devolver la imagen de la llave transparente
                return imagen_llave_transparente




            def colocar_bomba(bombas, personaje_x, personaje_y, bombas_colocadas, MAX_BOMBAS):
                # Función auxiliar para verificar si una bomba está en una posición
                def bomba_en_posicion(x, y):
                    for bomba, _ in bombas:
                        if bomba.colliderect(pygame.Rect(x, y, 20, 20)):
                            return True
                    return False

                # Verificar si hay espacio para colocar la bomba
                if bombas_colocadas >= MAX_BOMBAS:
                    return bombas, bombas_colocadas

                # Verificar si la posición para colocar la bomba está ocupada por otra bomba
                if bomba_en_posicion(personaje_x, personaje_y):
                    return bombas, bombas_colocadas

                # Si la posición no está ocupada, colocar la bomba
                bomba = pygame.Rect(personaje_x, personaje_y, 20, 20)
                bombas.append((bomba, time.time()))
                bombas_colocadas += 1

                return bombas, bombas_colocadas


            def verificar_explosion(bombas, personaje_rect, corazones):
                for bomba, _ in bombas:
                    # Verificar si la explosión alcanza al personaje
                    if bomba.colliderect(personaje_rect):
                        if len(corazones) > 0:
                            # Si hay corazones disponibles, eliminar uno
                            corazones.pop()
                        return True  # Indicar que hubo una explosión que alcanzó al personaje
                # Llamar recursivamente a la función con las bombas restantes y el mismo personaje
                if bombas:
                    return verificar_explosion(bombas[:-1], personaje_rect, corazones)
                return False  # Indicar que no hubo explosión que alcanzó al personaje



            def dibujar_puertas_subterraneas(superficie, puertas_posiciones):
                for pos_puerta_x, pos_puerta_y in puertas_posiciones:
                    superficie.blit(imagen_puerta_subterranea, (pos_puerta_x, pos_puerta_y))
            # Función recursiva para detectar colisiones con las puertas subterráneas en diferentes posiciones
            def detectar_colisiones_puerta_subterranea(personaje_rect, puertas_posiciones, puntos):
                # Variable para verificar si se detectó una colisión con una puerta subterránea
                colision_puerta_subterranea = False
                
                # Función interna para detectar colisiones
                def detectar_colisiones_recursiva(puertas_posiciones, puntos, colision_puerta_subterranea):
                    if not puertas_posiciones:
                        # Si no quedan puertas subterráneas, devolver los puntos actualizados y la lista de posiciones de puertas subterráneas
                        return puntos, [], colision_puerta_subterranea
                    
                    # Extraer la posición de la primera puerta subterránea en la lista
                    pos_puerta_x, pos_puerta_y = puertas_posiciones[0]
                    
                    # Verificar colisión entre el personaje y la puerta subterránea
                    if personaje_rect.colliderect(pygame.Rect(pos_puerta_x, pos_puerta_y, 55, 55)):
                        # Aumentar puntos si hay colisión
                        puntos += 500
                        # Eliminar la posición de la puerta subterránea de la lista
                        puertas_posiciones.pop(0)
                        colision_puerta_subterranea = True
                        
                        # Abrir la puerta subterránea
                        abrir_puerta_subterranea()
                        
                        # Llamar recursivamente a la función con la lista actualizada de puertas subterráneas
                        return detectar_colisiones_recursiva(puertas_posiciones, puntos, colision_puerta_subterranea)
                    
                    else:
                        # Si no hay colisión, llamar recursivamente a la función con la lista restante de puertas subterráneas
                        puntos, puertas_posiciones, colision_puerta_subterranea = detectar_colisiones_recursiva(puertas_posiciones[1:], puntos, colision_puerta_subterranea)
                        return puntos, [(pos_puerta_x, pos_puerta_y)] + puertas_posiciones, colision_puerta_subterranea
                
                # Llamar a la función interna para iniciar la detección de colisiones
                return detectar_colisiones_recursiva(puertas_posiciones, puntos, colision_puerta_subterranea)
            # Después de obtener los puntos necesarios
            def abrir_puerta_subterranea():
                # Cargar la imagen de la puerta subterránea abierta
                imagen_puerta_subterranea_abierta = pygame.image.load("mapas/puerta_subterranea.png").convert_alpha()
                
                # Ajustar el valor alfa de los píxeles de la imagen para hacerla visible
                # Por ejemplo, establecer el valor alfa a 255 para que sea completamente opaca
                factor_visibilidad = 5  # Por ejemplo, establecer la visibilidad al máximo
                imagen_puerta_subterranea_abierta.set_alpha(factor_visibilidad)
                
                # Devolver la imagen de la puerta subterránea abierta
                return imagen_puerta_subterranea_abierta






            # Ventana
            ventana = pygame.display.set_mode((ANCHO, ALTO))
            pygame.display.set_caption("BOMBERMAN")

            # Cargar imagen de la vida
            imagen_vida = pygame.image.load("mapas/cora.jpg").convert_alpha()
            imagen_vida = pygame.transform.scale(imagen_vida, (30, 30))
            # Cargar imagen de la llave
            imagen_llave = pygame.image.load("mapas/llave.jpg").convert_alpha()
            imagen_llave = pygame.transform.scale(imagen_llave, (30, 30))
            imagen_llave2 = pygame.image.load("mapas/llave.jpg").convert_alpha()
            imagen_llave2 = pygame.transform.scale(imagen_llave2, (30, 30))
            imagen_llave3 = pygame.image.load("mapas/llave.jpg").convert_alpha()
            imagen_llave3 = pygame.transform.scale(imagen_llave3, (30, 30))
            # Cargar imagen de la estrella
            imagen_estrella = pygame.image.load("mapas/estre.jpg").convert_alpha()
            imagen_estrella = pygame.transform.scale(imagen_estrella, (ANCHO_MURO, ALTO_MURO))
            imagen_estrella2 = pygame.image.load("mapas/estre.jpg").convert_alpha()
            imagen_estrella2 = pygame.transform.scale(imagen_estrella2, (ANCHO_MURO, ALTO_MURO))

            # Datos de los muros 
            ancho_muro = ANCHO // len(mapa[0])
            alto_muro = ALTO // len(mapa)
            muros, colisiones = construir_mapa(mapa, ancho_muro, alto_muro)

            # Cargar imagen del muro
            imagen_muro = pygame.image.load("mapas/block.png").convert_alpha()
            imagen_muro = pygame.transform.scale(imagen_muro, (ancho_muro, alto_muro))

            # Cargar imagen de la bomba
            imagen_bomba = pygame.image.load("mapas/boom.jpg").convert_alpha()
            imagen_bomba = pygame.transform.scale(imagen_bomba, (35, 35))

            # Cargar imagen de la puerta subterranea
            puerta_subterranea = pygame.image.load("mapas/puerta_subterranea.png")
            imagen_puerta_subterranea = pygame.transform.scale(puerta_subterranea, (55, 55))  # para escalar la imagen 
            puerta_subterranea2 = pygame.image.load("mapas/puerta_subterranea.png")
            imagen_puerta_subterranea2 = pygame.transform.scale(puerta_subterranea2, (55, 55))  # para escalar la imagen 
            imagen_puerta_subterranea3 = pygame.image.load("mapas/puerta_subterranea.png")
            imagen_puerta_subterranea3 = pygame.transform.scale(imagen_puerta_subterranea3, (55, 55))  # para escalar la imagen 

            # Coordenadas donde se colocará la imagen
            x_puerta_subterranea = 765
            y_puerta_subterranea = 85
            x_puerta_subterranea2 = 284
            y_puerta_subterranea2 = 430

            # Cargar imagen de la caja
            caja = pygame.image.load("mapas/caja.jpg")
            imagen_caja = pygame.transform.scale(caja, (55, 55))  # para escalar la imagen 
            # Coordenadas donde se colocará la imagen
            x_caja = 690
            y_caja = 85



            # Cargar imagen de fondo
            imagen_fondo = pygame.image.load("mapas/fondo_mapa.jpg").convert()  
            imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO, ALTO))

            # Cargar imágenes del personaje para cada dirección
            personaje_arriba = pygame.image.load("proyecto/personaje1/arriba.png").convert_alpha()
            personaje_abajo = pygame.image.load("proyecto/personaje1/abajo.png").convert_alpha()
            personaje_izquierda = pygame.image.load("proyecto/personaje1/izquierda.png").convert_alpha()
            personaje_derecha = pygame.image.load("proyecto/personaje1/derecha.png").convert_alpha()

            # Definir la velocidad de movimiento del personaje
            PLAYER_SPEED = 2.6

            # Crear un diccionario para asociar la dirección con la imagen correspondiente
            direccion_imagen = {
                "izquierda": personaje_izquierda,
                "derecha": personaje_derecha,
                "arriba": personaje_arriba,
                "abajo": personaje_abajo
            }

            # Personaje
            personaje = pygame.Rect(80, 520, 40, 40)
            direccion_personaje = "derecha"

            #----LISTAS----
            #bombas
            bombas = []
            #Explosiones
            explosiones = []
            # Definir la cantidad máxima de bombas que el jugador puede colocar
            MAX_BOMBAS = 6
            # Contador para rastrear cuántas bombas ha colocado el jugador
            bombas_colocadas = 0
            #vidas del jugador 
            vidas = 4 
            corazones = [1, 2, 3]  # Ejemplo de inicialización de la lista de corazones


            # Coordenadas donde se colocarán las cajas
            cajas_posiciones = [
                (80, 145),  # Ejemplo de posición para la primera caja
                (213, 360),  # Ejemplo de posición para la segunda caja
                (353, 220),
                (695, 500),
                (630, 85),
            ]

            # Lista para almacenar los rectángulos de las cajas
            cajas_rect = []

            # Crear rectángulos para cada posición de caja y agregarlos a la lista
            for posicion in cajas_posiciones:
                caja_rect = pygame.Rect(posicion[0], posicion[1], 55, 55)  # Rectángulo con las mismas dimensiones que las cajas
                cajas_rect.append(caja_rect)

            # Lista de posiciones de estrellas en el mapa
            estrellas_posiciones = [
                (80, 80),
                (769,500)
            ]
            llave_posicion = [
                (170, 372),
                (432, 297),
                (570, 160),

            ]
            puertas_posiciones = [(765, 85), (284, 430), (75, 430)]



            #-----------------enemigo--------------------------
            e_alto=35
            e_ancho=30
            i_enemigo1 = pygame.image.load("mapas/Goblin1.jpg").convert()  
            i_enemigo1 = pygame.transform.scale(i_enemigo1, (e_ancho, e_alto))
            # Posición inicial del enemigo
            enemigo_x, enemigo_y = 775, 200
            # Posición a la que queremos mover al enemigo
            destino_x, destino_y = 775, 400
            # Velocidad del enemigo
            velocidad_x = 1
            velocidad_y = 1
            # Puntos de destino del enemigo 
            punto_destino1 = (775, 400)
            punto_destino2 = (775, 200)
            # Variable para rastrear el punto actual hacia el que se mueve el enemigo
            punto_destino_actual = punto_destino1


            #-----------------enemigo2--------------------------
            e_alto = 35
            e_ancho = 30
            i_enemigo2 = pygame.image.load("mapas/Goblin1.jpg").convert()  
            i_enemigo2 = pygame.transform.scale(i_enemigo2, (e_ancho, e_alto))
            # Posición inicial del enemigo2
            enemigo2_x, enemigo2_y = 150, 90
            # Posición a la que queremos mover al enemigo2
            destino2_x, destino2_y = 570, 90
            # Velocidad del enemigo2
            velocidad2_x = 1
            velocidad2_y = 1
            # Puntos de destino del enemigo2 
            punto_destino2_1 = (570, 90)
            punto_destino2_2 = (150, 90)
            # Variable para rastrear el punto actual hacia el que se mueve el enemigo2
            punto_destino_actual2 = punto_destino2_1



            # Bucle principal
            jugando = True
            while jugando:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        jugando = False
                    # Obtener las teclas presionadas
                keys = pygame.key.get_pressed()
                dx, dy = 0, 0
                

                if keys[pygame.K_a]:
                    dx = -PLAYER_SPEED
                    direccion_personaje = "izquierda"
                if keys[pygame.K_d]:
                    dx = PLAYER_SPEED
                    direccion_personaje = "derecha"
                if keys[pygame.K_w]:
                    dy = -PLAYER_SPEED
                    direccion_personaje = "arriba"
                if keys[pygame.K_s]:
                    dy = PLAYER_SPEED
                    direccion_personaje = "abajo"
                # Colocar una bomba si se presiona la tecla de espacio y el jugador tiene bombas disponibles
                if keys[pygame.K_SPACE] and len(bombas) < MAX_BOMBAS:
                    # Llamar a la función recursiva para verificar y colocar la bomba
                    bombas, bombas_colocadas = colocar_bomba(bombas, personaje.x, personaje.y, bombas_colocadas, MAX_BOMBAS)

                # Llamar a la función para restablecer los elementos
                #restablecer_elementos()

                for bomba, tiempo in bombas:
                    if time.time() - tiempo > 2:  # Tiempo de detonación de la bomba (2 segundos)
                        # Llamada a la función de explosión
                        alcance_explosion, jugador_alcanzado = explosion((bomba.centerx, bomba.centery), 3, muros, cajas_rect, personaje, corazones)
                        if jugador_alcanzado:
                            # Si el jugador fue alcanzado por la explosión, resta un corazón
                            if len(corazones) > 0:
                                corazones.pop()
                        bombas.remove((bomba, tiempo))

                # Mover al personaje con colisiones
                nueva_posicion = move_colisiones(personaje, dx, dy, colisiones, cajas_rect)


                
                # Verificar si hay colisión con los muros o las cajas
                colision_muro = False
                colision_caja = False
                for muro in muros:
                    if nueva_posicion.colliderect(muro):
                        colision_muro = True
                        break
                for caja in cajas_rect:
                    if nueva_posicion.colliderect(caja):
                        colision_caja = True
                        break

                # Actualizar la posición del personaje solo si no hay colisión con un muro o una caja
                if nueva_posicion != personaje and not colision_muro and not colision_caja:
                    personaje = nueva_posicion




                    
                # Calcular la diferencia entre las coordenadas del enemigo y el punto de destino actual
                dx = punto_destino_actual[0] - enemigo_x
                dy = punto_destino_actual[1] - enemigo_y

                # Normalizar la dirección para que el enemigo se mueva a una velocidad constante
                norm = (dx ** 2 + dy ** 2) ** 0.5
                if norm != 0:
                    dx = dx / norm * velocidad_x
                    dy = dy / norm * velocidad_y

                # Mover al enemigo hacia el punto de destino actual
                enemigo_x += dx
                enemigo_y += dy

                def verificar_destino(enemigo_x, enemigo_y, punto_destino_actual, punto_destino1, punto_destino2):
                    # Verificar si el enemigo ha llegado al punto de destino actual
                    if abs(enemigo_x - punto_destino_actual[0]) < 5 and abs(enemigo_y - punto_destino_actual[1]) < 5:
                        # Cambiar al siguiente punto de destino
                        if punto_destino_actual == punto_destino1:
                            return punto_destino2
                        else:
                            return punto_destino1
                    else:
                        return punto_destino_actual
                # Llamar a la función recursiva para verificar y cambiar el punto de destino actual
                punto_destino_actual = verificar_destino(enemigo_x, enemigo_y, punto_destino_actual, punto_destino1, punto_destino2)

                # Calcular la diferencia entre las coordenadas del enemigo 2 y el punto de destino actual
                dx2 = punto_destino_actual2[0] - enemigo2_x
                dy2 = punto_destino_actual2[1] - enemigo2_y

                # Normalizar la dirección para que el enemigo 2 se mueva a una velocidad constante
                norm2 = (dx2 ** 2 + dy2 ** 2) ** 0.5
                if norm2 != 0:
                    dx2 = dx2 / norm2 * velocidad2_x
                    dy2 = dy2 / norm2 * velocidad2_y

                # Mover al enemigo 2 hacia el punto de destino actual
                enemigo2_x += dx2
                enemigo2_y += dy2

                def verificar_destino(enemigo2_x, enemigo2_y, punto_destino_actual2, punto_destino2_1, punto_destino2_2):
                    # Verificar si el enemigo ha llegado al punto de destino actual
                    if abs(enemigo2_x - punto_destino_actual2[0]) < 5 and abs(enemigo2_y - punto_destino_actual2[1]) < 5:
                        # Cambiar al siguiente punto de destino
                        if punto_destino_actual2 == punto_destino2_1:
                            return punto_destino2_2
                        else:
                            return punto_destino2_1
                    else:
                        return punto_destino_actual2
                # Llamar a la función recursiva para verificar y cambiar el punto de destino actual del enemigo 2
                punto_destino_actual2 = verificar_destino(enemigo2_x, enemigo2_y, punto_destino_actual2, punto_destino2_1, punto_destino2_2)



                # Llamar a la función recursiva para detectar colisiones con las estrellas y actualizar los puntos, la lista de posiciones de estrellas y la bandera de colisión con la estrella
                puntos, estrellas_posiciones, colision_estrella = detectar_colisiones_estrella(personaje, estrellas_posiciones, puntos)
                # Llamar a la función recursiva para detectar colisiones con las estrellas y actualizar los puntos, la lista de posiciones de estrellas y la bandera de colisión con la estrella
            

                # Verificar si el enemigo y el jugador están en la misma posición
                if verificar_colision_jugador_enemigo(personaje, enemigo_x, enemigo_y):
                    # Reducir el contador de vidas del jugador en uno
                    vidas -= 1
                    # Reiniciar la posición del enemigo
                    enemigo_x, enemigo_y = 775, 200
                    
                puntos, llave_posicion, colision_llave = detectar_colisiones_llave(personaje, llave_posicion, puntos)
                if colision_llave:
                    llaves += 1

                # Dibujar puertas subterráneas en la superficie
                dibujar_puertas_subterraneas(ventana, puertas_posiciones)
                
                # Detectar colisiones con las puertas subterráneas
                puntos, puertas_posiciones, colision_puerta_subterranea = detectar_colisiones_puerta_subterranea(personaje, puertas_posiciones, puntos)
                

                # Dibujar los elementos del juego
                ventana.blit(imagen_fondo, (0, 0))
                dibujar_estrellas(ventana, estrellas_posiciones)
                if colision_estrella:
                # Hacer la estrella transparente
                    imagen_estrella = hacer_estrella_transparente()
                dibujar_llaves(ventana, llave_posicion)
                if colision_llave:
                # Hacer la estrella transparente
                    imagen_llave = hacer_llave_transparente()

                ventana.blit(i_enemigo1, (enemigo_x, enemigo_y))
                ventana.blit(i_enemigo2, (enemigo2_x, enemigo2_y))
                dibujar_puertas_subterraneas(ventana, puertas_posiciones)
                ventana.blit(imagen_estrella, (80, 80))
                ventana.blit(imagen_llave, (170, 372))
                # Dibujar las cajas en el mapa
                for posicion in cajas_posiciones:
                    ventana.blit(imagen_caja, posicion)
                dibujar_muros(ventana, muros)
                for bomba in bombas:
                    ventana.blit(imagen_bomba, bomba[0])
                    
                
                if personaje.colliderect(pygame.Rect(x_puerta_subterranea, y_puerta_subterranea, 55, 55)):
                    # Verificar si el contador de llaves es igual a 1
                    if llaves == 1:
                        # Cambiar al mapa2
                        mapa = mapa2

                        # Recalcular los muros y colisiones para el nuevo mapa
                        muros, colisiones = construir_mapa(mapa, ancho_muro, alto_muro)
                if personaje.colliderect(pygame.Rect(x_puerta_subterranea2, y_puerta_subterranea2, 55, 55)):
                    # Verificar si el contador de llaves es igual a 1
                    if llaves == 2:
                        # Cambiar al mapa2
                        mapa2 = mapa3

                        # Recalcular los muros y colisiones para el nuevo mapa
                        muros, colisiones = construir_mapa(mapa3, ancho_muro, alto_muro)
                

                ventana.blit(direccion_imagen[direccion_personaje], personaje)

                # Dibujar la barra de información
                tiempo = time.time() - tiempo_inicial
                dibujar_barra_informacion(ventana, vidas, puntos, llaves, tiempo)
                
                
                # Detectar colisiones con la puerta subterránea 3
                if personaje.colliderect(pygame.Rect(75, 430, 55, 55)):
                # Verificar si el contador de llaves es igual a 3
                    if llaves == 3:
                        # Crear la ventana emergente
                        ventana_emergente = pygame.display.set_mode((400, 200))
                        pygame.display.set_caption("¡Ganaste!")
                        
                        WHITE = (255, 255, 255)
                        GRAY = (200, 200, 200)
                        BLACK = (0, 0, 0)
                        
                        def create_button(text, fuente, color, hover_color, surface, x, y, width, height, action=None):
                            mouse_pos = pygame.mouse.get_pos()
                            click = pygame.mouse.get_pressed()

                            if x < mouse_pos[0] < x + width and y < mouse_pos[1] < y + height:
                                pygame.draw.rect(surface, hover_color, (x, y, width, height))
                                if click[0] == 1 and action is not None:
                                    action()
                            else:
                                pygame.draw.rect(surface, color, (x, y, width, height))

                            draw_text(text, fuente, (0, 0, 0), surface, x + width // 2, y + height // 2)

                        def draw_text(text, fuente, color, surface, x, y):
                            text_obj = fuente.render(text, True, color)
                            text_rect = text_obj.get_rect()
                            text_rect.center = (x, y)
                            surface.blit(text_obj, text_rect)

                        # Bucle principal de la ventana emergente
                        # Coordenadas y dimensiones del botón para regresar a la ventana principal
                        boton_rect_regresar = pygame.Rect(150, 120, 100, 50)
                        # Fuente para el texto en la ventana emergente
                        fuente = pygame.font.Font(None, 36)

                        # Crear la superficie de texto
                        texto_ganaste = "¡Ganaste!"
                        color_texto = (0, 0, 0)  # Color del texto
                        texto_surface = fuente.render(texto_ganaste, True, color_texto)
                        # Bucle principal de la ventana emergente
                        ventana_emergente_abierta = True
                        while ventana_emergente_abierta:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    ventana_emergente_abierta = False
                                    # Salir del juego completamente
                                    pygame.quit()
                                    sys.exit()
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                    # Verificar si se hizo clic en el botón de regresar
                                    if boton_rect_regresar.collidepoint(event.pos):
                                        # Salir del bucle para cerrar la ventana emergente
                                        ventana_emergente_abierta = False

                            # Dibujar contenido de la ventana emergente
                            ventana_emergente.fill((255, 255, 255))  # Color de fondo blanco
                            # Agregar texto u otras imágenes aquí si lo deseas
                            create_button("Regresar", fuente, GRAY, BLACK, ventana_emergente, 150, 120, 100, 50, menu)
                            ventana_emergente.blit(texto_surface, (150 - texto_surface.get_width() // 2, 80))

                            # Actualizar la ventana emergente
                            pygame.display.flip()



                # Actualizar la ventana
                pygame.display.flip()

            # Salir del juego
            pygame.quit()
            pass

        def open_game_2():
            # Inicializar
            pygame.init()
            tiempo_inicial = time.time()
            puntos = 0
            llaves = 0
            fuente = pygame.font.SysFont(None, 30)
            # Medidas
            ANCHO = 900
            ALTO = 700

            # Tamaño del mapa
            TAMANO_MAPA_X = 13
            TAMANO_MAPA_Y = 9

            # Tamaño del mapa y tamaño de los muros
            ANCHO_MAPA = 600
            ALTO_MAPA = 450

            # Definir dimensiones de la ventana emergente
            VENTANA_EMERGENTE_ANCHO = 400
            VENTANA_EMERGENTE_ALTO = 200

            # Colores
            BLANCO = (255, 255, 255)
            NEGRO = (0, 0, 0)
            ROJO = (255, 0, 0)

            # Tamaño del mapa
            TAMANO_MAPA_X = 13
            TAMANO_MAPA_Y = 9

            # Tamaño del mapa y tamaño de los muros
            ANCHO_MAPA = 600
            ALTO_MAPA = 450
            ANCHO_MURO = ANCHO_MAPA // TAMANO_MAPA_X
            ALTO_MURO = ALTO_MAPA // TAMANO_MAPA_Y



            # Mapa1
            mapa = [
                
                "xxxxxxxxxxxxx",
                "x           x",
                "x x x x x x x",
                "x           x",
                "x x x x x x x",
                "x           x",
                "xxx x x x x x",
                "x          xx",
                "xxxxxxxxxxxxx",
                "             "
            ]
            # Mapa2

            mapa2 = [
                
                "xxxxxxxxxxxxx",
                "xx          x",
                "x x x x x x x",
                "x    x      x",
                "x x x   x x x",
                "x   x       x",
                "xx   x x  x x",
                "x   x   x  xx",
                "xxxxxxxxxxxxx",
                "             "
            ]
            # Mapa1
            mapa3 = [
                
                "xxxxxxxxxxxxx",
                "xx          x",
                "x x x x   x x",
                "x    x      x",
                "x x x   x x x",
                "x   x       x",
                "x x    x  x x",
                "xx  x   x  xx",
                "xxxxxxxxxxxxx",
                "             "
            ]



            # Función para formatear el tiempo en minutos y segundos
            def formatear_tiempo(tiempo):
                minutos = int(tiempo // 60)
                segundos = int(tiempo % 60)
                return f"{minutos:02}:{segundos:02}"
            # Función para dibujar la barra de información con el tiempo formateado
            def dibujar_barra_informacion(superficie, vidas, puntos, llaves, tiempo, x_vida_inicial=20, y_vida=ALTO - 40, espacio_entre_elementos=40):
                # Caso base: si no quedan vidas, terminar la recursión
                if vidas <= 0:
                    # Dibujar el fondo de la barra de información al final de la recursión
                    pygame.draw.rect(superficie, BLANCO, (0, ALTO - 50, ANCHO, 50))
                    # Dibujar el contador de puntos
                    fuente = pygame.font.SysFont(None, 30)
                    texto_puntos = fuente.render("Puntos: " + str(puntos), True, NEGRO)
                    superficie.blit(texto_puntos, (ANCHO - 150, ALTO - 40))
                    # Dibujar el contador de llaves
                    texto_llaves = fuente.render("Llaves: " + str(llaves), True, NEGRO)
                    superficie.blit(texto_llaves, (ANCHO - 280, ALTO - 40))
                    # Dibujar el cronómetro formateado
                    texto_tiempo = fuente.render("Tiempo: " + formatear_tiempo(tiempo), True, NEGRO)
                    superficie.blit(texto_tiempo, (450, ALTO - 40))
                    return
                else:
                    # Dibujar la barra blanca antes de dibujar los corazones y llaves
                    pygame.draw.rect(superficie, BLANCO, (0, ALTO - 50, ANCHO, 50))
                    # Llamar recursivamente para dibujar las vidas restantes
                    dibujar_barra_informacion(superficie, vidas - 1, puntos, llaves, tiempo, x_vida_inicial + espacio_entre_elementos + imagen_vida.get_width(), y_vida, espacio_entre_elementos)
                    # Dibujar una vida después de dibujar las vidas restantes
                    superficie.blit(imagen_vida, (x_vida_inicial, y_vida))



                # Escribir texto en la barra de información
                fuente = pygame.font.SysFont(None, 24)
                texto = ""
                texto_renderizado = fuente.render(texto, True, NEGRO)
                superficie.blit(texto_renderizado, (20, ALTO - 40))


            # Función para construir el mapa recursivamente
            def construir_mapa(mapa, ancho_muro, alto_muro, x=0, y=0):
                # Obtener las dimensiones del mapa
                TAMANO_MAPA_Y = len(mapa)

                # Caso base: si hemos alcanzado el final del mapa, retornar una lista vacía de muros y colisiones
                if y >= TAMANO_MAPA_Y:
                    return [], []

                # Caso recursivo: explorar la siguiente fila del mapa
                muros_fila, colisiones_fila = construir_mapa(mapa, ancho_muro, alto_muro, 0, y + 1)

                # Lista para almacenar los muros y colisiones de esta fila
                muros = []
                colisiones = []

                # Iterar sobre cada columna en la fila actual
                for x_actual, caracter in enumerate(mapa[y]):
                    # Calcular las coordenadas x e y del muro actual
                    x_actual *= ancho_muro
                    x_actual += x
                    y_actual = y * alto_muro

                    if caracter == "x":
                        # Crear un rectángulo para representar el muro
                        rect_muro = pygame.Rect(x_actual, y_actual, ancho_muro, alto_muro)
                        muros.append(rect_muro)
                        # Crear un rectángulo de colisión para el muro (ligeramente más pequeño para evitar superposiciones)
                        rect_colision = pygame.Rect(x_actual + 2, y_actual + 2, ancho_muro - 4, alto_muro - 4)
                        colisiones.append(rect_colision)

                # Combinar los muros y colisiones de esta fila con los de las filas anteriores
                muros.extend(muros_fila)
                colisiones.extend(colisiones_fila)

                return muros, colisiones

            def dibujar_muros(superficie, muros):
                if not muros:  # Caso base: si la lista de muros está vacía, detener la recursión
                    return
                
                # Obtener el primer muro de la lista
                primer_muro = muros[0]
                
                # Dibujar la imagen de muro en la superficie
                superficie.blit(imagen_muro, (primer_muro.x, primer_muro.y))
                
                # Llamar recursivamente a la función con el resto de la lista de muros
                dibujar_muros(superficie, muros[1:])






            def explosion(posicion, rango, muros, cajas, personaje, corazones):
                alcance = [(0, 0)]  # La propia posición de la bomba
                
                muros_a_eliminar = []
                cajas_a_eliminar = []
                jugador_alcanzado = False  # Bandera para verificar si el jugador fue alcanzado por la explosión
                
                # Verificar si la explosión alcanza al personaje
                for x, y in alcance:
                    if personaje.colliderect(pygame.Rect(x * ANCHO_MURO, y * ALTO_MURO, ANCHO_MURO, ALTO_MURO)):
                        jugador_alcanzado = True  # El jugador fue alcanzado por la explosión
                        break
                
                for direccion in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    for i in range(1, rango + 1):
                        nueva_posicion = (posicion[0] + direccion[0] * i, posicion[1] + direccion[1] * i)
                        alcance.append(nueva_posicion)
                        # Romper la explosión si se encuentra un muro
                        for muro in muros:
                            if muro.collidepoint(nueva_posicion):
                                muros_a_eliminar.append(muro)
                                break
                        else:
                            # Romper la explosión si se encuentra una caja
                            for caja in cajas:
                                if caja.collidepoint(nueva_posicion):
                                    cajas_a_eliminar.append(caja)
                                    break
                            continue
                        break
                # Eliminar los muros alcanzados por la explosión
                for muro in muros_a_eliminar:
                    muros.remove(muro)
                # Eliminar las cajas alcanzadas por la explosión
                for caja in cajas_a_eliminar:
                    cajas.remove(caja)
                return alcance, jugador_alcanzado





            #al detectar una colicion no deja que el npc se mueva 
            #cuando lo hay colicion lo deja avanzar a la siguiente posicion 
            def move_colisiones(personaje, dx, dy, colisiones, cajas, indice=0):
                if indice == len(colisiones):
                    # Si no hay más objetos para verificar colisión, devolver la nueva posición
                    return personaje.move(dx, dy)
                
                obj = colisiones[indice]
                nueva_posicion = personaje.move(dx, dy)
                
                # Verificar colisión con las cajas
                for caja in cajas:
                    if nueva_posicion.colliderect(caja):
                        # Si hay colisión con una caja, no mover al personaje
                        return personaje
                
                if nueva_posicion.colliderect(obj):
                    # Si hay colisión con un objeto, no mover al personaje
                    return personaje
                
                # Llamar recursivamente para verificar la siguiente colisión
                return move_colisiones(personaje, dx, dy, colisiones, cajas, indice + 1)

            # Función para mover recursivamente al enemigo
            def mover_enemigo(x, y, destino_x, destino_y, cajas):
                # Caso base: si el enemigo ha alcanzado las coordenadas de destino, retornar las coordenadas actuales
                if x == destino_x and y == destino_y:
                    return x, y

                # Calcular la dirección del movimiento en x e y
                if destino_x > x:
                    nueva_x = min(x + velocidad_x, destino_x)
                elif destino_x < x:
                    nueva_x = max(x - velocidad_x, destino_x)
                else:
                    nueva_x = x

                if destino_y > y:
                    nueva_y = min(y + velocidad_y, destino_y)
                elif destino_y < y:
                    nueva_y = max(y - velocidad_y, destino_y)
                else:
                    nueva_y = y

                # Verificar si hay colisión con las cajas
                for caja in cajas:
                    if pygame.Rect(nueva_x, nueva_y, e_ancho, e_alto).colliderect(caja):
                        # Si hay colisión con una caja, no mover al enemigo
                        return x, y
                
                # Llamar recursivamente a la función mover_enemigo() con las nuevas coordenadas
                return mover_enemigo(nueva_x, nueva_y, destino_x, destino_y, cajas)

            def verificar_colision_jugador_enemigo(jugador_rect, enemigo_x, enemigo_y):
                return jugador_rect.colliderect(pygame.Rect(enemigo_x, enemigo_y, e_ancho, e_alto))




            def dibujar_estrellas(superficie, estrellas_posiciones):
                for pos_estrella_x, pos_estrella_y in estrellas_posiciones:
                    superficie.blit(imagen_estrella, (pos_estrella_x, pos_estrella_y))
                    superficie.blit(imagen_estrella2, (pos_estrella_x, pos_estrella_y))  # Dibujar la segunda estrella en la misma posición
            # Función recursiva para detectar colisiones con las estrellas en diferentes posiciones
            def detectar_colisiones_estrella(personaje_rect, estrellas_posiciones, puntos):
                # Variable para verificar si se detectó una colisión con una estrella
                colision_estrella = False
                
                # Función interna para detectar colisiones
                def detectar_colisiones_recursiva(estrellas_posiciones, puntos, colision_estrella):
                    if not estrellas_posiciones:
                        # Si no quedan estrellas, devolver los puntos actualizados y la lista de posiciones de estrellas
                        return puntos, [], colision_estrella
                    
                    # Extraer la posición de la primera estrella en la lista
                    pos_estrella_x, pos_estrella_y = estrellas_posiciones[0]
                    
                    # Verificar colisión entre el personaje y la estrella
                    if personaje_rect.colliderect(pygame.Rect(pos_estrella_x, pos_estrella_y, ANCHO_MURO, ALTO_MURO)):
                        # Aumentar 100 puntos si hay colisión
                        puntos += 100
                        # Eliminar la posición de la estrella de la lista
                        estrellas_posiciones.pop(0)
                        colision_estrella = True
                        
                        # Hacer la estrella transparente
                        hacer_estrella_transparente()
                        
                        # Llamar recursivamente a la función con la lista actualizada de estrellas
                        return detectar_colisiones_recursiva(estrellas_posiciones, puntos, colision_estrella)
                    
                    else:
                        # Si no hay colisión, llamar recursivamente a la función con la lista restante de estrellas
                        puntos, estrellas_posiciones, colision_estrella = detectar_colisiones_recursiva(estrellas_posiciones[1:], puntos, colision_estrella)
                        return puntos, [(pos_estrella_x, pos_estrella_y)] + estrellas_posiciones, colision_estrella
                
                # Llamar a la función interna para iniciar la detección de colisiones
                return detectar_colisiones_recursiva(estrellas_posiciones, puntos, colision_estrella)
            # Después de obtener los puntos necesarios
            def hacer_estrella_transparente():
                # Cargar la imagen de la estrella con transparencia alfa
                imagen_estrella_transparente = pygame.image.load("mapas/estre.jpg").convert_alpha()
                
                # Ajustar el valor alfa de los píxeles de la imagen para hacerla más transparente
                # Por ejemplo, reducir el valor alfa a la mitad (0 sería completamente transparente, 255 sería opaco)
                factor_transparencia = 2  # Por ejemplo, reducir a la mitad la transparencia original
                imagen_estrella_transparente.set_alpha(factor_transparencia)
                
                # Devolver la imagen de la estrella transparente
                return imagen_estrella_transparente





            def dibujar_llaves(superficie, llaves_posiciones):
                for pos_llave_x, pos_llave_y in llaves_posiciones:
                    superficie.blit(imagen_llave, (pos_llave_x, pos_llave_y))
                    superficie.blit(imagen_llave2, (pos_llave_x, pos_llave_y))
                    superficie.blit(imagen_llave3, (pos_llave_x, pos_llave_y))        
            # Función recursiva para detectar colisiones con las llaves en diferentes posiciones
            def detectar_colisiones_llave(personaje_rect, llaves_posiciones, puntos):
                # Variable para verificar si se detectó una colisión con una llave
                colision_llave = False
                
                # Función interna para detectar colisiones
                def detectar_colisiones_recursiva(llaves_posiciones, puntos, colision_llave):
                    if not llaves_posiciones:
                        # Si no quedan llaves, devolver los puntos actualizados y la lista de posiciones de llaves
                        return puntos, [], colision_llave
                    
                    # Extraer la posición de la primera llave en la lista
                    pos_llave_x, pos_llave_y = llaves_posiciones[0]
                    
                    # Verificar colisión entre el personaje y la llave
                    if personaje_rect.colliderect(pygame.Rect(pos_llave_x, pos_llave_y, ANCHO_MURO, ALTO_MURO)):
                        # Aumentar 100 puntos si hay colisión
                        puntos += 250
                        # Eliminar la posición de la llave de la lista
                        llaves_posiciones.pop(0)
                        colision_llave = True
                        
                        # Hacer la llave transparente
                        hacer_llave_transparente()
                        
                        # Llamar recursivamente a la función con la lista actualizada de llaves
                        return detectar_colisiones_recursiva(llaves_posiciones, puntos, colision_llave)
                    
                    else:
                        # Si no hay colisión, llamar recursivamente a la función con la lista restante de llaves
                        puntos, llaves_posiciones, colision_llave = detectar_colisiones_recursiva(llaves_posiciones[1:], puntos, colision_llave)
                        return puntos, [(pos_llave_x, pos_llave_y)] + llaves_posiciones, colision_llave
                
                # Llamar a la función interna para iniciar la detección de colisiones
                return detectar_colisiones_recursiva(llaves_posiciones, puntos, colision_llave)
            # Después de obtener los puntos necesarios
            def hacer_llave_transparente():
                # Cargar la imagen de la llave con transparencia alfa
                imagen_llave_transparente = pygame.image.load("mapas/llave.jpg").convert_alpha()
                
                # Ajustar el valor alfa de los píxeles de la imagen para hacerla más transparente
                # Por ejemplo, reducir el valor alfa a la mitad (0 sería completamente transparente, 255 sería opaco)
                factor_transparencia = 2  # Por ejemplo, reducir a la mitad la transparencia original
                imagen_llave_transparente.set_alpha(factor_transparencia)
                
                # Devolver la imagen de la llave transparente
                return imagen_llave_transparente




            def colocar_bomba(bombas, personaje_x, personaje_y, bombas_colocadas, MAX_BOMBAS):
                # Función auxiliar para verificar si una bomba está en una posición
                def bomba_en_posicion(x, y):
                    for bomba, _ in bombas:
                        if bomba.colliderect(pygame.Rect(x, y, 20, 20)):
                            return True
                    return False

                # Verificar si hay espacio para colocar la bomba
                if bombas_colocadas >= MAX_BOMBAS:
                    return bombas, bombas_colocadas

                # Verificar si la posición para colocar la bomba está ocupada por otra bomba
                if bomba_en_posicion(personaje_x, personaje_y):
                    return bombas, bombas_colocadas

                # Si la posición no está ocupada, colocar la bomba
                bomba = pygame.Rect(personaje_x, personaje_y, 20, 20)
                bombas.append((bomba, time.time()))
                bombas_colocadas += 1

                return bombas, bombas_colocadas


            def verificar_explosion(bombas, personaje_rect, corazones):
                for bomba, _ in bombas:
                    # Verificar si la explosión alcanza al personaje
                    if bomba.colliderect(personaje_rect):
                        if len(corazones) > 0:
                            # Si hay corazones disponibles, eliminar uno
                            corazones.pop()
                        return True  # Indicar que hubo una explosión que alcanzó al personaje
                # Llamar recursivamente a la función con las bombas restantes y el mismo personaje
                if bombas:
                    return verificar_explosion(bombas[:-1], personaje_rect, corazones)
                return False  # Indicar que no hubo explosión que alcanzó al personaje



            def dibujar_puertas_subterraneas(superficie, puertas_posiciones):
                for pos_puerta_x, pos_puerta_y in puertas_posiciones:
                    superficie.blit(imagen_puerta_subterranea, (pos_puerta_x, pos_puerta_y))
            # Función recursiva para detectar colisiones con las puertas subterráneas en diferentes posiciones
            def detectar_colisiones_puerta_subterranea(personaje_rect, puertas_posiciones, puntos):
                # Variable para verificar si se detectó una colisión con una puerta subterránea
                colision_puerta_subterranea = False
                
                # Función interna para detectar colisiones
                def detectar_colisiones_recursiva(puertas_posiciones, puntos, colision_puerta_subterranea):
                    if not puertas_posiciones:
                        # Si no quedan puertas subterráneas, devolver los puntos actualizados y la lista de posiciones de puertas subterráneas
                        return puntos, [], colision_puerta_subterranea
                    
                    # Extraer la posición de la primera puerta subterránea en la lista
                    pos_puerta_x, pos_puerta_y = puertas_posiciones[0]
                    
                    # Verificar colisión entre el personaje y la puerta subterránea
                    if personaje_rect.colliderect(pygame.Rect(pos_puerta_x, pos_puerta_y, 55, 55)):
                        # Aumentar puntos si hay colisión
                        puntos += 500
                        # Eliminar la posición de la puerta subterránea de la lista
                        puertas_posiciones.pop(0)
                        colision_puerta_subterranea = True
                        
                        # Abrir la puerta subterránea
                        abrir_puerta_subterranea()
                        
                        # Llamar recursivamente a la función con la lista actualizada de puertas subterráneas
                        return detectar_colisiones_recursiva(puertas_posiciones, puntos, colision_puerta_subterranea)
                    
                    else:
                        # Si no hay colisión, llamar recursivamente a la función con la lista restante de puertas subterráneas
                        puntos, puertas_posiciones, colision_puerta_subterranea = detectar_colisiones_recursiva(puertas_posiciones[1:], puntos, colision_puerta_subterranea)
                        return puntos, [(pos_puerta_x, pos_puerta_y)] + puertas_posiciones, colision_puerta_subterranea
                
                # Llamar a la función interna para iniciar la detección de colisiones
                return detectar_colisiones_recursiva(puertas_posiciones, puntos, colision_puerta_subterranea)
            # Después de obtener los puntos necesarios
            def abrir_puerta_subterranea():
                # Cargar la imagen de la puerta subterránea abierta
                imagen_puerta_subterranea_abierta = pygame.image.load("mapas/puerta_subterranea.png").convert_alpha()
                
                # Ajustar el valor alfa de los píxeles de la imagen para hacerla visible
                # Por ejemplo, establecer el valor alfa a 255 para que sea completamente opaca
                factor_visibilidad = 5  # Por ejemplo, establecer la visibilidad al máximo
                imagen_puerta_subterranea_abierta.set_alpha(factor_visibilidad)
                
                # Devolver la imagen de la puerta subterránea abierta
                return imagen_puerta_subterranea_abierta






            # Ventana
            ventana = pygame.display.set_mode((ANCHO, ALTO))
            pygame.display.set_caption("BOMBERMAN")

            # Cargar imagen de la vida
            imagen_vida = pygame.image.load("mapas/cora.jpg").convert_alpha()
            imagen_vida = pygame.transform.scale(imagen_vida, (30, 30))
            # Cargar imagen de la llave
            imagen_llave = pygame.image.load("mapas/llave.jpg").convert_alpha()
            imagen_llave = pygame.transform.scale(imagen_llave, (30, 30))
            imagen_llave2 = pygame.image.load("mapas/llave.jpg").convert_alpha()
            imagen_llave2 = pygame.transform.scale(imagen_llave2, (30, 30))
            imagen_llave3 = pygame.image.load("mapas/llave.jpg").convert_alpha()
            imagen_llave3 = pygame.transform.scale(imagen_llave3, (30, 30))
            # Cargar imagen de la estrella
            imagen_estrella = pygame.image.load("mapas/estre.jpg").convert_alpha()
            imagen_estrella = pygame.transform.scale(imagen_estrella, (ANCHO_MURO, ALTO_MURO))
            imagen_estrella2 = pygame.image.load("mapas/estre.jpg").convert_alpha()
            imagen_estrella2 = pygame.transform.scale(imagen_estrella2, (ANCHO_MURO, ALTO_MURO))

            # Datos de los muros 
            ancho_muro = ANCHO // len(mapa[0])
            alto_muro = ALTO // len(mapa)
            muros, colisiones = construir_mapa(mapa, ancho_muro, alto_muro)

            # Cargar imagen del muro
            imagen_muro = pygame.image.load("mapas/block.png").convert_alpha()
            imagen_muro = pygame.transform.scale(imagen_muro, (ancho_muro, alto_muro))

            # Cargar imagen de la bomba
            imagen_bomba = pygame.image.load("mapas/boom.jpg").convert_alpha()
            imagen_bomba = pygame.transform.scale(imagen_bomba, (35, 35))

            # Cargar imagen de la puerta subterranea
            puerta_subterranea = pygame.image.load("mapas/puerta_subterranea.png")
            imagen_puerta_subterranea = pygame.transform.scale(puerta_subterranea, (55, 55))  # para escalar la imagen 
            puerta_subterranea2 = pygame.image.load("mapas/puerta_subterranea.png")
            imagen_puerta_subterranea2 = pygame.transform.scale(puerta_subterranea2, (55, 55))  # para escalar la imagen 
            imagen_puerta_subterranea3 = pygame.image.load("mapas/puerta_subterranea.png")
            imagen_puerta_subterranea3 = pygame.transform.scale(imagen_puerta_subterranea3, (55, 55))  # para escalar la imagen 

            # Coordenadas donde se colocará la imagen
            x_puerta_subterranea = 765
            y_puerta_subterranea = 85
            x_puerta_subterranea2 = 284
            y_puerta_subterranea2 = 430

            # Cargar imagen de la caja
            caja = pygame.image.load("mapas/caja.jpg")
            imagen_caja = pygame.transform.scale(caja, (55, 55))  # para escalar la imagen 
            # Coordenadas donde se colocará la imagen
            x_caja = 690
            y_caja = 85



            # Cargar imagen de fondo
            imagen_fondo = pygame.image.load("mapas/fondo_mapa.jpg").convert()  
            imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO, ALTO))

            # Cargar imágenes del personaje para cada dirección
            personaje_arriba = pygame.image.load("proyecto/personaje2/arriba.png").convert_alpha()
            personaje_abajo = pygame.image.load("proyecto/personaje2/abajo.png").convert_alpha()
            personaje_izquierda = pygame.image.load("proyecto/personaje2/izquierda.png").convert_alpha()
            personaje_derecha = pygame.image.load("proyecto/personaje2/derecha.png").convert_alpha()

            # Definir la velocidad de movimiento del personaje
            PLAYER_SPEED = 2.6

            # Crear un diccionario para asociar la dirección con la imagen correspondiente
            direccion_imagen = {
                "izquierda": personaje_izquierda,
                "derecha": personaje_derecha,
                "arriba": personaje_arriba,
                "abajo": personaje_abajo
            }

            # Personaje
            personaje = pygame.Rect(80, 520, 40, 40)
            direccion_personaje = "derecha"

            #----LISTAS----
            #bombas
            bombas = []
            #Explosiones
            explosiones = []
            # Definir la cantidad máxima de bombas que el jugador puede colocar
            MAX_BOMBAS = 6
            # Contador para rastrear cuántas bombas ha colocado el jugador
            bombas_colocadas = 0
            #vidas del jugador 
            vidas = 4 
            corazones = [1, 2, 3]  # Ejemplo de inicialización de la lista de corazones


            # Coordenadas donde se colocarán las cajas
            cajas_posiciones = [
                (80, 145),  # Ejemplo de posición para la primera caja
                (213, 360),  # Ejemplo de posición para la segunda caja
                (353, 220),
                (695, 500),
                (630, 85),
            ]

            # Lista para almacenar los rectángulos de las cajas
            cajas_rect = []

            # Crear rectángulos para cada posición de caja y agregarlos a la lista
            for posicion in cajas_posiciones:
                caja_rect = pygame.Rect(posicion[0], posicion[1], 55, 55)  # Rectángulo con las mismas dimensiones que las cajas
                cajas_rect.append(caja_rect)

            # Lista de posiciones de estrellas en el mapa
            estrellas_posiciones = [
                (80, 80),
                (769,500)
            ]
            llave_posicion = [
                (170, 372),
                (432, 297),
                (570, 160),

            ]
            puertas_posiciones = [(765, 85), (284, 430), (75, 430)]



            #-----------------enemigo--------------------------
            e_alto=35
            e_ancho=30
            i_enemigo1 = pygame.image.load("mapas/Goblin1.jpg").convert()  
            i_enemigo1 = pygame.transform.scale(i_enemigo1, (e_ancho, e_alto))
            # Posición inicial del enemigo
            enemigo_x, enemigo_y = 775, 200
            # Posición a la que queremos mover al enemigo
            destino_x, destino_y = 775, 400
            # Velocidad del enemigo
            velocidad_x = 1
            velocidad_y = 1
            # Puntos de destino del enemigo 
            punto_destino1 = (775, 400)
            punto_destino2 = (775, 200)
            # Variable para rastrear el punto actual hacia el que se mueve el enemigo
            punto_destino_actual = punto_destino1


            #-----------------enemigo2--------------------------
            e_alto = 35
            e_ancho = 30
            i_enemigo2 = pygame.image.load("mapas/Goblin1.jpg").convert()  
            i_enemigo2 = pygame.transform.scale(i_enemigo2, (e_ancho, e_alto))
            # Posición inicial del enemigo2
            enemigo2_x, enemigo2_y = 150, 90
            # Posición a la que queremos mover al enemigo2
            destino2_x, destino2_y = 570, 90
            # Velocidad del enemigo2
            velocidad2_x = 1
            velocidad2_y = 1
            # Puntos de destino del enemigo2 
            punto_destino2_1 = (570, 90)
            punto_destino2_2 = (150, 90)
            # Variable para rastrear el punto actual hacia el que se mueve el enemigo2
            punto_destino_actual2 = punto_destino2_1



            # Bucle principal
            jugando = True
            while jugando:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        jugando = False
                    # Obtener las teclas presionadas
                keys = pygame.key.get_pressed()
                dx, dy = 0, 0
                

                if keys[pygame.K_a]:
                    dx = -PLAYER_SPEED
                    direccion_personaje = "izquierda"
                if keys[pygame.K_d]:
                    dx = PLAYER_SPEED
                    direccion_personaje = "derecha"
                if keys[pygame.K_w]:
                    dy = -PLAYER_SPEED
                    direccion_personaje = "arriba"
                if keys[pygame.K_s]:
                    dy = PLAYER_SPEED
                    direccion_personaje = "abajo"
                # Colocar una bomba si se presiona la tecla de espacio y el jugador tiene bombas disponibles
                if keys[pygame.K_SPACE] and len(bombas) < MAX_BOMBAS:
                    # Llamar a la función recursiva para verificar y colocar la bomba
                    bombas, bombas_colocadas = colocar_bomba(bombas, personaje.x, personaje.y, bombas_colocadas, MAX_BOMBAS)

                # Llamar a la función para restablecer los elementos
                #restablecer_elementos()

                for bomba, tiempo in bombas:
                    if time.time() - tiempo > 2:  # Tiempo de detonación de la bomba (2 segundos)
                        # Llamada a la función de explosión
                        alcance_explosion, jugador_alcanzado = explosion((bomba.centerx, bomba.centery), 3, muros, cajas_rect, personaje, corazones)
                        if jugador_alcanzado:
                            # Si el jugador fue alcanzado por la explosión, resta un corazón
                            if len(corazones) > 0:
                                corazones.pop()
                        bombas.remove((bomba, tiempo))

                # Mover al personaje con colisiones
                nueva_posicion = move_colisiones(personaje, dx, dy, colisiones, cajas_rect)


                
                # Verificar si hay colisión con los muros o las cajas
                colision_muro = False
                colision_caja = False
                for muro in muros:
                    if nueva_posicion.colliderect(muro):
                        colision_muro = True
                        break
                for caja in cajas_rect:
                    if nueva_posicion.colliderect(caja):
                        colision_caja = True
                        break

                # Actualizar la posición del personaje solo si no hay colisión con un muro o una caja
                if nueva_posicion != personaje and not colision_muro and not colision_caja:
                    personaje = nueva_posicion




                    
                # Calcular la diferencia entre las coordenadas del enemigo y el punto de destino actual
                dx = punto_destino_actual[0] - enemigo_x
                dy = punto_destino_actual[1] - enemigo_y

                # Normalizar la dirección para que el enemigo se mueva a una velocidad constante
                norm = (dx ** 2 + dy ** 2) ** 0.5
                if norm != 0:
                    dx = dx / norm * velocidad_x
                    dy = dy / norm * velocidad_y

                # Mover al enemigo hacia el punto de destino actual
                enemigo_x += dx
                enemigo_y += dy

                def verificar_destino(enemigo_x, enemigo_y, punto_destino_actual, punto_destino1, punto_destino2):
                    # Verificar si el enemigo ha llegado al punto de destino actual
                    if abs(enemigo_x - punto_destino_actual[0]) < 5 and abs(enemigo_y - punto_destino_actual[1]) < 5:
                        # Cambiar al siguiente punto de destino
                        if punto_destino_actual == punto_destino1:
                            return punto_destino2
                        else:
                            return punto_destino1
                    else:
                        return punto_destino_actual
                # Llamar a la función recursiva para verificar y cambiar el punto de destino actual
                punto_destino_actual = verificar_destino(enemigo_x, enemigo_y, punto_destino_actual, punto_destino1, punto_destino2)

                # Calcular la diferencia entre las coordenadas del enemigo 2 y el punto de destino actual
                dx2 = punto_destino_actual2[0] - enemigo2_x
                dy2 = punto_destino_actual2[1] - enemigo2_y

                # Normalizar la dirección para que el enemigo 2 se mueva a una velocidad constante
                norm2 = (dx2 ** 2 + dy2 ** 2) ** 0.5
                if norm2 != 0:
                    dx2 = dx2 / norm2 * velocidad2_x
                    dy2 = dy2 / norm2 * velocidad2_y

                # Mover al enemigo 2 hacia el punto de destino actual
                enemigo2_x += dx2
                enemigo2_y += dy2

                def verificar_destino(enemigo2_x, enemigo2_y, punto_destino_actual2, punto_destino2_1, punto_destino2_2):
                    # Verificar si el enemigo ha llegado al punto de destino actual
                    if abs(enemigo2_x - punto_destino_actual2[0]) < 5 and abs(enemigo2_y - punto_destino_actual2[1]) < 5:
                        # Cambiar al siguiente punto de destino
                        if punto_destino_actual2 == punto_destino2_1:
                            return punto_destino2_2
                        else:
                            return punto_destino2_1
                    else:
                        return punto_destino_actual2
                # Llamar a la función recursiva para verificar y cambiar el punto de destino actual del enemigo 2
                punto_destino_actual2 = verificar_destino(enemigo2_x, enemigo2_y, punto_destino_actual2, punto_destino2_1, punto_destino2_2)



                # Llamar a la función recursiva para detectar colisiones con las estrellas y actualizar los puntos, la lista de posiciones de estrellas y la bandera de colisión con la estrella
                puntos, estrellas_posiciones, colision_estrella = detectar_colisiones_estrella(personaje, estrellas_posiciones, puntos)
                # Llamar a la función recursiva para detectar colisiones con las estrellas y actualizar los puntos, la lista de posiciones de estrellas y la bandera de colisión con la estrella
            

                # Verificar si el enemigo y el jugador están en la misma posición
                if verificar_colision_jugador_enemigo(personaje, enemigo_x, enemigo_y):
                    # Reducir el contador de vidas del jugador en uno
                    vidas -= 1
                    # Reiniciar la posición del enemigo
                    enemigo_x, enemigo_y = 775, 200
                    
                puntos, llave_posicion, colision_llave = detectar_colisiones_llave(personaje, llave_posicion, puntos)
                if colision_llave:
                    llaves += 1

                # Dibujar puertas subterráneas en la superficie
                dibujar_puertas_subterraneas(ventana, puertas_posiciones)
                
                # Detectar colisiones con las puertas subterráneas
                puntos, puertas_posiciones, colision_puerta_subterranea = detectar_colisiones_puerta_subterranea(personaje, puertas_posiciones, puntos)
                

                # Dibujar los elementos del juego
                ventana.blit(imagen_fondo, (0, 0))
                dibujar_estrellas(ventana, estrellas_posiciones)
                if colision_estrella:
                # Hacer la estrella transparente
                    imagen_estrella = hacer_estrella_transparente()
                dibujar_llaves(ventana, llave_posicion)
                if colision_llave:
                # Hacer la estrella transparente
                    imagen_llave = hacer_llave_transparente()

                ventana.blit(i_enemigo1, (enemigo_x, enemigo_y))
                ventana.blit(i_enemigo2, (enemigo2_x, enemigo2_y))
                dibujar_puertas_subterraneas(ventana, puertas_posiciones)
                ventana.blit(imagen_estrella, (80, 80))
                ventana.blit(imagen_llave, (170, 372))
                # Dibujar las cajas en el mapa
                for posicion in cajas_posiciones:
                    ventana.blit(imagen_caja, posicion)
                dibujar_muros(ventana, muros)
                for bomba in bombas:
                    ventana.blit(imagen_bomba, bomba[0])
                    
                
                if personaje.colliderect(pygame.Rect(x_puerta_subterranea, y_puerta_subterranea, 55, 55)):
                    # Verificar si el contador de llaves es igual a 1
                    if llaves == 1:
                        # Cambiar al mapa2
                        mapa = mapa2

                        # Recalcular los muros y colisiones para el nuevo mapa
                        muros, colisiones = construir_mapa(mapa, ancho_muro, alto_muro)
                if personaje.colliderect(pygame.Rect(x_puerta_subterranea2, y_puerta_subterranea2, 55, 55)):
                    # Verificar si el contador de llaves es igual a 1
                    if llaves == 2:
                        # Cambiar al mapa2
                        mapa2 = mapa3

                        # Recalcular los muros y colisiones para el nuevo mapa
                        muros, colisiones = construir_mapa(mapa3, ancho_muro, alto_muro)
                

                ventana.blit(direccion_imagen[direccion_personaje], personaje)

                # Dibujar la barra de información
                tiempo = time.time() - tiempo_inicial
                dibujar_barra_informacion(ventana, vidas, puntos, llaves, tiempo)
                
                
                # Detectar colisiones con la puerta subterránea 3
                if personaje.colliderect(pygame.Rect(75, 430, 55, 55)):
                # Verificar si el contador de llaves es igual a 3
                    if llaves == 3:
                        # Crear la ventana emergente
                        ventana_emergente = pygame.display.set_mode((400, 200))
                        pygame.display.set_caption("¡Ganaste!")
                        
                        WHITE = (255, 255, 255)
                        GRAY = (200, 200, 200)
                        BLACK = (0, 0, 0)
                        
                        def create_button(text, fuente, color, hover_color, surface, x, y, width, height, action=None):
                            mouse_pos = pygame.mouse.get_pos()
                            click = pygame.mouse.get_pressed()

                            if x < mouse_pos[0] < x + width and y < mouse_pos[1] < y + height:
                                pygame.draw.rect(surface, hover_color, (x, y, width, height))
                                if click[0] == 1 and action is not None:
                                    action()
                            else:
                                pygame.draw.rect(surface, color, (x, y, width, height))

                            draw_text(text, fuente, (0, 0, 0), surface, x + width // 2, y + height // 2)

                        def draw_text(text, fuente, color, surface, x, y):
                            text_obj = fuente.render(text, True, color)
                            text_rect = text_obj.get_rect()
                            text_rect.center = (x, y)
                            surface.blit(text_obj, text_rect)

                        # Bucle principal de la ventana emergente
                        # Coordenadas y dimensiones del botón para regresar a la ventana principal
                        boton_rect_regresar = pygame.Rect(150, 120, 100, 50)
                        # Fuente para el texto en la ventana emergente
                        fuente = pygame.font.Font(None, 36)

                        # Crear la superficie de texto
                        texto_ganaste = "¡Ganaste!"
                        color_texto = (0, 0, 0)  # Color del texto
                        texto_surface = fuente.render(texto_ganaste, True, color_texto)
                        # Bucle principal de la ventana emergente
                        ventana_emergente_abierta = True
                        while ventana_emergente_abierta:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    ventana_emergente_abierta = False
                                    # Salir del juego completamente
                                    pygame.quit()
                                    sys.exit()
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                    # Verificar si se hizo clic en el botón de regresar
                                    if boton_rect_regresar.collidepoint(event.pos):
                                        # Salir del bucle para cerrar la ventana emergente
                                        ventana_emergente_abierta = False

                            # Dibujar contenido de la ventana emergente
                            ventana_emergente.fill((255, 255, 255))  # Color de fondo blanco
                            # Agregar texto u otras imágenes aquí si lo deseas
                            create_button("Regresar", fuente, GRAY, BLACK, ventana_emergente, 150, 120, 100, 50, menu)
                            ventana_emergente.blit(texto_surface, (150 - texto_surface.get_width() // 2, 80))

                            # Actualizar la ventana emergente
                            pygame.display.flip()



                # Actualizar la ventana
                pygame.display.flip()

            # Salir del juego
            pygame.quit()
            pass

        def open_game_3():
            # Inicializar
            pygame.init()
            tiempo_inicial = time.time()
            puntos = 0
            llaves = 0
            fuente = pygame.font.SysFont(None, 30)
            # Medidas
            ANCHO = 900
            ALTO = 700

            # Tamaño del mapa
            TAMANO_MAPA_X = 13
            TAMANO_MAPA_Y = 9

            # Tamaño del mapa y tamaño de los muros
            ANCHO_MAPA = 600
            ALTO_MAPA = 450

            # Definir dimensiones de la ventana emergente
            VENTANA_EMERGENTE_ANCHO = 400
            VENTANA_EMERGENTE_ALTO = 200

            # Colores
            BLANCO = (255, 255, 255)
            NEGRO = (0, 0, 0)
            ROJO = (255, 0, 0)

            # Tamaño del mapa
            TAMANO_MAPA_X = 13
            TAMANO_MAPA_Y = 9

            # Tamaño del mapa y tamaño de los muros
            ANCHO_MAPA = 600
            ALTO_MAPA = 450
            ANCHO_MURO = ANCHO_MAPA // TAMANO_MAPA_X
            ALTO_MURO = ALTO_MAPA // TAMANO_MAPA_Y



            # Mapa1
            mapa = [
                
                "xxxxxxxxxxxxx",
                "x           x",
                "x x x x x x x",
                "x           x",
                "x x x x x x x",
                "x           x",
                "xxx x x x x x",
                "x          xx",
                "xxxxxxxxxxxxx",
                "             "
            ]
            # Mapa2

            mapa2 = [
                
                "xxxxxxxxxxxxx",
                "xx          x",
                "x x x x x x x",
                "x    x      x",
                "x x x   x x x",
                "x   x       x",
                "xx   x x  x x",
                "x   x   x  xx",
                "xxxxxxxxxxxxx",
                "             "
            ]
            # Mapa1
            mapa3 = [
                
                "xxxxxxxxxxxxx",
                "xx          x",
                "x x x x   x x",
                "x    x      x",
                "x x x   x x x",
                "x   x       x",
                "x x    x  x x",
                "xx  x   x  xx",
                "xxxxxxxxxxxxx",
                "             "
            ]



            # Función para formatear el tiempo en minutos y segundos
            def formatear_tiempo(tiempo):
                minutos = int(tiempo // 60)
                segundos = int(tiempo % 60)
                return f"{minutos:02}:{segundos:02}"
            # Función para dibujar la barra de información con el tiempo formateado
            def dibujar_barra_informacion(superficie, vidas, puntos, llaves, tiempo, x_vida_inicial=20, y_vida=ALTO - 40, espacio_entre_elementos=40):
                # Caso base: si no quedan vidas, terminar la recursión
                if vidas <= 0:
                    # Dibujar el fondo de la barra de información al final de la recursión
                    pygame.draw.rect(superficie, BLANCO, (0, ALTO - 50, ANCHO, 50))
                    # Dibujar el contador de puntos
                    fuente = pygame.font.SysFont(None, 30)
                    texto_puntos = fuente.render("Puntos: " + str(puntos), True, NEGRO)
                    superficie.blit(texto_puntos, (ANCHO - 150, ALTO - 40))
                    # Dibujar el contador de llaves
                    texto_llaves = fuente.render("Llaves: " + str(llaves), True, NEGRO)
                    superficie.blit(texto_llaves, (ANCHO - 280, ALTO - 40))
                    # Dibujar el cronómetro formateado
                    texto_tiempo = fuente.render("Tiempo: " + formatear_tiempo(tiempo), True, NEGRO)
                    superficie.blit(texto_tiempo, (450, ALTO - 40))
                    return
                else:
                    # Dibujar la barra blanca antes de dibujar los corazones y llaves
                    pygame.draw.rect(superficie, BLANCO, (0, ALTO - 50, ANCHO, 50))
                    # Llamar recursivamente para dibujar las vidas restantes
                    dibujar_barra_informacion(superficie, vidas - 1, puntos, llaves, tiempo, x_vida_inicial + espacio_entre_elementos + imagen_vida.get_width(), y_vida, espacio_entre_elementos)
                    # Dibujar una vida después de dibujar las vidas restantes
                    superficie.blit(imagen_vida, (x_vida_inicial, y_vida))



                # Escribir texto en la barra de información
                fuente = pygame.font.SysFont(None, 24)
                texto = ""
                texto_renderizado = fuente.render(texto, True, NEGRO)
                superficie.blit(texto_renderizado, (20, ALTO - 40))


            # Función para construir el mapa recursivamente
            def construir_mapa(mapa, ancho_muro, alto_muro, x=0, y=0):
                # Obtener las dimensiones del mapa
                TAMANO_MAPA_Y = len(mapa)

                # Caso base: si hemos alcanzado el final del mapa, retornar una lista vacía de muros y colisiones
                if y >= TAMANO_MAPA_Y:
                    return [], []

                # Caso recursivo: explorar la siguiente fila del mapa
                muros_fila, colisiones_fila = construir_mapa(mapa, ancho_muro, alto_muro, 0, y + 1)

                # Lista para almacenar los muros y colisiones de esta fila
                muros = []
                colisiones = []

                # Iterar sobre cada columna en la fila actual
                for x_actual, caracter in enumerate(mapa[y]):
                    # Calcular las coordenadas x e y del muro actual
                    x_actual *= ancho_muro
                    x_actual += x
                    y_actual = y * alto_muro

                    if caracter == "x":
                        # Crear un rectángulo para representar el muro
                        rect_muro = pygame.Rect(x_actual, y_actual, ancho_muro, alto_muro)
                        muros.append(rect_muro)
                        # Crear un rectángulo de colisión para el muro (ligeramente más pequeño para evitar superposiciones)
                        rect_colision = pygame.Rect(x_actual + 2, y_actual + 2, ancho_muro - 4, alto_muro - 4)
                        colisiones.append(rect_colision)

                # Combinar los muros y colisiones de esta fila con los de las filas anteriores
                muros.extend(muros_fila)
                colisiones.extend(colisiones_fila)

                return muros, colisiones

            def dibujar_muros(superficie, muros):
                if not muros:  # Caso base: si la lista de muros está vacía, detener la recursión
                    return
                
                # Obtener el primer muro de la lista
                primer_muro = muros[0]
                
                # Dibujar la imagen de muro en la superficie
                superficie.blit(imagen_muro, (primer_muro.x, primer_muro.y))
                
                # Llamar recursivamente a la función con el resto de la lista de muros
                dibujar_muros(superficie, muros[1:])






            def explosion(posicion, rango, muros, cajas, personaje, corazones):
                alcance = [(0, 0)]  # La propia posición de la bomba
                
                muros_a_eliminar = []
                cajas_a_eliminar = []
                jugador_alcanzado = False  # Bandera para verificar si el jugador fue alcanzado por la explosión
                
                # Verificar si la explosión alcanza al personaje
                for x, y in alcance:
                    if personaje.colliderect(pygame.Rect(x * ANCHO_MURO, y * ALTO_MURO, ANCHO_MURO, ALTO_MURO)):
                        jugador_alcanzado = True  # El jugador fue alcanzado por la explosión
                        break
                
                for direccion in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    for i in range(1, rango + 1):
                        nueva_posicion = (posicion[0] + direccion[0] * i, posicion[1] + direccion[1] * i)
                        alcance.append(nueva_posicion)
                        # Romper la explosión si se encuentra un muro
                        for muro in muros:
                            if muro.collidepoint(nueva_posicion):
                                muros_a_eliminar.append(muro)
                                break
                        else:
                            # Romper la explosión si se encuentra una caja
                            for caja in cajas:
                                if caja.collidepoint(nueva_posicion):
                                    cajas_a_eliminar.append(caja)
                                    break
                            continue
                        break
                # Eliminar los muros alcanzados por la explosión
                for muro in muros_a_eliminar:
                    muros.remove(muro)
                # Eliminar las cajas alcanzadas por la explosión
                for caja in cajas_a_eliminar:
                    cajas.remove(caja)
                return alcance, jugador_alcanzado





            #al detectar una colicion no deja que el npc se mueva 
            #cuando lo hay colicion lo deja avanzar a la siguiente posicion 
            def move_colisiones(personaje, dx, dy, colisiones, cajas, indice=0):
                if indice == len(colisiones):
                    # Si no hay más objetos para verificar colisión, devolver la nueva posición
                    return personaje.move(dx, dy)
                
                obj = colisiones[indice]
                nueva_posicion = personaje.move(dx, dy)
                
                # Verificar colisión con las cajas
                for caja in cajas:
                    if nueva_posicion.colliderect(caja):
                        # Si hay colisión con una caja, no mover al personaje
                        return personaje
                
                if nueva_posicion.colliderect(obj):
                    # Si hay colisión con un objeto, no mover al personaje
                    return personaje
                
                # Llamar recursivamente para verificar la siguiente colisión
                return move_colisiones(personaje, dx, dy, colisiones, cajas, indice + 1)

            # Función para mover recursivamente al enemigo
            def mover_enemigo(x, y, destino_x, destino_y, cajas):
                # Caso base: si el enemigo ha alcanzado las coordenadas de destino, retornar las coordenadas actuales
                if x == destino_x and y == destino_y:
                    return x, y

                # Calcular la dirección del movimiento en x e y
                if destino_x > x:
                    nueva_x = min(x + velocidad_x, destino_x)
                elif destino_x < x:
                    nueva_x = max(x - velocidad_x, destino_x)
                else:
                    nueva_x = x

                if destino_y > y:
                    nueva_y = min(y + velocidad_y, destino_y)
                elif destino_y < y:
                    nueva_y = max(y - velocidad_y, destino_y)
                else:
                    nueva_y = y

                # Verificar si hay colisión con las cajas
                for caja in cajas:
                    if pygame.Rect(nueva_x, nueva_y, e_ancho, e_alto).colliderect(caja):
                        # Si hay colisión con una caja, no mover al enemigo
                        return x, y
                
                # Llamar recursivamente a la función mover_enemigo() con las nuevas coordenadas
                return mover_enemigo(nueva_x, nueva_y, destino_x, destino_y, cajas)

            def verificar_colision_jugador_enemigo(jugador_rect, enemigo_x, enemigo_y):
                return jugador_rect.colliderect(pygame.Rect(enemigo_x, enemigo_y, e_ancho, e_alto))




            def dibujar_estrellas(superficie, estrellas_posiciones):
                for pos_estrella_x, pos_estrella_y in estrellas_posiciones:
                    superficie.blit(imagen_estrella, (pos_estrella_x, pos_estrella_y))
                    superficie.blit(imagen_estrella2, (pos_estrella_x, pos_estrella_y))  # Dibujar la segunda estrella en la misma posición
            # Función recursiva para detectar colisiones con las estrellas en diferentes posiciones
            def detectar_colisiones_estrella(personaje_rect, estrellas_posiciones, puntos):
                # Variable para verificar si se detectó una colisión con una estrella
                colision_estrella = False
                
                # Función interna para detectar colisiones
                def detectar_colisiones_recursiva(estrellas_posiciones, puntos, colision_estrella):
                    if not estrellas_posiciones:
                        # Si no quedan estrellas, devolver los puntos actualizados y la lista de posiciones de estrellas
                        return puntos, [], colision_estrella
                    
                    # Extraer la posición de la primera estrella en la lista
                    pos_estrella_x, pos_estrella_y = estrellas_posiciones[0]
                    
                    # Verificar colisión entre el personaje y la estrella
                    if personaje_rect.colliderect(pygame.Rect(pos_estrella_x, pos_estrella_y, ANCHO_MURO, ALTO_MURO)):
                        # Aumentar 100 puntos si hay colisión
                        puntos += 100
                        # Eliminar la posición de la estrella de la lista
                        estrellas_posiciones.pop(0)
                        colision_estrella = True
                        
                        # Hacer la estrella transparente
                        hacer_estrella_transparente()
                        
                        # Llamar recursivamente a la función con la lista actualizada de estrellas
                        return detectar_colisiones_recursiva(estrellas_posiciones, puntos, colision_estrella)
                    
                    else:
                        # Si no hay colisión, llamar recursivamente a la función con la lista restante de estrellas
                        puntos, estrellas_posiciones, colision_estrella = detectar_colisiones_recursiva(estrellas_posiciones[1:], puntos, colision_estrella)
                        return puntos, [(pos_estrella_x, pos_estrella_y)] + estrellas_posiciones, colision_estrella
                
                # Llamar a la función interna para iniciar la detección de colisiones
                return detectar_colisiones_recursiva(estrellas_posiciones, puntos, colision_estrella)
            # Después de obtener los puntos necesarios
            def hacer_estrella_transparente():
                # Cargar la imagen de la estrella con transparencia alfa
                imagen_estrella_transparente = pygame.image.load("mapas/estre.jpg").convert_alpha()
                
                # Ajustar el valor alfa de los píxeles de la imagen para hacerla más transparente
                # Por ejemplo, reducir el valor alfa a la mitad (0 sería completamente transparente, 255 sería opaco)
                factor_transparencia = 2  # Por ejemplo, reducir a la mitad la transparencia original
                imagen_estrella_transparente.set_alpha(factor_transparencia)
                
                # Devolver la imagen de la estrella transparente
                return imagen_estrella_transparente





            def dibujar_llaves(superficie, llaves_posiciones):
                for pos_llave_x, pos_llave_y in llaves_posiciones:
                    superficie.blit(imagen_llave, (pos_llave_x, pos_llave_y))
                    superficie.blit(imagen_llave2, (pos_llave_x, pos_llave_y))
                    superficie.blit(imagen_llave3, (pos_llave_x, pos_llave_y))        
            # Función recursiva para detectar colisiones con las llaves en diferentes posiciones
            def detectar_colisiones_llave(personaje_rect, llaves_posiciones, puntos):
                # Variable para verificar si se detectó una colisión con una llave
                colision_llave = False
                
                # Función interna para detectar colisiones
                def detectar_colisiones_recursiva(llaves_posiciones, puntos, colision_llave):
                    if not llaves_posiciones:
                        # Si no quedan llaves, devolver los puntos actualizados y la lista de posiciones de llaves
                        return puntos, [], colision_llave
                    
                    # Extraer la posición de la primera llave en la lista
                    pos_llave_x, pos_llave_y = llaves_posiciones[0]
                    
                    # Verificar colisión entre el personaje y la llave
                    if personaje_rect.colliderect(pygame.Rect(pos_llave_x, pos_llave_y, ANCHO_MURO, ALTO_MURO)):
                        # Aumentar 100 puntos si hay colisión
                        puntos += 250
                        # Eliminar la posición de la llave de la lista
                        llaves_posiciones.pop(0)
                        colision_llave = True
                        
                        # Hacer la llave transparente
                        hacer_llave_transparente()
                        
                        # Llamar recursivamente a la función con la lista actualizada de llaves
                        return detectar_colisiones_recursiva(llaves_posiciones, puntos, colision_llave)
                    
                    else:
                        # Si no hay colisión, llamar recursivamente a la función con la lista restante de llaves
                        puntos, llaves_posiciones, colision_llave = detectar_colisiones_recursiva(llaves_posiciones[1:], puntos, colision_llave)
                        return puntos, [(pos_llave_x, pos_llave_y)] + llaves_posiciones, colision_llave
                
                # Llamar a la función interna para iniciar la detección de colisiones
                return detectar_colisiones_recursiva(llaves_posiciones, puntos, colision_llave)
            # Después de obtener los puntos necesarios
            def hacer_llave_transparente():
                # Cargar la imagen de la llave con transparencia alfa
                imagen_llave_transparente = pygame.image.load("mapas/llave.jpg").convert_alpha()
                
                # Ajustar el valor alfa de los píxeles de la imagen para hacerla más transparente
                # Por ejemplo, reducir el valor alfa a la mitad (0 sería completamente transparente, 255 sería opaco)
                factor_transparencia = 2  # Por ejemplo, reducir a la mitad la transparencia original
                imagen_llave_transparente.set_alpha(factor_transparencia)
                
                # Devolver la imagen de la llave transparente
                return imagen_llave_transparente




            def colocar_bomba(bombas, personaje_x, personaje_y, bombas_colocadas, MAX_BOMBAS):
                # Función auxiliar para verificar si una bomba está en una posición
                def bomba_en_posicion(x, y):
                    for bomba, _ in bombas:
                        if bomba.colliderect(pygame.Rect(x, y, 20, 20)):
                            return True
                    return False

                # Verificar si hay espacio para colocar la bomba
                if bombas_colocadas >= MAX_BOMBAS:
                    return bombas, bombas_colocadas

                # Verificar si la posición para colocar la bomba está ocupada por otra bomba
                if bomba_en_posicion(personaje_x, personaje_y):
                    return bombas, bombas_colocadas

                # Si la posición no está ocupada, colocar la bomba
                bomba = pygame.Rect(personaje_x, personaje_y, 20, 20)
                bombas.append((bomba, time.time()))
                bombas_colocadas += 1

                return bombas, bombas_colocadas


            def verificar_explosion(bombas, personaje_rect, corazones):
                for bomba, _ in bombas:
                    # Verificar si la explosión alcanza al personaje
                    if bomba.colliderect(personaje_rect):
                        if len(corazones) > 0:
                            # Si hay corazones disponibles, eliminar uno
                            corazones.pop()
                        return True  # Indicar que hubo una explosión que alcanzó al personaje
                # Llamar recursivamente a la función con las bombas restantes y el mismo personaje
                if bombas:
                    return verificar_explosion(bombas[:-1], personaje_rect, corazones)
                return False  # Indicar que no hubo explosión que alcanzó al personaje



            def dibujar_puertas_subterraneas(superficie, puertas_posiciones):
                for pos_puerta_x, pos_puerta_y in puertas_posiciones:
                    superficie.blit(imagen_puerta_subterranea, (pos_puerta_x, pos_puerta_y))
            # Función recursiva para detectar colisiones con las puertas subterráneas en diferentes posiciones
            def detectar_colisiones_puerta_subterranea(personaje_rect, puertas_posiciones, puntos):
                # Variable para verificar si se detectó una colisión con una puerta subterránea
                colision_puerta_subterranea = False
                
                # Función interna para detectar colisiones
                def detectar_colisiones_recursiva(puertas_posiciones, puntos, colision_puerta_subterranea):
                    if not puertas_posiciones:
                        # Si no quedan puertas subterráneas, devolver los puntos actualizados y la lista de posiciones de puertas subterráneas
                        return puntos, [], colision_puerta_subterranea
                    
                    # Extraer la posición de la primera puerta subterránea en la lista
                    pos_puerta_x, pos_puerta_y = puertas_posiciones[0]
                    
                    # Verificar colisión entre el personaje y la puerta subterránea
                    if personaje_rect.colliderect(pygame.Rect(pos_puerta_x, pos_puerta_y, 55, 55)):
                        # Aumentar puntos si hay colisión
                        puntos += 500
                        # Eliminar la posición de la puerta subterránea de la lista
                        puertas_posiciones.pop(0)
                        colision_puerta_subterranea = True
                        
                        # Abrir la puerta subterránea
                        abrir_puerta_subterranea()
                        
                        # Llamar recursivamente a la función con la lista actualizada de puertas subterráneas
                        return detectar_colisiones_recursiva(puertas_posiciones, puntos, colision_puerta_subterranea)
                    
                    else:
                        # Si no hay colisión, llamar recursivamente a la función con la lista restante de puertas subterráneas
                        puntos, puertas_posiciones, colision_puerta_subterranea = detectar_colisiones_recursiva(puertas_posiciones[1:], puntos, colision_puerta_subterranea)
                        return puntos, [(pos_puerta_x, pos_puerta_y)] + puertas_posiciones, colision_puerta_subterranea
                
                # Llamar a la función interna para iniciar la detección de colisiones
                return detectar_colisiones_recursiva(puertas_posiciones, puntos, colision_puerta_subterranea)
            # Después de obtener los puntos necesarios
            def abrir_puerta_subterranea():
                # Cargar la imagen de la puerta subterránea abierta
                imagen_puerta_subterranea_abierta = pygame.image.load("mapas/puerta_subterranea.png").convert_alpha()
                
                # Ajustar el valor alfa de los píxeles de la imagen para hacerla visible
                # Por ejemplo, establecer el valor alfa a 255 para que sea completamente opaca
                factor_visibilidad = 5  # Por ejemplo, establecer la visibilidad al máximo
                imagen_puerta_subterranea_abierta.set_alpha(factor_visibilidad)
                
                # Devolver la imagen de la puerta subterránea abierta
                return imagen_puerta_subterranea_abierta






            # Ventana
            ventana = pygame.display.set_mode((ANCHO, ALTO))
            pygame.display.set_caption("BOMBERMAN")

            # Cargar imagen de la vida
            imagen_vida = pygame.image.load("mapas/cora.jpg").convert_alpha()
            imagen_vida = pygame.transform.scale(imagen_vida, (30, 30))
            # Cargar imagen de la llave
            imagen_llave = pygame.image.load("mapas/llave.jpg").convert_alpha()
            imagen_llave = pygame.transform.scale(imagen_llave, (30, 30))
            imagen_llave2 = pygame.image.load("mapas/llave.jpg").convert_alpha()
            imagen_llave2 = pygame.transform.scale(imagen_llave2, (30, 30))
            imagen_llave3 = pygame.image.load("mapas/llave.jpg").convert_alpha()
            imagen_llave3 = pygame.transform.scale(imagen_llave3, (30, 30))
            # Cargar imagen de la estrella
            imagen_estrella = pygame.image.load("mapas/estre.jpg").convert_alpha()
            imagen_estrella = pygame.transform.scale(imagen_estrella, (ANCHO_MURO, ALTO_MURO))
            imagen_estrella2 = pygame.image.load("mapas/estre.jpg").convert_alpha()
            imagen_estrella2 = pygame.transform.scale(imagen_estrella2, (ANCHO_MURO, ALTO_MURO))

            # Datos de los muros 
            ancho_muro = ANCHO // len(mapa[0])
            alto_muro = ALTO // len(mapa)
            muros, colisiones = construir_mapa(mapa, ancho_muro, alto_muro)

            # Cargar imagen del muro
            imagen_muro = pygame.image.load("mapas/block.png").convert_alpha()
            imagen_muro = pygame.transform.scale(imagen_muro, (ancho_muro, alto_muro))

            # Cargar imagen de la bomba
            imagen_bomba = pygame.image.load("mapas/boom.jpg").convert_alpha()
            imagen_bomba = pygame.transform.scale(imagen_bomba, (35, 35))

            # Cargar imagen de la puerta subterranea
            puerta_subterranea = pygame.image.load("mapas/puerta_subterranea.png")
            imagen_puerta_subterranea = pygame.transform.scale(puerta_subterranea, (55, 55))  # para escalar la imagen 
            puerta_subterranea2 = pygame.image.load("mapas/puerta_subterranea.png")
            imagen_puerta_subterranea2 = pygame.transform.scale(puerta_subterranea2, (55, 55))  # para escalar la imagen 
            imagen_puerta_subterranea3 = pygame.image.load("mapas/puerta_subterranea.png")
            imagen_puerta_subterranea3 = pygame.transform.scale(imagen_puerta_subterranea3, (55, 55))  # para escalar la imagen 

            # Coordenadas donde se colocará la imagen
            x_puerta_subterranea = 765
            y_puerta_subterranea = 85
            x_puerta_subterranea2 = 284
            y_puerta_subterranea2 = 430

            # Cargar imagen de la caja
            caja = pygame.image.load("mapas/caja.jpg")
            imagen_caja = pygame.transform.scale(caja, (55, 55))  # para escalar la imagen 
            # Coordenadas donde se colocará la imagen
            x_caja = 690
            y_caja = 85



            # Cargar imagen de fondo
            imagen_fondo = pygame.image.load("mapas/fondo_mapa.jpg").convert()  
            imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO, ALTO))

            # Cargar imágenes del personaje para cada dirección
            personaje_arriba = pygame.image.load("proyecto/personaje3/arriba.png").convert_alpha()
            personaje_abajo = pygame.image.load("proyecto/personaje3/abajo.png").convert_alpha()
            personaje_izquierda = pygame.image.load("proyecto/personaje3/izquierda.png").convert_alpha()
            personaje_derecha = pygame.image.load("proyecto/personaje3/derecha.png").convert_alpha()

            # Definir la velocidad de movimiento del personaje
            PLAYER_SPEED = 2.6

            # Crear un diccionario para asociar la dirección con la imagen correspondiente
            direccion_imagen = {
                "izquierda": personaje_izquierda,
                "derecha": personaje_derecha,
                "arriba": personaje_arriba,
                "abajo": personaje_abajo
            }

            # Personaje
            personaje = pygame.Rect(80, 520, 40, 40)
            direccion_personaje = "derecha"

            #----LISTAS----
            #bombas
            bombas = []
            #Explosiones
            explosiones = []
            # Definir la cantidad máxima de bombas que el jugador puede colocar
            MAX_BOMBAS = 6
            # Contador para rastrear cuántas bombas ha colocado el jugador
            bombas_colocadas = 0
            #vidas del jugador 
            vidas = 4 
            corazones = [1, 2, 3]  # Ejemplo de inicialización de la lista de corazones


            # Coordenadas donde se colocarán las cajas
            cajas_posiciones = [
                (80, 145),  # Ejemplo de posición para la primera caja
                (213, 360),  # Ejemplo de posición para la segunda caja
                (353, 220),
                (695, 500),
                (630, 85),
            ]

            # Lista para almacenar los rectángulos de las cajas
            cajas_rect = []

            # Crear rectángulos para cada posición de caja y agregarlos a la lista
            for posicion in cajas_posiciones:
                caja_rect = pygame.Rect(posicion[0], posicion[1], 55, 55)  # Rectángulo con las mismas dimensiones que las cajas
                cajas_rect.append(caja_rect)

            # Lista de posiciones de estrellas en el mapa
            estrellas_posiciones = [
                (80, 80),
                (769,500)
            ]
            llave_posicion = [
                (170, 372),
                (432, 297),
                (570, 160),

            ]
            puertas_posiciones = [(765, 85), (284, 430), (75, 430)]



            #-----------------enemigo--------------------------
            e_alto=35
            e_ancho=30
            i_enemigo1 = pygame.image.load("mapas/Goblin1.jpg").convert()  
            i_enemigo1 = pygame.transform.scale(i_enemigo1, (e_ancho, e_alto))
            # Posición inicial del enemigo
            enemigo_x, enemigo_y = 775, 200
            # Posición a la que queremos mover al enemigo
            destino_x, destino_y = 775, 400
            # Velocidad del enemigo
            velocidad_x = 1
            velocidad_y = 1
            # Puntos de destino del enemigo 
            punto_destino1 = (775, 400)
            punto_destino2 = (775, 200)
            # Variable para rastrear el punto actual hacia el que se mueve el enemigo
            punto_destino_actual = punto_destino1


            #-----------------enemigo2--------------------------
            e_alto = 35
            e_ancho = 30
            i_enemigo2 = pygame.image.load("mapas/Goblin1.jpg").convert()  
            i_enemigo2 = pygame.transform.scale(i_enemigo2, (e_ancho, e_alto))
            # Posición inicial del enemigo2
            enemigo2_x, enemigo2_y = 150, 90
            # Posición a la que queremos mover al enemigo2
            destino2_x, destino2_y = 570, 90
            # Velocidad del enemigo2
            velocidad2_x = 1
            velocidad2_y = 1
            # Puntos de destino del enemigo2 
            punto_destino2_1 = (570, 90)
            punto_destino2_2 = (150, 90)
            # Variable para rastrear el punto actual hacia el que se mueve el enemigo2
            punto_destino_actual2 = punto_destino2_1



            # Bucle principal
            jugando = True
            while jugando:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        jugando = False
                    # Obtener las teclas presionadas
                keys = pygame.key.get_pressed()
                dx, dy = 0, 0
                

                if keys[pygame.K_a]:
                    dx = -PLAYER_SPEED
                    direccion_personaje = "izquierda"
                if keys[pygame.K_d]:
                    dx = PLAYER_SPEED
                    direccion_personaje = "derecha"
                if keys[pygame.K_w]:
                    dy = -PLAYER_SPEED
                    direccion_personaje = "arriba"
                if keys[pygame.K_s]:
                    dy = PLAYER_SPEED
                    direccion_personaje = "abajo"
                # Colocar una bomba si se presiona la tecla de espacio y el jugador tiene bombas disponibles
                if keys[pygame.K_SPACE] and len(bombas) < MAX_BOMBAS:
                    # Llamar a la función recursiva para verificar y colocar la bomba
                    bombas, bombas_colocadas = colocar_bomba(bombas, personaje.x, personaje.y, bombas_colocadas, MAX_BOMBAS)

                # Llamar a la función para restablecer los elementos
                #restablecer_elementos()

                for bomba, tiempo in bombas:
                    if time.time() - tiempo > 2:  # Tiempo de detonación de la bomba (2 segundos)
                        # Llamada a la función de explosión
                        alcance_explosion, jugador_alcanzado = explosion((bomba.centerx, bomba.centery), 3, muros, cajas_rect, personaje, corazones)
                        if jugador_alcanzado:
                            # Si el jugador fue alcanzado por la explosión, resta un corazón
                            if len(corazones) > 0:
                                corazones.pop()
                        bombas.remove((bomba, tiempo))

                # Mover al personaje con colisiones
                nueva_posicion = move_colisiones(personaje, dx, dy, colisiones, cajas_rect)


                
                # Verificar si hay colisión con los muros o las cajas
                colision_muro = False
                colision_caja = False
                for muro in muros:
                    if nueva_posicion.colliderect(muro):
                        colision_muro = True
                        break
                for caja in cajas_rect:
                    if nueva_posicion.colliderect(caja):
                        colision_caja = True
                        break

                # Actualizar la posición del personaje solo si no hay colisión con un muro o una caja
                if nueva_posicion != personaje and not colision_muro and not colision_caja:
                    personaje = nueva_posicion




                    
                # Calcular la diferencia entre las coordenadas del enemigo y el punto de destino actual
                dx = punto_destino_actual[0] - enemigo_x
                dy = punto_destino_actual[1] - enemigo_y

                # Normalizar la dirección para que el enemigo se mueva a una velocidad constante
                norm = (dx ** 2 + dy ** 2) ** 0.5
                if norm != 0:
                    dx = dx / norm * velocidad_x
                    dy = dy / norm * velocidad_y

                # Mover al enemigo hacia el punto de destino actual
                enemigo_x += dx
                enemigo_y += dy

                def verificar_destino(enemigo_x, enemigo_y, punto_destino_actual, punto_destino1, punto_destino2):
                    # Verificar si el enemigo ha llegado al punto de destino actual
                    if abs(enemigo_x - punto_destino_actual[0]) < 5 and abs(enemigo_y - punto_destino_actual[1]) < 5:
                        # Cambiar al siguiente punto de destino
                        if punto_destino_actual == punto_destino1:
                            return punto_destino2
                        else:
                            return punto_destino1
                    else:
                        return punto_destino_actual
                # Llamar a la función recursiva para verificar y cambiar el punto de destino actual
                punto_destino_actual = verificar_destino(enemigo_x, enemigo_y, punto_destino_actual, punto_destino1, punto_destino2)

                # Calcular la diferencia entre las coordenadas del enemigo 2 y el punto de destino actual
                dx2 = punto_destino_actual2[0] - enemigo2_x
                dy2 = punto_destino_actual2[1] - enemigo2_y

                # Normalizar la dirección para que el enemigo 2 se mueva a una velocidad constante
                norm2 = (dx2 ** 2 + dy2 ** 2) ** 0.5
                if norm2 != 0:
                    dx2 = dx2 / norm2 * velocidad2_x
                    dy2 = dy2 / norm2 * velocidad2_y

                # Mover al enemigo 2 hacia el punto de destino actual
                enemigo2_x += dx2
                enemigo2_y += dy2

                def verificar_destino(enemigo2_x, enemigo2_y, punto_destino_actual2, punto_destino2_1, punto_destino2_2):
                    # Verificar si el enemigo ha llegado al punto de destino actual
                    if abs(enemigo2_x - punto_destino_actual2[0]) < 5 and abs(enemigo2_y - punto_destino_actual2[1]) < 5:
                        # Cambiar al siguiente punto de destino
                        if punto_destino_actual2 == punto_destino2_1:
                            return punto_destino2_2
                        else:
                            return punto_destino2_1
                    else:
                        return punto_destino_actual2
                # Llamar a la función recursiva para verificar y cambiar el punto de destino actual del enemigo 2
                punto_destino_actual2 = verificar_destino(enemigo2_x, enemigo2_y, punto_destino_actual2, punto_destino2_1, punto_destino2_2)



                # Llamar a la función recursiva para detectar colisiones con las estrellas y actualizar los puntos, la lista de posiciones de estrellas y la bandera de colisión con la estrella
                puntos, estrellas_posiciones, colision_estrella = detectar_colisiones_estrella(personaje, estrellas_posiciones, puntos)
                # Llamar a la función recursiva para detectar colisiones con las estrellas y actualizar los puntos, la lista de posiciones de estrellas y la bandera de colisión con la estrella
            

                # Verificar si el enemigo y el jugador están en la misma posición
                if verificar_colision_jugador_enemigo(personaje, enemigo_x, enemigo_y):
                    # Reducir el contador de vidas del jugador en uno
                    vidas -= 1
                    # Reiniciar la posición del enemigo
                    enemigo_x, enemigo_y = 775, 200
                    
                puntos, llave_posicion, colision_llave = detectar_colisiones_llave(personaje, llave_posicion, puntos)
                if colision_llave:
                    llaves += 1

                # Dibujar puertas subterráneas en la superficie
                dibujar_puertas_subterraneas(ventana, puertas_posiciones)
                
                # Detectar colisiones con las puertas subterráneas
                puntos, puertas_posiciones, colision_puerta_subterranea = detectar_colisiones_puerta_subterranea(personaje, puertas_posiciones, puntos)
                

                # Dibujar los elementos del juego
                ventana.blit(imagen_fondo, (0, 0))
                dibujar_estrellas(ventana, estrellas_posiciones)
                if colision_estrella:
                # Hacer la estrella transparente
                    imagen_estrella = hacer_estrella_transparente()
                dibujar_llaves(ventana, llave_posicion)
                if colision_llave:
                # Hacer la estrella transparente
                    imagen_llave = hacer_llave_transparente()

                ventana.blit(i_enemigo1, (enemigo_x, enemigo_y))
                ventana.blit(i_enemigo2, (enemigo2_x, enemigo2_y))
                dibujar_puertas_subterraneas(ventana, puertas_posiciones)
                ventana.blit(imagen_estrella, (80, 80))
                ventana.blit(imagen_llave, (170, 372))
                # Dibujar las cajas en el mapa
                for posicion in cajas_posiciones:
                    ventana.blit(imagen_caja, posicion)
                dibujar_muros(ventana, muros)
                for bomba in bombas:
                    ventana.blit(imagen_bomba, bomba[0])
                    
                
                if personaje.colliderect(pygame.Rect(x_puerta_subterranea, y_puerta_subterranea, 55, 55)):
                    # Verificar si el contador de llaves es igual a 1
                    if llaves == 1:
                        # Cambiar al mapa2
                        mapa = mapa2

                        # Recalcular los muros y colisiones para el nuevo mapa
                        muros, colisiones = construir_mapa(mapa, ancho_muro, alto_muro)
                if personaje.colliderect(pygame.Rect(x_puerta_subterranea2, y_puerta_subterranea2, 55, 55)):
                    # Verificar si el contador de llaves es igual a 1
                    if llaves == 2:
                        # Cambiar al mapa2
                        mapa2 = mapa3

                        # Recalcular los muros y colisiones para el nuevo mapa
                        muros, colisiones = construir_mapa(mapa3, ancho_muro, alto_muro)
                

                ventana.blit(direccion_imagen[direccion_personaje], personaje)

                # Dibujar la barra de información
                tiempo = time.time() - tiempo_inicial
                dibujar_barra_informacion(ventana, vidas, puntos, llaves, tiempo)
                
                
                # Detectar colisiones con la puerta subterránea 3
                if personaje.colliderect(pygame.Rect(75, 430, 55, 55)):
                # Verificar si el contador de llaves es igual a 3
                    if llaves == 3:
                        # Crear la ventana emergente
                        ventana_emergente = pygame.display.set_mode((400, 200))
                        pygame.display.set_caption("¡Ganaste!")
                        
                        WHITE = (255, 255, 255)
                        GRAY = (200, 200, 200)
                        BLACK = (0, 0, 0)
                        
                        def create_button(text, fuente, color, hover_color, surface, x, y, width, height, action=None):
                            mouse_pos = pygame.mouse.get_pos()
                            click = pygame.mouse.get_pressed()

                            if x < mouse_pos[0] < x + width and y < mouse_pos[1] < y + height:
                                pygame.draw.rect(surface, hover_color, (x, y, width, height))
                                if click[0] == 1 and action is not None:
                                    action()
                            else:
                                pygame.draw.rect(surface, color, (x, y, width, height))

                            draw_text(text, fuente, (0, 0, 0), surface, x + width // 2, y + height // 2)

                        def draw_text(text, fuente, color, surface, x, y):
                            text_obj = fuente.render(text, True, color)
                            text_rect = text_obj.get_rect()
                            text_rect.center = (x, y)
                            surface.blit(text_obj, text_rect)

                        # Bucle principal de la ventana emergente
                        # Coordenadas y dimensiones del botón para regresar a la ventana principal
                        boton_rect_regresar = pygame.Rect(150, 120, 100, 50)
                        # Fuente para el texto en la ventana emergente
                        fuente = pygame.font.Font(None, 36)

                        # Crear la superficie de texto
                        texto_ganaste = "¡Ganaste!"
                        color_texto = (0, 0, 0)  # Color del texto
                        texto_surface = fuente.render(texto_ganaste, True, color_texto)
                        # Bucle principal de la ventana emergente
                        ventana_emergente_abierta = True
                        while ventana_emergente_abierta:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    ventana_emergente_abierta = False
                                    # Salir del juego completamente
                                    pygame.quit()
                                    sys.exit()
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                    # Verificar si se hizo clic en el botón de regresar
                                    if boton_rect_regresar.collidepoint(event.pos):
                                        # Salir del bucle para cerrar la ventana emergente
                                        ventana_emergente_abierta = False

                            # Dibujar contenido de la ventana emergente
                            ventana_emergente.fill((255, 255, 255))  # Color de fondo blanco
                            # Agregar texto u otras imágenes aquí si lo deseas
                            create_button("Regresar", fuente, GRAY, BLACK, ventana_emergente, 150, 120, 100, 50, menu)
                            ventana_emergente.blit(texto_surface, (150 - texto_surface.get_width() // 2, 80))

                            # Actualizar la ventana emergente
                            pygame.display.flip()



                # Actualizar la ventana
                pygame.display.flip()

            # Salir del juego
            pygame.quit()
            pass

        def main_menu():
            screen = pygame.display.set_mode((ancho, alto))
            pygame.display.set_caption("Menú Principal")

            font = pygame.font.Font(None, 40)
            WHITE = (255, 255, 255)
            GRAY = (200, 200, 200)
            BLACK = (0, 0, 0)



            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                



                                
                                
                                
                fondo_per = pygame.image.load("mapas/finper.jpg").convert()  
                fondo_per = pygame.transform.scale(fondo_per, (ancho, alto))
                screen.blit(fondo_per, (0, 0))
                    
                



                create_button("personaje 1", font, GRAY, BLACK, screen, 128, 500, 200, 50, open_game_1)
                create_button("personaje 2", font, GRAY, BLACK, screen, 358, 500, 200, 50, open_game_2)
                create_button("personaje 3", font, GRAY, BLACK, screen, 584, 500,200, 50, open_game_3)

                pygame.display.update()

        main_menu()   



    def top(screen, texto_ingresado):  
        font = pygame.font.Font(None, 40)
        BLACK = (0, 0, 0)

        def main_menu():
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        
                fondo_top = pygame.image.load("mapas/foncon.jpg").convert()  
                fondo_top = pygame.transform.scale(fondo_top, (ancho, alto))
                screen.blit(fondo_top, (0, 0))
                draw_text(texto_ingresado, font, BLACK, screen, 400, 50)  # Aquí se usa texto_ingresado
                pygame.display.update()

        main_menu()

    def info():
        screen = pygame.display.set_mode((ancho, alto))
        pygame.display.set_caption("Menú Principal")
        def main_menu():
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                fondo_info = pygame.image.load("mapas/foninfo.jpg").convert()  
                fondo_info = pygame.transform.scale(fondo_info, (ancho, alto))
                screen.blit(fondo_info, (0, 0))
                pygame.display.update()
        main_menu()   

    def confi():
        screen = pygame.display.set_mode((ancho, alto))
        pygame.display.set_caption("Menú Principal")

        # Variable para rastrear si la música está silenciada
        muted = False

        def main_menu():
            nonlocal muted  # Declarar que muted es una variable no local

            jugando = True
            volumen = 0.5  # Volumen inicial

            while jugando:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        jugando = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:  # Botón izquierdo del mouse
                            mouseX, mouseY = pygame.mouse.get_pos()
                            if 300 <= mouseX <= 400 and 150 <= mouseY <= 200:
                                # Cambia el estado de la variable muted
                                muted = not muted
                                # Ajusta el volumen de la música
                                pygame.mixer.music.set_volume(0 if muted else volumen)
                            elif 50 <= mouseX <= 250 and 300 <= mouseY <= 320:
                                # Calcula el nuevo volumen en función de la posición del mouse
                                volumen = (mouseX - 50) / 200
                                # Ajusta el volumen de la música
                                pygame.mixer.music.set_volume(volumen)

                # Dibujar en la pantalla
                fondo_con = pygame.image.load("mapas/foncon.jpg").convert()  
                fondo_con = pygame.transform.scale(fondo_con, (ancho, alto))
                screen.blit(fondo_con, (0, 0))
                barra_x = (ancho - 200) // 2  
                dibujar_barra_volumen(screen, volumen, barra_x)  
                draw_volume_indicator(screen, volumen, barra_x) 
                if muted:
                    create_button("<x", font, GRAY, BLACK, screen, 300, 150, 100, 50)
                else:
                    create_button("<)))", font, GRAY, BLACK, screen, 300, 150, 100, 50)
                
                pygame.display.update()
    # En main_menu()
    

        def dibujar_barra_volumen(surface, volumen, x):
            pygame.draw.rect(surface, BLANCO, (50, 300, 200, 20))
            pygame.draw.rect(surface, AZUL, (50, 300, volumen * 200, 20))

        def draw_volume_indicator(surface, volumen, x):
            # Calcula la posición horizontal del rectángulo indicador
            indicator_pos = (50 + volumen * 200, 300)  # Ajusta la coordenada x según la barra
            # Dibuja el rectángulo indicador
            pygame.draw.rect(surface, NEGRO, (indicator_pos[0] - 5, indicator_pos[1], 4, 20))


        main_menu()

    def create_button(text, font, color, hover_color, surface, x, y, width, height, action=None):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse_pos[0] < x + width and y < mouse_pos[1] < y + height:
            pygame.draw.rect(surface, hover_color, (x, y, width, height))
            if click[0] == 1 and action is not None:
                action()
        else:
            pygame.draw.rect(surface, color, (x, y, width, height))

        draw_text(text, font, (0, 0, 0), surface, x + width // 2, y + height // 2)

    def draw_text(text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_obj, text_rect)

    pygame.init()

    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("bomberman")

    font = pygame.font.Font(None, 40)

    WHITE = (255, 255, 255)
    GRAY = (200, 200, 200)
    BLACK = (0, 0, 0)

    fondo_inicio = pygame.image.load("mapas/fonini.jpg").convert()  
    fondo_inicio = pygame.transform.scale(fondo_inicio, (ancho, alto))

    input_box = pygame.Rect(50, 50, 200, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    font_input = pygame.font.Font(None, 32)

    running = True
    volumen = 0.5  # Volumen inicial

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                        active = False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        # Dibujar la pantalla de inicio
        screen.blit(fondo_inicio, (0, 0))

        # Dibujar el cuadro de texto
        pygame.draw.rect(screen, color, input_box, 2)
        txt_surface = font_input.render(text, True, (0, 0, 0))
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        # Crear botones
        create_button("nombre", font, GRAY, BLACK, screen, 50, 10, 200, 32)
        create_button("enter", font, GRAY, BLACK, screen, 247, 50, 70, 32)
        create_button("jugar", font, GRAY, BLACK, screen, 50, 100, 200, 50, pantalla_personajes)
        create_button("top puntajes", font, GRAY, BLACK, screen, 50, 190, 200, 50, lambda: top(screen, text))
        create_button("informacion", font, GRAY, BLACK, screen, 50, 290, 200, 50, info)
        create_button("configuracion", font, GRAY, BLACK, screen, 50, 390, 200, 50, confi)


        # Actualizar la pantalla
        pygame.display.update()

    # Detener la música y cerrar Pygame al salir del juego
    pygame.mixer.music.stop()
    pygame.quit()
    sys.exit()
pass

def create_button(text, font, color, hover_color, surface, x, y, width, height, action=None):
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse_pos[0] < x + width and y < mouse_pos[1] < y + height:
        pygame.draw.rect(surface, hover_color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(surface, color, (x, y, width, height))

    draw_text(text, font, (0, 0, 0), surface, x + width // 2, y + height // 2)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pantalla Inicial")

font = pygame.font.Font(None, 40)

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

fondo_inicio = pygame.image.load("mapas/fon.jpg").convert()  
fondo_inicio = pygame.transform.scale(fondo_inicio, (ancho, alto))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dibujar los elementos del juego
    screen.blit(fondo_inicio, (0, 0))

    create_button("Iniciar", font, GRAY, BLACK, screen, 285, 400, 200, 50,menu)

    pygame.display.update()

pygame.quit()
sys.exit()