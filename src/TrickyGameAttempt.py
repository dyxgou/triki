from typing import Any
import pygame 
from settings import WIDTH, HEIGHT, TRICKYBUTTONSTART_PATH, TRICKYBUTTONEXIT_PATH, TRICKYGRID_PATH, TRICKYPLAYBUTTON_PATH, TRICKYX_PATH, TRICKYO_PATH, get_font
import sys
import random
  
pygame.init()


FPS = 10
FramePerSec = pygame.time.Clock()


background_colour = (55, 20, 55) 
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('test') 
TURN_FONT = get_font(20)
  
StartButton = pygame.image.load(TRICKYBUTTONSTART_PATH)
ExitButton = pygame.image.load(TRICKYBUTTONEXIT_PATH)
Grid = pygame.image.load(TRICKYGRID_PATH)
PlayButton = pygame.image.load(TRICKYPLAYBUTTON_PATH)
TrickyX = pygame.image.load(TRICKYX_PATH)
TrickyO = pygame.image.load(TRICKYO_PATH)
  
class GameImageInteractions():
    def __init__(self, CordX, CordY, sprite, size):
        width = sprite.get_width()
        height = sprite.get_height()
        self.image = pygame.transform.scale(sprite, (int(width*size), int(height*size)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (CordX, CordY)
        self.clicked = False

    def PlaceImage(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def ImageMouseReact(self):
        ActionPerform = False
        MousePosition = pygame.mouse.get_pos()
        if self.rect.collidepoint(MousePosition):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked == False:
                self.clicked = True
                ActionPerform = True
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked = False
        return ActionPerform
    
    
                
def TrickyGameTurnsUI(TurnOrder, font, color, CordX, CordY):
    pygame.draw.rect(screen, background_colour, pygame.Rect(CordX, CordY, 320, 60))
    TURN_UI = font.render(f"Es el turno de {TurnOrder}", True, color)
    screen.blit(TURN_UI, (CordX, CordY))

def TrickyGameLogicUI(TurnOrder, CordX, CordY):
    if TurnOrder == "X":
        screen.blit(TrickyX, (CordX, CordY))
        RandomTurn[0] = 1
    if TurnOrder == "O":
        screen.blit(TrickyO, (CordX, CordY))
        RandomTurn[0] = 0
    
    

Grid_X =[125,225,325]
Grid_Y =[285,380,475]
TrickyPos_X =[150,250,350]
TrickyPos_Y =[295,390,485]
StartButtonIngame = GameImageInteractions(212, 70, StartButton, 0.5)
ExitButtonInGame = GameImageInteractions(212, 130, ExitButton,0.5)
GridInGame = GameImageInteractions(100, 250, Grid, 1)
PlayButtonInGame1 = GameImageInteractions(Grid_X[0], Grid_Y[0], PlayButton, 0.7)
PlayButtonInGame2 = GameImageInteractions(Grid_X[1], Grid_Y[0], PlayButton, 0.7)
PlayButtonInGame3 = GameImageInteractions(Grid_X[2], Grid_Y[0], PlayButton, 0.7)
PlayButtonInGame4 = GameImageInteractions(Grid_X[0], Grid_Y[1], PlayButton, 0.7)
PlayButtonInGame5 = GameImageInteractions(Grid_X[1], Grid_Y[1], PlayButton, 0.7)
PlayButtonInGame6 = GameImageInteractions(Grid_X[2], Grid_Y[1], PlayButton, 0.7)
PlayButtonInGame7 = GameImageInteractions(Grid_X[0], Grid_Y[2], PlayButton, 0.7)
PlayButtonInGame8 = GameImageInteractions(Grid_X[1], Grid_Y[2], PlayButton, 0.7)
PlayButtonInGame9 = GameImageInteractions(Grid_X[2], Grid_Y[2], PlayButton, 0.7)
TurnOrder = ["X", "O"]
RandomTurn=[]


screen.fill(background_colour)
pygame.display.flip() 
running = True


def GameTricky():
    RandomTurn.append(random.randint(0,1))
    while running: 
        for event in pygame.event.get():      
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
        TrickyGameTurnsUI(TurnOrder[RandomTurn[0]], TURN_FONT, (255, 255, 0), 125, 210)
        if ExitButtonInGame.ImageMouseReact() == True:
            pygame.quit()
            sys.exit()
        if PlayButtonInGame1.ImageMouseReact() == True:
            TrickyGameLogicUI(TurnOrder[RandomTurn[0]], TrickyPos_X[0], TrickyPos_Y[0])
        if PlayButtonInGame2.ImageMouseReact() == True:
            TrickyGameLogicUI(TurnOrder[RandomTurn[0]], TrickyPos_X[1], TrickyPos_Y[0])
        if PlayButtonInGame3.ImageMouseReact() == True:
            TrickyGameLogicUI(TurnOrder[RandomTurn[0]], TrickyPos_X[2], TrickyPos_Y[0])
        if PlayButtonInGame4.ImageMouseReact() == True:
            TrickyGameLogicUI(TurnOrder[RandomTurn[0]], TrickyPos_X[0], TrickyPos_Y[1])
        if PlayButtonInGame5.ImageMouseReact() == True:
            TrickyGameLogicUI(TurnOrder[RandomTurn[0]], TrickyPos_X[1], TrickyPos_Y[1])
        if PlayButtonInGame6.ImageMouseReact() == True:
            TrickyGameLogicUI(TurnOrder[RandomTurn[0]], TrickyPos_X[2], TrickyPos_Y[1])
        if PlayButtonInGame7.ImageMouseReact() == True:
            TrickyGameLogicUI(TurnOrder[RandomTurn[0]], TrickyPos_X[0], TrickyPos_Y[2])
        if PlayButtonInGame8.ImageMouseReact() == True:
            TrickyGameLogicUI(TurnOrder[RandomTurn[0]], TrickyPos_X[1], TrickyPos_Y[2])
        if PlayButtonInGame9.ImageMouseReact() == True:
            TrickyGameLogicUI(TurnOrder[RandomTurn[0]], TrickyPos_X[2], TrickyPos_Y[2])
        
        pygame.display.update()
        FramePerSec.tick(FPS)

def MenuInicial():
    while running: 
        for event in pygame.event.get():      
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
        StartButtonIngame.PlaceImage()
        ExitButtonInGame.PlaceImage()
        if ExitButtonInGame.ImageMouseReact() == True:
            pygame.quit()
            sys.exit()
        if StartButtonIngame.ImageMouseReact() == True:
            GridInGame.PlaceImage()
            PlayButtonInGame1.PlaceImage()
            PlayButtonInGame2.PlaceImage()
            PlayButtonInGame3.PlaceImage()
            PlayButtonInGame4.PlaceImage()
            PlayButtonInGame5.PlaceImage()
            PlayButtonInGame6.PlaceImage()
            PlayButtonInGame7.PlaceImage()
            PlayButtonInGame8.PlaceImage()
            PlayButtonInGame9.PlaceImage()
            GameTricky()
        pygame.display.update()
        FramePerSec.tick(FPS)

MenuInicial()

