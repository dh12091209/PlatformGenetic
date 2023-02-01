import pygame


class Player:
    def __init__(self):
        self.x = 400
        self.y = 400
        self.width = 30
        self.height = 30
        self.color = (255,0,0)
        self.isJumping = False
        self.currentJumpVel = 40
        self.maxJumVel = 40

    def draw(self,screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width))

    def handle_key_presses(self):
        if pygame.key.get_pressed()[pygame.K_SPACE] and not self.isJumping:
            self.isJumping = True

    def act(self):
        oldx = self.x
        oldy = self.y

        self.handle_key_presses()
        self.handleJump()
        self.y -= self.map.get_gravity()
        if self.is_map_collision():
            self.x = oldx
            self.y = oldy
            self.isJumping = False
            self.currentJumpVel = self.maxJumVel


    def handleJump(self):
        if self.isJumping:
           self.y -= self.currentJumpVel
           self.currentJumpVel += self.map.get_gravity()
           # terminal velocity
           if self.currentJumpVel < -self.maxJumVel:
              self.currentJumpVel = -self.maxJumVel




    def setMap(self,map):
        self.map = map

    def is_map_collision(self):
        myHitBox = pygame.Rect(self.x,self.y,self.width,self.height)
        mapHitBoxes = self.map.get_hit_box_list()
        for box in mapHitBoxes:
            if myHitBox.colliderect(box):
                return True
        return False




class Platform:
    def __init__(self,x,y,width,height,color):
        self.x=x;
        self.y = y;
        self.width = width;
        self.height = height;
        self.color = color;

    #used for drawing and used for collision detection
    def getRect(self):
        return pygame.Rect(self.x,self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen,self.color,self.getRect())

class Map:

    def __init__(self,gravity = -0.5):
        self.platforms = []
        self.gravity = gravity

    def get_gravity(self):
        return self.gravity

    def set_gravity(self,gravity):
        self.gravity = gravity


    def add(self,platform):
        self.platforms.append(platform)

    def get_hit_box_list(self):
        hitBoxes = []
        for p in self.platforms:
            hitBoxes.append(p.getRect())

        return hitBoxes

    #Precondition: the platforms list is a homogeneous list of Platform objects
    def draw(self, screen):
        for p in self.platforms:
            p.draw(screen)


