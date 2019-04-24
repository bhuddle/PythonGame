
# Created by Benjamin Huddle
# Following website below
# https://opensource.com/article/17/12/game-framework-python

import pygame
import sys, os


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
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

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
ani = 4
clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('images', 'Test.png'))
backdropbox = world.get_rect()
player = Player()
player_list = pygame.sprite.Group()
player_list.add(player)
stepx = 10
stepy = 10
player.rect.x = 50
player.rect.y = 50
player_list = pygame.sprite.Group()
player_list.add(player)

'''
Main Loop
'''
while main == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left')
                player.control(-stepx, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right')
                player.control(stepx, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('up')
                player.control(0, -stepy)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                print('down')
                player.control(0, stepy)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left')
                player.control(stepx, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right')
                player.control(-stepx, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('up')
                player.control(0, stepy)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                print('down')
                player.control(0, -stepy)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    world.blit(backdrop, backdropbox)
    player.update()
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)