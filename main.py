import random
import pygame
from player import *


#start the pygame engine
pygame.init()

#start the pygame font engine
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 23) #load a font for use

#start the sound engine
pygame.mixer.init();

#game variables
simOver = False
p1 = Player()
cam_x = 250
cam_y = 250
map1 = Map()
camera_group = pygame.sprite.Group()



#game independent variables (needed for every pygame)
FPS = 60 #60 Frames Per Second for the game update cycle
fpsClock = pygame.time.Clock() #used to lock the game to 60 FPS
screen = pygame.display.set_mode((1280,720)); #initialize the game window
# def get_sprite(self,x,y,width,height):
#     sprite = pygame.Surface([width,height])
#     sprite.blit(self.)
def create_map_1():
    map1.add(Platform(100,600,400,30,(0,255,0)))
    map1.add(Platform(600, 430, 30, 100, (0, 255, 0)))
    map1.add(Platform(300, 600, 400, 30, (0, 255, 0)))
    map1.add(Platform(700, 430, 30, 100, (0, 255, 0)))
    map1.add(Platform(700,530,400,30,(0,255,0)))
    map1.add(Platform(0,720,1280,20,(0,255,0)))
    map1.add(Platform(825,270,400,30,(0,255,0)))
    map1.add(Platform(460, 200, 30, 30, (0, 255, 0)))

    map1.set_gravity(-4)

def draw_mouse_coords():
    textSurface = myfont.render(str(pygame.mouse.get_pos()), True ,(255,255,255))
    screen.blit(textSurface,(50,30))
def clear_screen():
    pygame.draw.rect(screen, (0,0,0), (0, 0, 1280, 720))


#initialize all data before gameplay
create_map_1()
p1.setMap(map1)


#main while loop
while not simOver:
    #loop through and empty the event queue, key presses
    #buttons, clicks, etc.
    for event in pygame.event.get():
        #if the event is a click on the "X" close button
        if event.type == pygame.QUIT:
            simOver = True

    #draw code
    clear_screen()
    map1.draw(screen)
    p1.draw(screen)
    draw_mouse_coords()

    #player update code
    p1.act()

    #Tween Camera
    cam_x+= ()

    #put all the graphics on the screen
    #should be the LAST LINE of game code
    pygame.display.flip()
    fpsClock.tick(FPS) #slow the loop down to 60 loops per second