class ButtonNotRederedException(Exception):
    """El botón no ha sido renderizado en ninguna superficie por lo tanto no tiene coordenadas."""


class EmptyPlayException(Exception):
    """Cuando en alguna parte de la lógica se ha jugado una jugada vacia (Ni X, ni O)"""
