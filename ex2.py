import pygame as pg
class Rectangle:
    def __init__(self,rgb = (0,0,0),x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.rgb = rgb
    def draw(self,screen):
        pg.draw.rect(screen,self.rgb,(self.x,self.y,self.w,self.h))
# class ButtonPressed:
#     def __init__(self,s):
#         self.s = 0
#     def move(self,)
pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
rec = Rectangle((120,20,220),100,100,100,100)
w,a,s,d = 0,0,0,0
xmove = 0
ymove = 0
sp = 0.1 #speed
while(run) :
    screen.fill((255, 255, 255))
    rec.x += d-a
    rec.y += s-w
    rec.draw(screen)

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
                d = sp
            if event.key == pg.K_a: #ปุ่มถูกกดและเป็นปุ่ม A
                a = sp
            if event.key == pg.K_s:
                s = sp
            if event.key == pg.K_w:
                w = sp
        if event.type == pg.KEYUP:
            w,a,s,d = 0,0,0,0
        
            
        
        
    