import pygame

HEIGHT = 700
WIDTH = 1100

BACKGROUND_PATH = "assets/Background.png"
TRICKYBUTTONSTART_PATH = "assets/StartButton.png"
TRICKYBUTTONEXIT_PATH = "assets/ExitButton.png"
TRICKYGRID_PATH = "assets/TrickyGrid.png"
TRICKYPLAYBUTTON_PATH = "assets/PlayButton.png"
TRICKYX_PATH = "assets/TrickyX.png"
TRICKYO_PATH = "assets/TrickyO.png"

def get_font(size: int):
    return pygame.font.Font("assets/font.ttf", size)
