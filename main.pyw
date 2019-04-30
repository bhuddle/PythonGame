
# Created by Benjamin Huddle
# Following website below
# https://opensource.com/article/17/12/game-framework-python

import pygame
import sys, os, time


'''
Objects
'''
class Player(pygame.sprite.Sprite):
    '''
    Spawn a player
    '''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        for i in range(1, 7):
            img = pygame.image.load(os.path.join('images', 'hero' + str(i) + '.png'))
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()


    '''
    control player movement 
    '''
    def control(self, x, y):
        self.movex += x
        self.movey += y


    '''
    update sprite position
    '''
    def update(self):
        """logic for keeping player on screen"""
        self.rect.x = self.rect.x + self.movex
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > (worldx - self.image.get_rect().size[0]):
            self.rect.x = worldx - self.image.get_rect().size[0]

        self.rect.y = self.rect.y + self.movey
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > (worldy - self.image.get_rect().size[1]):
            self.rect.y = worldy - self.image.get_rect().size[1]

        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]

        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]

        if self.movey < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]

        if self.movey > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]


'''
Setup
'''
main = True
ALPHA = (0, 255, 0)
worldx = 960
worldy = 720
fps = 60
next_frame = 1.0/fps
ani = 9
clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('images', 'Test.png'))
backdropbox = world.get_rect()
player = Player()
player_list = pygame.sprite.Group()
player_list.add(player)
stepx = 3
stepy = 3
player.rect.x = 50
player.rect.y = 50
player_list = pygame.sprite.Group()
player_list.add(player)

'''
Main Loop
'''
next_tick = time.perf_counter()
last_tick = time.perf_counter()
frame_clock = time.perf_counter()
frame_counter = 0
while main:
    ### Setting current time to track the amount of time passed between
    ### program loops to determine timing for each frame
    current_time = time.perf_counter()
    ### Changed pygame.event.get() to poll for specific events 
    ### (quit, keydown, keyup) rather than all possible events
    events = pygame.event.get([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-stepx, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(stepx, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, -stepy)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, stepy)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(stepx, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-stepx, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, stepy)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, -stepy)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False
    ### if the 'next game tick' is less than or equal to 'current game time'
    if next_tick <= current_time:
        ### while the 'next game tick' is behind the 'current game time',
        ### update the player object, then increase the time until the
        ### 'next game tick' by 'one frame'
        while (next_tick <= current_time):
            delta = current_time-last_tick
            player.update()
            next_tick += next_frame
            frame_counter +=1
        ### draw all updated objects to screen surface
        world.blit(backdrop, backdropbox) ## This is the base background
        player_list.draw(world) ## The player is being drawn to the background
        ### Update the screen to display what is on the screen surface
        pygame.display.flip()
        last_tick = time.perf_counter()
    else:
        ## Sleep until the game needs to be updated next frame
        time.sleep(next_tick-current_time)
    ### Calculate frame rate and update window title to reflect this
    if current_time-frame_clock >= 1:
        pygame.display.set_caption('FPS: '+str(frame_counter))
        frame_counter = 0
        frame_clock = time.perf_counter()
