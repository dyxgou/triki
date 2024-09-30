class ButtonNotRederedException(Exception):
    """El botón no ha sido renderizado en ninguna superficie por lo tanto no tiene coordenadas."""
    """
    Excepción lanzada cuando un botón no ha sido renderizado en ninguna superficie gráfica.

    Esto ocurre cuando el botón no ha sido dibujado o mostrado en la interfaz gráfica, 
    lo que significa que no tiene coordenadas asignadas y no puede interactuar con el usuario.
    """


class EmptyPlayException(Exception):
    """Cuando en alguna parte de la lógica se ha jugado una jugada vacia (Ni X, ni O)"""
    """Excepción lanzada cuando se realiza una jugada vacía en la lógica del juego.

    Esto sucede cuando se intenta registrar una jugada que no corresponde ni a 'X' ni a 'O',
    lo que generalmente representa un error en el flujo del juego.
    """