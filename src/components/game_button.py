class GameButton(Button):
    """
    Representa un botón en el juego de Triki, asociado a una casilla del tablero.

    Hereda de la clase Button y agrega funcionalidades específicas para el juego:

    * **Actualización del texto:** Muestra el símbolo correspondiente (X, O o vacío) según el estado de la casilla.
    * **Manejo de clics:** Devuelve una función que actualiza el estado del tablero cuando se hace clic en el botón.

    Atributos:
        x (int): Coordenada x del botón en el tablero.
        y (int): Coordenada y del botón en el tablero.

    Métodos:
        __init__(self, topleft: Coordinates, x: int, y: int):
            Constructor de la clase. Inicializa el botón con su posición y lo vincula a una casilla del tablero.
        insert_play(self, board: Board):
            Actualiza el texto del botón para reflejar el estado actual de la casilla en el tablero.
        get_on_click(self, board: Board) -> Callable:
            Devuelve una función que se ejecutará cuando se haga clic en el botón. Esta función actualiza el estado del tablero en la casilla correspondiente.
    """

    def __init__(self, topleft: Coordinates, x: int, y: int) -> None:
        """
        Constructor de la clase.

        Args:
            topleft (Coordinates): Coordenadas de la esquina superior izquierda del botón.
            x (int): Coordenada x de la casilla asociada en el tablero.
            y (int): Coordenada y de la casilla asociada en el tablero.
        """

        super().__init__(topleft)
        self.x = topleft.x  # Asignar la coordenada x del objeto
        self.y = topleft.y  # Asignar la coordenada y del objeto

    def insert_play(self, board: Board) -> None:
        """
        Actualiza el texto del botón según el estado de la casilla correspondiente en el tablero.

        Args:
            board (Board): Objeto que representa el tablero de juego.
        """

        play = board.get_play(self.x, self.y)

        if play == Plays.EMPTY:
            self.insert_text("", 16, "yellow")
        elif play == Plays.X:
            self.insert_text("X", 25, "yellow")
        else:
            self.insert_text("O", 25, "yellow")

    def get_on_click(self, board: Board) -> Callable:
        """
        Devuelve una función que se ejecutará cuando se haga clic en el botón.

        Args:
            board (Board): Objeto que representa el tablero de juego.

        Returns:
            Callable: Función que actualiza el estado del tablero en la casilla correspondiente.
        """

        def on_click():
            board.play(self.x, self.y)

        return on_click
