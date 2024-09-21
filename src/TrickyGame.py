from typing import Any
import pygame 
from settings import WIDTH, HEIGHT, TRICKYBIGBUTTON_PATH, TRICKYSMALLBUTTON_PATH, TRICKYGRID_PATH, get_font
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


class CreateButton():
    def __init__(self, CordX, CordY, Sprite, SpriteSize, Text, TextFont, TextColor):
        SpriteWidth = Sprite.get_width()
        SpriteHeight = Sprite.get_height()
        ScaledSpriteX = int(SpriteWidth*SpriteSize)
        ScaledSpriteY = int(SpriteHeight*SpriteSize)
        self.image = pygame.transform.scale(Sprite, (ScaledSpriteX, ScaledSpriteY))
        self.rect = self.image.get_rect()
        self.rect.topleft = (CordX, CordY)
        ButtonText = TextFont.render(Text, True, TextColor)
        TextWidth = ButtonText.get_width()
        TextHeight = ButtonText.get_height()
        TextSize = SpriteSize + 0.3
        ScaledTextX = int(TextWidth*TextSize)
        ScaledTextY = int(TextHeight*TextSize)
        self.Text = pygame.transform.scale(ButtonText, (ScaledTextX, ScaledTextY))
        TextImageX = CordX + (int((ScaledSpriteX-ScaledTextX)/2))
        TextImageY = CordY + (int((ScaledSpriteY-ScaledTextY)/2))
        self.TextCords = (TextImageX, TextImageY)
        self.clicked = False

    def PlaceButton(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        screen.blit(self.Text, (self.TextCords))
        
    def ButtonMouseReact(self):
        ActionPerform = False
        MousePosition = pygame.mouse.get_pos()
        if self.rect.collidepoint(MousePosition):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked == False:
                self.clicked = True
                ActionPerform = True
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked = False
        return ActionPerform

class CreateImage():
    def __init__(self, CordX, CordY, sprite, size):
        width = sprite.get_width()
        height = sprite.get_height()
        self.image = pygame.transform.scale(sprite, (int(width*size), int(height*size)))
        self.Cords = (CordX, CordY)
        self.clicked = False

    def PlaceImage(self):
        screen.blit(self.image, (self.Cords))
        
    
                
def TrickyGameTurnsUI(TurnOrder, CordX, CordY, font, color):
    pygame.draw.rect(screen, background_colour, pygame.Rect(CordX, CordY, 320, 60))
    TURN_UI = font.render(f"Es el turno de {TurnOrder}", True, color)
    screen.blit(TURN_UI, (CordX, CordY))

def TrickyGameLogicUI(CordX, CordY, font, color):
    if RandomTurn[0] == 0:
        TrickyX = font.render(f"X", True, color)
        screen.blit(TrickyX, (CordX, CordY))
        RandomTurn[0] = 1
        return
    if RandomTurn[0] == 1:
        TrickyO = font.render(f"O", True, color)
        screen.blit(TrickyO, (CordX, CordY))
        RandomTurn[0] = 0
        return

#Concepto para el tablero
#def CreateGrid(self):
#        Grid_X_Size = len(PlayButton_X_Cord)
#        Grid_Y_Size = len(PlayButton_Y_Cord)
#        for x in range(Grid_X_Size):
#            for y in range(Grid_Y_Size):
#                screen.blit(self.image, (PlayButton_X_Cord[x], PlayButton_Y_Cord[y]))

Grid_X =[125,225,325]
Grid_Y =[285,380,475]
TrickyPos_X =[150,250,350]
TrickyPos_Y =[295,390,485]
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
        TrickyGameTurnsUI(TurnOrder[RandomTurn[0]], 125, 210, GAME_FONT, (255, 255, 0))
        if ExitButtonInGame.ButtonMouseReact() == True:
            pygame.quit()
            sys.exit()
        if PlayButtonInGame1.ButtonMouseReact() == True:
            TrickyGameLogicUI(TrickyPos_X[0], TrickyPos_Y[0], GAME_FONT, (255, 255, 0))
        if PlayButtonInGame2.ButtonMouseReact() == True:
            TrickyGameLogicUI(TrickyPos_X[1], TrickyPos_Y[0], GAME_FONT, (255, 255, 0))
        if PlayButtonInGame3.ButtonMouseReact() == True:
            TrickyGameLogicUI(TrickyPos_X[2], TrickyPos_Y[0], GAME_FONT, (255, 255, 0))
        if PlayButtonInGame4.ButtonMouseReact() == True:
            TrickyGameLogicUI(TrickyPos_X[0], TrickyPos_Y[1], GAME_FONT, (255, 255, 0))
        if PlayButtonInGame5.ButtonMouseReact() == True:
            TrickyGameLogicUI(TrickyPos_X[1], TrickyPos_Y[1], GAME_FONT, (255, 255, 0))
        if PlayButtonInGame6.ButtonMouseReact() == True:
            TrickyGameLogicUI(TrickyPos_X[2], TrickyPos_Y[1], GAME_FONT, (255, 255, 0))
        if PlayButtonInGame7.ButtonMouseReact() == True:
            TrickyGameLogicUI(TrickyPos_X[0], TrickyPos_Y[2], GAME_FONT, (255, 255, 0))
        if PlayButtonInGame8.ButtonMouseReact() == True:
            TrickyGameLogicUI(TrickyPos_X[1], TrickyPos_Y[2], GAME_FONT, (255, 255, 0))
        if PlayButtonInGame9.ButtonMouseReact() == True:
            TrickyGameLogicUI(TrickyPos_X[2], TrickyPos_Y[2], GAME_FONT, (255, 255, 0))
        
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

