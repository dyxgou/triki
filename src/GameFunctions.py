import pygame
from settings import WIDTH, HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class CreateImage():
    def __init__(self, CordX, CordY, sprite, size):
        width = sprite.get_width()
        height = sprite.get_height()
        self.image = pygame.transform.scale(sprite, (int(width*size), int(height*size)))
        self.Cords = (CordX, CordY)
        self.clicked = False

    def PlaceImage(self):
        screen.blit(self.image, (self.Cords))

class CreateButton():
    def __init__(self, CordX, CordY, Sprite, SpriteSize, Text, TextFont, TextColor):
        ScaleListSprite = ScaleImage(Sprite, SpriteSize)
        self.image = pygame.transform.scale(Sprite, (ScaleListSprite[0], ScaleListSprite[1]))
        self.rect = self.image.get_rect()
        self.rect.topleft = (CordX, CordY)
        ButtonText = TextFont.render(Text, True, TextColor)
        ScaleListText = ScaleImage(ButtonText, (SpriteSize+0.3))
        self.Text = pygame.transform.scale(ButtonText, (ScaleListText[0], ScaleListText[1]))
        CenterCordsList = CenterImage(CordX, CordY, ScaleListSprite[0], ScaleListSprite[1], ScaleListText[0], ScaleListText[1])
        self.TextCords = (CenterCordsList[0], CenterCordsList[1])
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
    
    def RemoveButton(self):
        self.rect.scale_by_ip(0)

def ScaleImage(Sprite, SpriteSize):
    SpriteWidth = Sprite.get_width()
    SpriteHeight = Sprite.get_height()
    ScaledSpriteX = int(SpriteWidth*SpriteSize)
    ScaledSpriteY = int(SpriteHeight*SpriteSize)
    ScaleList = [ScaledSpriteX, ScaledSpriteY]
    return ScaleList

def CenterImage(CordX, CordY, Image1ScaleX, Image1ScaleY, Image2ScaleX, Image2ScaleY):
    CenterImageX = CordX + (int((Image1ScaleX-Image2ScaleX)/2))
    CenterImageY = CordY + (int((Image1ScaleY-Image2ScaleY)/2))
    CenterCordsList = [CenterImageX, CenterImageY]
    return CenterCordsList