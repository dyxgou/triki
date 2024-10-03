"""
Este módulo es la entrada principal para ejecutar un juego de Triki (Tic-Tac-Toe) utilizando Pygame. 
Se encarga de gestionar la interfaz gráfica, el tablero de juego, y los botones que interactúan con el usuario.

Las principales responsabilidades de este módulo son:
- Crear y gestionar las superficies gráficas.
- Manejar los eventos del mouse, como los clics en los botones.
- Dibujar y actualizar el tablero de Triki.

Clases y funciones importadas de otros módulos:
- Game: Maneja la lógica general del juego y la ventana principal.
- Button: Clase para crear botones interactivos.
- Board: Clase que gestiona el estado del tablero de Triki.
- render_board: Función que dibuja el tablero y las marcas (X u O).
- get_turn_surface: Función (no utilizada aquí) que muestra de quién es el turno.
"""

import pygame
from sys import exit
from pygame.event import Event
from game import Game
from components.button import Button
from settings import BUTTON_HEIGHT, BUTTON_WIDTH, PADDING
from utils.render_board import render_board
from utils.get_turn_surface import get_turn_surface
from utils import Board


def start_game():
    """
    Función principal que inicia el juego de Triki. 

    Descripción detallada de la función:
    - Inicializa la ventana de juego utilizando la clase Game.
    - Crea dos superficies principales:
        1. Superficie donde se dibuja el tablero (con 3x3 celdas).
        2. Superficie para los botones (como el botón de "Salir").
    - Cada una de estas superficies se ajusta con el tamaño apropiado y se posiciona en la ventana.
    - Renderiza el tablero utilizando la clase Board y la función render_board.
    - Asigna la funcionalidad del botón de "Salir", que permite cerrar el juego al hacer clic.
    - Define un manejador de eventos para detectar clics del mouse y verificar si estos ocurren sobre los botones.
    - Inicia el bucle principal del juego para mantener la ventana activa y manejar los eventos de interacción.

    Devuelve: 
    - Ningún valor (es una función de procedimiento que gestiona la interfaz gráfica y las interacciones).
    """
    
    # Instancia principal del juego con el título "Triki!"
    # Aquí se inicializa el objeto `game` que controla el flujo general del juego y la ventana principal.
    game = Game("Triki!")

    """
    Crear la superficie central que contendrá el tablero.
    
    Parámetros:
    - x: Ancho de la superficie, calculado como (ancho del botón * 3) + padding, para representar un tablero de 3 columnas.
    - y: Alto de la superficie, calculado de la misma manera que el ancho, representando 3 filas del tablero.

    Devuelve:
    - surface_center: Superficie central del tablero donde se dibujarán las marcas (X y O).
    - center_cors: Coordenadas centrales que permitirán posicionar esta superficie correctamente en la ventana.
    """
    surface_center, center_cors = game.create_center_surface(
        x=(BUTTON_WIDTH * 3) + PADDING * 2,  # Calculamos el ancho del tablero basado en el tamaño de los botones.
        y=(BUTTON_HEIGHT * 3) + PADDING * 2,  # El alto sigue el mismo cálculo, ya que el tablero es cuadrado.
    )

    """
    Crear la superficie donde se dibujarán los botones.

    - Esta superficie tiene el mismo ancho que la superficie del tablero, pero su altura es fija (200 píxeles).
    - Los botones se dibujarán en esta superficie separada del tablero, permitiendo una organización clara.

    Devuelve:
    - buttons_surface: La superficie específica para los botones del juego (como "Salir").
    - button_cors: Coordenadas para posicionar la superficie de botones en la ventana, alineada con el tablero.
    """
    buttons_surface = game.create_surface(surface_center.get_width(), y=200)
    button_cors = buttons_surface.get_rect(bottomleft=center_cors.topleft)

    """
    Crear el botón de salida.

    Este botón se ubica en la superficie de botones y está diseñado para permitir al jugador cerrar el juego.
    - Se define el tamaño y la posición del botón en la superficie de botones.
    - Luego, se añade texto al botón para que diga "¡Salir!", con una fuente de tamaño 16 y color amarillo.
    """
    quit_button = Button(button_cors.topleft)  # Crear el botón en la esquina superior izquierda de la superficie de botones.
    quit_button.insert_text("¡Salir!", 16, "yellow")  # Añadir el texto "Salir" al botón.

    def on_quit():
        """
        Función que se ejecuta cuando el jugador hace clic en el botón de salida.
        - Llama a `pygame.quit()` para finalizar todos los procesos de Pygame (cerrar la ventana).
        - Llama a `exit()` para detener el programa de manera segura y salir de la ejecución.
        """
        pygame.quit()  # Cerrar la ventana de juego.
        exit()  # Terminar el programa.

    # Asignar la función `on_quit` al botón de salida.
    quit_button.on_click = on_quit

    """
    Añadir el botón de salida a la superficie de botones.
    - El botón se centra horizontalmente en la superficie de botones, calculando las coordenadas necesarias para ello.
    """
    game.blit_button(
        buttons_surface,
        quit_button,
        x=(buttons_surface.get_width() // 2) - quit_button.surface.get_width() // 2,  # Centrando el botón.
        y=(buttons_surface.get_height() // 2) - quit_button.surface.get_height() // 2,  # Ajustando la posición verticalmente.
    )

    """
    Crear el tablero del juego.
    - La clase Board gestiona el estado del tablero, como las posiciones ocupadas por las X y O, y permite actualizarlo tras cada jugada.
    """
    board = Board()

    """
    Renderizar el tablero en la superficie central.
    - Se dibujan las celdas vacías y las marcas existentes (si las hay) en el tablero.
    """
    render_board(surface_center, center_cors, board, game)

    """
    Colocar la superficie del tablero y la de los botones en la ventana principal del juego.
    - Esto se hace mediante `blit_surface`, que se encarga de mostrar ambas superficies en la ventana del juego.
    """
    game.blit_surface(surface_center, center_cors)  # Dibuja el tablero en la ventana.
    game.blit_surface(buttons_surface, button_cors)  # Dibuja la superficie de botones en la ventana.

    def on_click(event: Event):
        """
        Función para manejar los eventos de clic del mouse.
        
        Esta función verifica si el jugador ha hecho clic en algún botón y, de ser así, ejecuta la acción correspondiente.
        
        Pasos detallados:
        - Se obtiene la posición actual del mouse cuando ocurre el clic.
        - Se recorre la lista de botones para verificar si el mouse está sobre alguno.
        - Si el clic ocurre sobre un botón, se ejecuta su función `click()` (en este caso, `on_quit` para el botón de salir).
        - Se actualiza el cursor del mouse según su posición: 
            - Si está sobre un botón, el cursor cambia a una mano (indicativo de un elemento interactivo).
            - Si no está sobre ningún botón, el cursor vuelve a su forma predeterminada.
        """
        mouse_pos = pygame.mouse.get_pos()  # Obtener la posición del mouse cuando ocurre el evento de clic.

        # Recorrer todos los botones del juego para verificar si el mouse está sobre alguno.
        for button in game.buttons:
            if button.is_hover(mouse_pos):  # Verificar si el mouse está sobre el área de algún botón.
                if event.type == pygame.MOUSEBUTTONDOWN:  # Si el evento detectado es un clic del mouse.
                    button.click()  # Ejecutar la acción asignada al botón (en este caso, salir del juego).
                    render_board(surface_center, center_cors, board, game)  # Renderizar de nuevo el tablero tras el clic.
                
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # Cambiar el cursor a una mano.
                break
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # Restaurar el cursor predeterminado si no hay botones debajo del mouse.

    # Asignar la función `on_click` para manejar los eventos de clic del mouse.
    game.on_click = on_click

    # Iniciar el bucle principal del juego.
    # Este bucle mantiene la ventana abierta y en funcionamiento, gestionando eventos como clics y movimientos del mouse.
    game.init()


if __name__ == "__main__":
    """
    Punto de entrada del programa. 
    - Si este archivo es ejecutado directamente, se llamará a `start_game()` para iniciar el juego.
    - Si es importado como un módulo, esta sección no se ejecutará.
    """
    start_game()
