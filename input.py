import pygame as pg

pg.init()

class InputBox:

    def __init__(self, x, y, w, h, screen,font, inactivecolor, activecolor, text=''):
        self.rect = pg.Rect(x,y,w,h)
        self.color = inactivecolor
        self.othercolor = activecolor
        self.txt_surface = font.render(text,True,self.color)
        self.active = False 
        self.text = text
        self.screen = screen
        self.font = font
        self.x = x
        self.y = y
        
    def handle_event(self,event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active

            else:
                self.active = False

            self.color = self.othercolor if self.active else self.color
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    potat = self.text
                    self.text = ''
                    self.txt_surface = font.render(text, True, self.color)
                    return potat
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, self.color)
    def draw(self):
        self.screen.blit(self.txt_surface, (self.x, self.y))
        pg.draw.rect(self.screen,self.color,self.rect,2, border_radius=8)

        
                        
                    
                        
                
