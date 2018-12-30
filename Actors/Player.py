import pygame
import os
from configs import General
from pygame.locals import *
from configs.General import *
vector = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image_ori = pygame.image.load(os.path.join(IMAGE_FOLDER, PLAYER_IMG)).convert_alpha()
        self.image = self.image_ori
        self.game = game
        self.velocity = vector(int(0), int(0))
        self.position = vector(x, y)
        self.rect = self.image_ori.get_rect()
        self.rect.center = self.position
        self.direction = 0
        self.previous_direction = 0

    def move(self, cardinal):
        self.velocity = vector(0, 0)
        if cardinal == 'south':
            self.velocity.y = PLAYER_SPEED
            self.direction = 180

        if cardinal == 'est':
            self.velocity.x = PLAYER_SPEED
            self.direction = 270

        if cardinal == 'west':
            self.velocity.x = -PLAYER_SPEED
            self.direction = 90

        if cardinal == 'north':
            self.velocity.y = -PLAYER_SPEED
            self.direction = 360

        if cardinal == 'south-west':
            self.velocity.y = int(PLAYER_SPEED*0.7071)
            self.velocity.x = int(-PLAYER_SPEED*0.7071)
            self.direction = 135

        if cardinal == 'south-est':
            self.velocity.y = int(PLAYER_SPEED*0.7071)
            self.velocity.x = int(PLAYER_SPEED*0.7071)
            self.direction = 225

        if cardinal == 'north-west':
            self.velocity.y = int(-PLAYER_SPEED*0.7071)
            self.velocity.x = int(-PLAYER_SPEED*0.7071)
            self.direction = 45

        if cardinal == 'north-est':
            self.velocity.y = int(-PLAYER_SPEED*0.7071)
            self.velocity.x = int(PLAYER_SPEED*0.7071)
            self.direction = 315

        if self.direction != self.previous_direction:
            self.image, self.rect = self.rot_center(self.image_ori, self.rect, self.direction)

        self.position += self.velocity

        if self.position.x < 0:
            self.position.x = 0
            self.rect.x = 0
        if self.position.y < 0:
            self.position.y = 0
            self.rect.y = 0
        if self.position.x > WIDTH:
            self.position.x = WIDTH
            self.rect.x = WIDTH
        if self.position.y > HEIGHT:
            self.position.y = HEIGHT
            self.rect.y = HEIGHT

        self.rect.center = self.position
        print("Rect : {}\t\t{}\t\t Pos : {}\t\t{} Cardinal: {}".format(self.rect.centerx, self.rect.centery, self.position.x, self.position.y, cardinal))

    def rot_center(self, image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image, rot_rect

    def update(self):
        keystate = pygame.key.get_pressed()
        if (keystate[K_DOWN] or keystate[K_s]) and (keystate[K_LEFT] or keystate[K_a] or keystate[K_q]):
            self.move('south-west')
        elif (keystate[K_DOWN] or keystate[K_s]) and (keystate[K_RIGHT] or keystate[K_d]):
            self.move('south-est')
        elif (keystate[K_UP] or keystate[K_z]) and (keystate[K_RIGHT] or keystate[K_d]):
            self.move('north-est')
        elif (keystate[K_UP] or keystate[K_z]) and (keystate[K_LEFT] or keystate[K_a] or keystate[K_q]):
            self.move('north-west')
        elif keystate[K_UP] or keystate[K_w] or keystate[K_z]:
            self.move('north')
        elif keystate[K_RIGHT] or keystate[K_d]:
            self.move('est')
        elif keystate[K_DOWN] or keystate[K_s]:
            self.move('south')
        elif keystate[K_LEFT] or keystate[K_a] or keystate[K_q]:
            self.move('west')

