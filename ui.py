import pygame as pg
import sys


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.enter = False
    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
                self.enter = False
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN :
                    if self.text != "" :
                        self.enter = True
                    self.color = COLOR_INACTIVE
                    self.active = False
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)





pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

firstname = InputBox(200, 100, 140, 32) # สร้าง InputBox1
lastname = InputBox(200, 164, 140, 32) # สร้าง InputBox2
age = InputBox(200, 228, 140, 32)
input_boxes = [firstname, lastname,age] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True
font = pg.font.Font('freesansbold.ttf', 16) # font and fontsize
tfont = pg.font.Font('freesansbold.ttf', 18)
sfont = pg.font.Font('freesansbold.ttf', 10)
while run:
    screen.fill((255, 255, 200))
    screen.blit(tfont.render("firstname ", True, (0,0,0)),(80,100+9))
    screen.blit(tfont.render("lastname ", True, (0,0,0)),(80,164+9))
    screen.blit(tfont.render("age ", True, (0,0,0)),(80,228+9))
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
    outn = "Your name is" + firstname.text + " " + lastname.text + "!"
    try :
        int(age.text) 
        outa = " You are " + age.text + " years old."
    except :
        if age.enter :
            screen.blit(font.render("Please enter numbers only", True, (200,0,0)),(410,235))
            age.text = ""
        outa = "None"
    if not firstname.enter :
        screen.blit(sfont.render("required", True, (220,0,0)),(210,100+36))
    if not lastname.enter : 
        screen.blit(sfont.render("required", True, (220,0,0)),(210,164+36))
    if not age.enter :
        screen.blit(sfont.render("required", True, (220,0,0)),(210,228+36))

    text = font.render('FRA 142', True, (255,255,255), (0,0,0)) # (text,is smooth?,letter color,background color)
    finaltext = outn + outa
    if age.enter and firstname.enter and lastname.enter and outa != "None" :
        screen.blit(FONT.render(finaltext, True, (200,0,00)),(30,350))
    
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()