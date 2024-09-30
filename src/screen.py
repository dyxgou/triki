from typing import Callable, Optional
from pygame.event import Event
from pygame import MOUSEBUTTONDOWN, SurfaceType
import pygame
from sys import exit

from settings import HEIGHT, WIDTH, get_font, get_image
from errors import screen_errors
from clock import Clock

EventHandler = Callable[[Event], None]


class Screen(Clock):

    """Clase que representa una pantalla en el juego

    Atributes:
    __screen : SurfaceType
    Superficie donde se muestran  los elementos del juego.
    __title : str
   Título de la ventana del juego
    __background : SurfaceType
   Imagen de fondo que se muestra en la pantalla.
    __running : bool
  Indica si el juego está iniciando su ejecucion .
    __on_click : Función que se ejecuta al hacer clic en la pantalla"""

    

    __screen: SurfaceType
    __title: str
    __background: SurfaceType
    __running: bool = True
    __on_click: Optional[EventHandler] = None

    @property
    def on_click(self):
        
        """Obtiene el evento haciendo  clic en la pantalla.
        
        Returns:
        EventHandler: La función que maneja el clic."""
        
        return self.__on_click

    @on_click.setter
    def on_click(self, new_on_click: EventHandler):
        
        """Establece el evento asociado al clic en la pantalla.

        Parámetros:
       
        new_on_click : EventHandler
            La  función que manejará los clics en la pantalla"""
       
        self.__on_click = new_on_click

    def _init_(self, title: str) -> None:
       
        """Constructor de la clase Screen. Inicializa una nueva pantalla con el título dado.

        Parámetros:
       
        title : str
            El título que se mostrará en la ventana del juego."""
        
        Clock._init_(self)
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__background = get_image("Background.png")
        self._screen.blit(self._background, (0, 0))
        self.__title = title

    @property
    def screen(self):
       
        """Devuelve la superficie de la pantalla en la que se visualizan  los elementos.

        Returns:
        --------
        SurfaceType: La superficie de la pantalla."""
        
        return self.__screen

    def init(self):
       
        """Inicializa el bucle principal de la pantalla del juego.

        Este método maneja los eventos de pygame y llama al evento de clic si está definido.
        También actualiza la pantalla y controla el framerate.

        Excepciones:
       
        screen_errors.UndefinedClickException:
            Si el handler de clic no está definido, lanza esta excepción."""
       
        if self.__on_click is None:
            raise screen_errors.UndefinedClickException(
                "El click handler no ha sido definido."
            )

        pygame.display.set_caption(self.__title)

        while self.__running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
                    pygame.quit()
                    exit()

                self.__on_click(event)

            pygame.display.update()
            self.tick(30)


if _name_ == "_main_":
    menu = Screen("Triki!")

    def on_click(event: Event):
        
        """Función qu3 maneja los  eventos de clic.

        Parámetros:
      
        event : Event
            El evento de clic detectado por pygame."""
        
        if event.type == MOUSEBUTTONDOWN:
            print("click!")

    menu.on_click = on_click
    surface = pygame.Surface((500, 500))
    surface.fill((0, 0, 200))

    font = get_font(18)  # Obtiene una fuente de tamaño 18 
    button_img = get_image("TextButton.png")  # Carga una imagen de botón
    text = font.render("start", True, "yellow")  # el texto "start" en amarillo
    text_center_cors = text.get_rect(
        center=(
            button_img.get_width() // 2,
            button_img.get_height() // 2 - 10,
        )
    )  # Posiciona el texto en el centro del botón

    button_img.blit(text, text_center_cors)  # Dibuja el texto sobre la imagen del botón
    center_cors = surface.get_rect(
        center=(
            menu.screen.get_width() // 2,
            menu.screen.get_height() // 2,
        )
    )  # Posiciona la imagen del botón en el centro de la pantalla

    surface.blit(
        button_img,
        (
            0,
            0,
        ),
    )  # Dibuja la imagen del botón en la superficie

    menu.screen.blit(surface, center_cors)  # Dibuja la superficie en la pantalla
    menu.init()  # Inicializa el bucle principal del juego
