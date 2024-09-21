from typing import Any
import pygame 
from settings import WIDTH, HEIGHT, TRICKYBIGBUTTON_PATH, TRICKYSMALLBUTTON_PATH, TRICKYGRID_PATH, get_font
from GameFunctions import CreateButton, CreateImage, ScaleImage, CenterImage
import sys
import random
  
pygame.init()

FPS = 10
FramePerSec = pygame.time.Clock()


background_colour = (55, 20, 55) 
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('test') 
GAME_FONT = get_font(20)
  
BigButton = pygame.image.load(TRICKYBIGBUTTON_PATH)
SmallButton = pygame.image.load(TRICKYSMALLBUTTON_PATH)
Grid = pygame.image.load(TRICKYGRID_PATH)

def TrickyGameTurnsUI(CordX, CordY, font, color):
    pygame.draw.rect(screen, background_colour, pygame.Rect(CordX, CordY, 320, 60))
    TURN_UI = font.render(f"Es el turno de {TurnOrder[RandomTurn[0]]}", True, color)
    screen.blit(TURN_UI, (CordX, CordY))

def TrickyGameLogicUI(CordX, CordY, font, color, Sprite, SpriteSize):
    ScaleUIList = ScaleImage(Sprite, SpriteSize)
    TrickyGridUI = font.render(f"{TurnOrder[RandomTurn[0]]}", True, color)
    ScaleTextList = ScaleImage(TrickyGridUI, 1)
    CenterImageCords = CenterImage(CordX, CordY, ScaleUIList[0], ScaleUIList[1], ScaleTextList[0], ScaleTextList[1])
    screen.blit(TrickyGridUI, (CenterImageCords[0], CenterImageCords[1]))
    if RandomTurn[0] == 0:
        RandomTurn[0] = 1
    else:
        RandomTurn[0] = 0

Grid_X =[125,225,325]
Grid_Y =[285,380,475]
StartButtonIngame = CreateButton(212, 70, BigButton, 0.5, "START", GAME_FONT, (255, 255, 0))
ExitButtonInGame = CreateButton(212, 130, BigButton, 0.5, "EXIT", GAME_FONT, (255, 255, 0))

GridInGame = CreateImage(100, 250, Grid, 1)

PlayButtonInGame1 = CreateButton(Grid_X[0], Grid_Y[0], SmallButton, 0.7, " ", GAME_FONT, (0, 0, 0))
PlayButtonInGame2 = CreateButton(Grid_X[1], Grid_Y[0], SmallButton, 0.7, " ", GAME_FONT, (0, 0, 0))
PlayButtonInGame3 = CreateButton(Grid_X[2], Grid_Y[0], SmallButton, 0.7, " ", GAME_FONT, (0, 0, 0))
PlayButtonInGame4 = CreateButton(Grid_X[0], Grid_Y[1], SmallButton, 0.7, " ", GAME_FONT, (0, 0, 0))
PlayButtonInGame5 = CreateButton(Grid_X[1], Grid_Y[1], SmallButton, 0.7, " ", GAME_FONT, (0, 0, 0))
PlayButtonInGame6 = CreateButton(Grid_X[2], Grid_Y[1], SmallButton, 0.7, " ", GAME_FONT, (0, 0, 0))
PlayButtonInGame7 = CreateButton(Grid_X[0], Grid_Y[2], SmallButton, 0.7, " ", GAME_FONT, (0, 0, 0))
PlayButtonInGame8 = CreateButton(Grid_X[1], Grid_Y[2], SmallButton, 0.7, " ", GAME_FONT, (0, 0, 0))
PlayButtonInGame9 = CreateButton(Grid_X[2], Grid_Y[2], SmallButton, 0.7, " ", GAME_FONT, (0, 0, 0))

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
        TrickyGameTurnsUI(125, 210, GAME_FONT, (255, 255, 0))
        if ExitButtonInGame.ButtonMouseReact() == True:
            pygame.quit()
            sys.exit()
        if PlayButtonInGame1.ButtonMouseReact() == True:
            TrickyGameLogicUI(Grid_X[0], Grid_Y[0], GAME_FONT, (255, 255, 0), SmallButton, 0.7)
            PlayButtonInGame1.RemoveButton()
        if PlayButtonInGame2.ButtonMouseReact() == True:
            TrickyGameLogicUI(Grid_X[1], Grid_Y[0], GAME_FONT, (255, 255, 0), SmallButton, 0.7)
            PlayButtonInGame2.RemoveButton()
        if PlayButtonInGame3.ButtonMouseReact() == True:
            TrickyGameLogicUI(Grid_X[2], Grid_Y[0], GAME_FONT, (255, 255, 0), SmallButton, 0.7)
            PlayButtonInGame3.RemoveButton()
        if PlayButtonInGame4.ButtonMouseReact() == True:
            TrickyGameLogicUI(Grid_X[0], Grid_Y[1], GAME_FONT, (255, 255, 0), SmallButton, 0.7)
            PlayButtonInGame4.RemoveButton()
        if PlayButtonInGame5.ButtonMouseReact() == True:
            TrickyGameLogicUI(Grid_X[1], Grid_Y[1], GAME_FONT, (255, 255, 0), SmallButton, 0.7)
            PlayButtonInGame5.RemoveButton()
        if PlayButtonInGame6.ButtonMouseReact() == True:
            TrickyGameLogicUI(Grid_X[2], Grid_Y[1], GAME_FONT, (255, 255, 0), SmallButton, 0.7)
            PlayButtonInGame6.RemoveButton()
        if PlayButtonInGame7.ButtonMouseReact() == True:
            TrickyGameLogicUI(Grid_X[0], Grid_Y[2], GAME_FONT, (255, 255, 0), SmallButton, 0.7)
            PlayButtonInGame7.RemoveButton()
        if PlayButtonInGame8.ButtonMouseReact() == True:
            TrickyGameLogicUI(Grid_X[1], Grid_Y[2], GAME_FONT, (255, 255, 0), SmallButton, 0.7)
            PlayButtonInGame8.RemoveButton()
        if PlayButtonInGame9.ButtonMouseReact() == True:
            TrickyGameLogicUI(Grid_X[2], Grid_Y[2], GAME_FONT, (255, 255, 0), SmallButton, 0.7)
            PlayButtonInGame9.RemoveButton()
        
        pygame.display.update()
        FramePerSec.tick(FPS)

def MenuInicial():
    while running: 
        for event in pygame.event.get():      
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
        StartButtonIngame.PlaceButton()
        ExitButtonInGame.PlaceButton()
        if ExitButtonInGame.ButtonMouseReact() == True:
            pygame.quit()
            sys.exit()
        if StartButtonIngame.ButtonMouseReact() == True:
            GridInGame.PlaceImage()
            PlayButtonInGame1.PlaceButton()
            PlayButtonInGame2.PlaceButton()
            PlayButtonInGame3.PlaceButton()
            PlayButtonInGame4.PlaceButton()
            PlayButtonInGame5.PlaceButton()
            PlayButtonInGame6.PlaceButton()
            PlayButtonInGame7.PlaceButton()
            PlayButtonInGame8.PlaceButton()
            PlayButtonInGame9.PlaceButton()
            GameTricky()
        pygame.display.update()
        FramePerSec.tick(FPS)

MenuInicial()

