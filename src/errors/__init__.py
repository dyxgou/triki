class UndefinedClickHandler(Exception):
    """
    Excepción personalizada que se lanza cuando no se ha definido un manejador de clics.

    Esta excepción puede utilizarse para indicar que una función o método que 
    se esperaba que manejara eventos de clic no ha sido implementado o está ausente.

    Ejemplo:
        def handle_click(event):
            if not click_handler:
                raise UndefinedClickHandler("No se ha definido un manejador de clics.")

    Hereda de:
        Exception: La clase base para todas las excepciones en Python.
    """
    pass
