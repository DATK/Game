import pygame as pg
from src.interface_elements.Button import Button
from src.interface_elements.Label import Label
config = {"RESHD": (1280, 720), "RESFHD": (1920, 1080), "NAME": "TEST"}


class Player:

    def __init__(self):
        self.player_texture = pg.image.load("./src/img/player.png")
        self.player_texture = pg.transform.scale(
            self.player_texture, (80, 120))
        self.player_texture.set_colorkey((255, 255, 255))
        self.player_rect = self.player_texture.get_rect()

        self.x = 100
        self.y = 300
        self.speed = 5

    def move_keyboard(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.y -= self.speed
        if keys[pg.K_s]:
            self.y += self.speed
        if keys[pg.K_a]:
            self.x -= self.speed
        if keys[pg.K_d]:
            self.x += self.speed

    def move_button_right(self):
        self.x += self.speed
            
    def move_button_left(self):
        self.x -= self.speed
       

    def draw(self, scr):
        scr.blit(self.player_texture, (self.x, self.y))

    def retr_rect(self):
        return self.player_rect


class Game:

    def __init__(self):
        pg.init()
        self.main_res = config["RESHD"]
        self.screen = pg.display.set_mode(self.main_res)
        pg.display.set_caption(config["NAME"])
        self.clc = pg.time.Clock()
        self.fps = 60
        self.load_objects()

    def load_objects(self):
        self.pl = Player()
        self.phone = pg.image.load("./src/img/phone.png")
        self.phone = pg.transform.scale(self.phone, self.main_res)
        self.fps_label = Label(30, 1200, 200, 50)
        self.left_button=Button(30,660,70,40,text="Left",function=self.pl.move_button_left)
        self.right_button=Button(1200,660,70,40,text="Right",function=self.pl.move_button_right)
        

    def change_res(self):
        self.main_res = (config["RESFHD"])
        self.screen = pg.display.set_mode(self.main_res)
        self.load_objects()

    def draw_objects(self, event=None):
        self.screen.blit(self.phone, (0, 0))
        self.fps_label.show(self.screen, text=str(
            int(self.clc.get_fps())), isbackground=False)
        self.left_button.show_rect(self.screen)
        self.right_button.show_rect(self.screen)
        self.left_button.changing_rect(pg.mouse.get_pos())
        self.right_button.changing_rect(pg.mouse.get_pos())
        self.left_button.do_func(event)
        self.right_button.do_func(event)
        
        self.pl.draw(self.screen)

    def run(self):
        while True:
            for event in pg.event.get():
                self.draw_objects(event)
                self.pl.move_keyboard()
                if event.type == pg.QUIT:
                    exit()
            self.clc.tick(self.fps)
            pg.display.update()


app = Game()

app.run()
