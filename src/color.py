from typing import Sequence, Tuple, Union

from pygame import Color

RGBAOutput = Tuple[int, int, int, int]
"""
Representa un color RGBA (rojo, verde, azul, alfa) como una tupla de cuatro enteros.
Cada entero tiene un valor de 0 a 255, donde:
- El primer entero es el componente rojo (R).
- El segundo entero es el componente verde (G).
- El tercer entero es el componente azul (B).
- El cuarto entero es el canal alfa (A), que representa la transparencia.
"""

ColorValue = Union[Color, int, str, Tuple[int, int, int], RGBAOutput, Sequence[int]]
"""
Representa un valor de color que puede ser de varios tipos compatibles con pygame.
Este tipo flexible permite especificar colores en diferentes formatos, incluyendo:
- `Color`: Un objeto de color de pygame.
- `int`: Un valor entero que puede representar un color codificado.
- `str`: Una cadena que representa el nombre del color (por ejemplo, "red" o "blue").
- `Tuple[int, int, int]`: Una tupla de tres enteros para representar un color en formato RGB (rojo, verde, azul).
- `RGBAOutput`: Una tupla de cuatro enteros que incluye el canal alfa (RGBA).
- `Sequence[int]`: Cualquier secuencia de enteros que represente un color.
"""
