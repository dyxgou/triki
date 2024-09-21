import pygame

HEIGHT = 700
WIDTH = 1100

BACKGROUND_PATH = "assets/Background.png"
TRICKYGRID_PATH = "assets/TrickyGrid.png"
TRICKYBIGBUTTON_PATH = "assets/TrickyBigButton.png"
TRICKYSMALLBUTTON_PATH = "assets/TrickySmallButton.png"

def get_font(size: int):
    return pygame.font.Font("assets/font.ttf", size)
