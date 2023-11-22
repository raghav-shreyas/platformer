import pygame
from pygame.locals import *
pygame.init()

clock=pygame.time.Clock()
fps=60


screen_width=680
screen_height=680
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("platformer")

#load images
sun_img=pygame.image.load("sun.png")
bg_img=pygame.image.load("sky1.png")

tile_size=34


def grid():
    for line_ in range(0, 20):
	    pygame.draw.line(screen,(255, 255, 255),(0, line_ * tile_size),(screen_width, line_ * tile_size));pygame.draw.line(screen,(255, 255, 255),(line_ * tile_size, 0),(line_ * tile_size, screen_height))

class player:
    def __init__(self,x,y):
        player_img=pygame.image.load("player.png.png")
        self.image=pygame.transform.scale(player_img,(100,100))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.vel_y=0
        self.jumped=False
    def update(self):

        dx=0
        dy=0

        key=pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped==False:
            self.vel_y=-15
            self.jumped=True
        if key[pygame.K_SPACE]==False:
            self.jumped=False
        if key[pygame.K_LEFT]:
            dx-=5
        if key[pygame.K_RIGHT]:
            dx+=5
        
        #gravity
        self.vel_y+=1
        if self.vel_y>10:
            self.vel_y=10

        dy+=self.vel_y
        
        self.rect.x+=dx
        self.rect.y+=dy
        if self.rect.bottom>screen_height:
            self.rect.bottom=screen_height
            dy=0


        #drawing player to screen
        screen.blit(self.image,self.rect)



class world():
    def __init__(self,data):
        self.tile_list=[]
        #image

        dirt_img=pygame.image.load("dirtt.png")
        grass_img=pygame.image.load("grass.png")
        row_count=0
        for row in data:
            col_count=0
            for tile in row:
                if tile==1:
                    img=pygame.transform.scale(dirt_img,(tile_size,tile_size))
                    img_rect=img.get_rect()
                    img_rect.x=col_count*tile_size
                    img_rect.y=row_count*tile_size
                    tile=(img,img_rect)
                    self.tile_list.append(tile)
                if tile==2:
                    img=pygame.transform.scale(grass_img,(tile_size,tile_size))
                    img_rect=img.get_rect()
                    img_rect.x=col_count*tile_size
                    img_rect.y=row_count*tile_size
                    tile=(img,img_rect)
                    self.tile_list.append(tile)
                col_count+=1
            row_count+=1
    def draw(self):
      for tile in self.tile_list:
            screen.blit(tile[0],tile[1])




world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1], 
[1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1], 
[1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

player=player(50,screen_height-125)
world=world(world_data)

run=True
while run:

    clock.tick(fps)

    screen.blit(bg_img,(0,0))
    screen.blit(sun_img,(35,15))
    

    grid()
    world.draw()
    player.update()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()
