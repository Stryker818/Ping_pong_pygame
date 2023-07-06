#Imports
from pygame import *
import random

#Font
font.init()
#Create window
window = display.set_mode((700, 500))
#Create name of the window
display.set_caption("Космо-Шутер")

#Create background
background = transform.scale(image.load("ping_pong_table.jpg"), (700, 500))

#Create clock
clock = time.Clock()
FPS = 60

#Gme for while
game = True
finish = False


#Create music and Sound
#mixer.pre_init(44100, -16, 1, 512)
#mixer.init()
#Music = mixer.music.load("Techno.mp3")
#Sound = mixer.Sound("Pulya.ogg")
#mixer.music.play(-1)
##Set volume for music and Sound
#mixer.music.set_volume(0.1)
#Sound.set_volume(1)


#Create class "GameSprite"
class GameSprite(sprite.Sprite):
    def __init__(self, pic, x, y, speed, spr_x, spr_y):
        super().__init__()
        self.image = transform.scale(image.load(pic), (spr_x, spr_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#Create class Player with parent class "Player"
class Player(GameSprite):
    
    #Update for Player
    def update_left(self):
        keys = key.get_pressed()
        
        #Moving of Player
        if keys[K_w] and self.rect.y > self.speed:
            self.rect.y -= self.speed
    
        if keys[K_s] and self.rect.y < 350-self.speed:
            self.rect.y += self.speed
    
    def update_right(self):
        keys = key.get_pressed()
        
        #Moving of Player
        if keys[K_UP] and self.rect.y > self.speed:
            self.rect.y -= self.speed
    
        if keys[K_DOWN] and self.rect.y < 350-self.speed:
            self.rect.y += self.speed

#Group of sprites
bullets = sprite.Group()

#class Bullet
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()




                    #self, pic, x, y, speed, spr_x, spr_y
left_player = Player('rocket_left.png', 20, 210, 10, 20, 160)
right_player = Player('rocket_right.png', 650, 210, 10, 20, 160)
ball = GameSprite('ping_pong_ball.png', 350, 250, 10, 50, 50)


#Create font and labels
font1 = font.SysFont('Arial', 80)

win = font1.render("YOU WIN!", True, (0, 255, 0))
lose = font1.render("YOU LOSE!", True, (255, 0, 0))
    

#Group of sprites
bullets = sprite.Group()

#class Bullet
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()



#Groups of sprites 
enemies = sprite.Group()
asteroids = sprite.Group()


#Create font and labels
font1 = font.SysFont('Arial', 80)

win = font1.render("YOU WIN!", True, (0, 255, 0))
lose = font1.render("YOU LOSE!", True, (255, 0, 0))

#Gaming while cycle
while game:
    #Cycle for keystrokes
    for e in event.get():
        #Interpreter if for QUIT
        if e.type == QUIT:
            game = False 
        
    
    #Cycle for FINISH
    if finish != True:
        window.blit(background, (0,0))
        left_player.reset()
        right_player.reset()
        left_player.update_left()
        right_player.update_right()
        ball.reset()
        display.update()
    time.delay(10)    