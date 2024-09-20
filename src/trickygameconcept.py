from typing import Any
import pygame 
from settings import WIDTH, HEIGHT, TRICKYBUTTONSTART_PATH, TRICKYBUTTONEXIT_PATH, TRICKYGRID_PATH, TRICKYPLAYBUTTON_PATH
  
pygame.init()

FPS = 10
FramePerSec = pygame.time.Clock()


background_colour = (55, 20, 55) 
screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption('test') 
  
StartButton = pygame.image.load(TRICKYBUTTONSTART_PATH)
ExitButton = pygame.image.load(TRICKYBUTTONEXIT_PATH)
Grid = pygame.image.load(TRICKYGRID_PATH)
PlayButton = pygame.image.load(TRICKYPLAYBUTTON_PATH)

  
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
                print("CLICK")
                self.clicked = True
                ActionPerform = True
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked = False
        return ActionPerform
    
    def CreateGrid(self):
        Grid_X_Size = len(PlayButton_X_Cord)
        Grid_Y_Size = len(PlayButton_Y_Cord)
        for x in range(Grid_X_Size):
            for y in range(Grid_Y_Size):
                screen.blit(self.image, (PlayButton_X_Cord[x], PlayButton_Y_Cord[y]))
                

StartButtonIngame = GameImageInteractions(212, 100, StartButton, 0.5)
ExitButtonInGame = GameImageInteractions(212, 160, ExitButton,0.5)
GridInGame = GameImageInteractions(100, 250, Grid, 1)
PlayButtonInGame = GameImageInteractions(0, 0, PlayButton, 0.7)

Grid_X =[125,225,325]
Grid_Y =[285,380,475]
PlayButton_X_Cord = [Grid_X[0], Grid_X[1], Grid_X[2], Grid_X[0], Grid_X[1], Grid_X[2], Grid_X[0], Grid_X[1], Grid_X[2]]
PlayButton_Y_Cord = [Grid_Y[0], Grid_Y[0], Grid_Y[0], Grid_Y[1], Grid_Y[1], Grid_Y[1], Grid_Y[2], Grid_Y[2], Grid_Y[2]]



screen.fill(background_colour)
pygame.display.flip() 
running = True
while running: 
    for event in pygame.event.get():      
        if event.type == pygame.QUIT: 
            running = False
    StartButtonIngame.PlaceImage()
    ExitButtonInGame.PlaceImage()
    if ExitButtonInGame.ImageMouseReact() == True:
        break
    if StartButtonIngame.ImageMouseReact() == True:
        GridInGame.PlaceImage()
        PlayButtonInGame.CreateGrid()
    if PlayButtonInGame.ImageMouseReact() == True:
        pass
    pygame.display.update()
    FramePerSec.tick(FPS)

pygame.quit()