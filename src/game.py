from typing import List, Optional
"""
Se usan los tipos List y Optional para las anotaciones de tipo.     
"""
import pygame
"""
La biblioteca principal para el manejo de gráficos, superficies y eventos en el juego. 
"""
from sys import exit
"""
exit: Para salir del programa. 
"""

from pygame.event import Event
from pygame.rect import RectType
from pygame.surface import SurfaceType
"""
pygame.event, pygame.rect, pygame.surface: Estos módulos de pygame permiten trabajar con eventos, rectángulos y superficies (imágenes en pantalla).
"""

from screen import Screen
from color import ColorValue
from components.button import Button
"""
screen, color, button: Se importan clases externas Screen, ColorValue, y Button de los otros archivos, estos son componentes personalizables del juego.
"""

class Game(Screen):
    """
    Define la clase Game, que hereda de la clase Screen 
    """
    __buttons: List[Button]
    """
    __buttons: Es una lista de botones (Button), usada para almacenar los botones que se añaden al juego.
    """
    def __init__(self, title: str) -> None:
        super().__init__(title)
        """
        El constructor recibe un título para la ventana y lo pasa a la clase Screen.
        """
        self.__buttons = []
        """
        Inicializa __buttons como una lista vacía para almacenar los botones. 
        """

    @property
    def buttons(self):
        return self.__buttons
        """
        Devuelve la lista de botones. 
        """

    def create_surface(
        self,
        x: int = 500,
        y: int = 500,
        alpha: bool = False,
        color: Optional[ColorValue] = None,
    ):
        new_surface = pygame.Surface((x, y), pygame.SRCALPHA, 32)
        """
        Crea una superficie de tamaño (x, y) usando pygame.Surface(). 
            x, y: Definen el tamaño de la superficie (ancho y alto, en píxeles).
            alpha: Si es True, la superficie admitirá transparencia.
            color: Si se proporciona un color, se llenará la superficie con él.
            pygame.Surface: Crea la superficie con dimensiones (x, y).
        """

        if alpha:
            new_surface = pygame.Surface.convert_alpha(new_surface)
            """
            Crea una superficie de tamaño (x, y) usando pygame.Surface(). 
            """
        elif color is not None:
            new_surface.fill(color)
            """
            Si se proporciona un color, la superficie se llena con ese color.
            """

        return new_surface
        """
        Devuelve la nueva superficie creada.
        """
    def create_center_surface(
        
        self,
        x: int = 500,
        y: int = 500,
        alpha: bool = False,
        color: Optional[ColorValue] = None,
    ):
        new_surface = self.create_surface(x, y, alpha, color)
       
        center_cors = new_surface.get_rect(
            center=(self.screen.get_width() // 2, self.screen.get_height() // 2)
        )
        """
        Se crea una superficie centrada en la pantalla.
            new_surface: Llama al método create_surface() para crear una superficie.
            center_cors: Calcula las coordenadas del centro para posicionar la superficie centrada en la pantalla.
        """

        return (new_surface, center_cors)
        """
        Devuelve la superficie y las coordenadas centrales.
        """

    def blit_surface(self, surface: SurfaceType, cors: RectType):
        """
        Con este metodo podemos dibujar superficies con sus repectivos elementos en pantalla.

        Args:
            surface (Surface): La superficie que se va a renderizar.
            cors (RectType): Las coordenadas donde se va a dibujar la superficie.
        """
        self.screen.blit(surface, cors)

    def blit_button(self, surface: SurfaceType, button: Button, x: int = 0, y: int = 0):
        self.__buttons.append(button)
        """
        Dibujamos un botón en la superficie y añade el botón a la lista de botones.
            self.__buttons.append(button): Añade el botón a la lista interna.
        """

        button.blit(surface, x, y)
        """
        Dibuja el botón en la superficie en las coordenadas especificadas.
            button.blit(surface, x, y): Dibuja el botón en la superficie en las coordenadas especificadas (x, y).
        """

if __name__ == "__main__":
    pygame.init()
    """
    Inicializa todos los módulos de pygame.
    """

    game = Game("Triki!")
    """
    Crea una instancia del juego con el título "Triki!".
    """
    surface_center, center_cors = game.create_center_surface()
    """
    Crea una superficie centrada en la pantalla.
    """
    button = Button(center_cors.topleft)
    """
    Crea un botón, lo coloca en la esquina superior izquierda de la superficie centrada.
    """
    button.insert_text("quit!", 16, "yellow")
    """
    El texto del botón es "quit!" con tamaño de fuente 16 y color amarillo.
    """
    def on_quit():
        pygame.quit()
        exit()
    """
    Define una función que cierra el juego cuando se hace clic en el botón.
    """

    button.on_click = on_quit
    """
    El botón se configura para cerrar el juego cuando se hace clic en él.
    """
    surface_width, surface_height = surface_center.get_size()

    game.blit_button(
        surface_center,
        button,
        x=surface_width // 2 - button.surface.get_width() // 2,
        y=surface_height // 2 - button.surface.get_height() // 2,
    )
    """
    Coloca el botón en el centro de la superficie.
    """
    game.blit_surface(surface_center, center_cors)
    """
    Dibuja la superficie centrada en la pantalla.
    """

    def on_click(event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            for button in game.buttons:
                if button.is_hover(mouse_pos):
                    button.click()
    """
    Define una función que detecta el clic del ratón y verifica si se ha hecho clic en algún botón. Si es así, ejecuta la acción asociada (en este caso, salir del juego).
    """
    game.on_click = on_click
    """
    Captura los eventos de clic del ratón. Si un botón está bajo el ratón cuando se hace clic, se ejecuta su función click().
    """ 

    game.init()
    """
    Inicia el juego.
    """