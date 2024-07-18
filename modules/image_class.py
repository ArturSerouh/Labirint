import pygame

win_width = 1000
win_height = 800

screen = pygame.display.set_mode((win_width, win_height))



class Image_sprite():
    def __init__(self, player_image, x, y, player_width, player_hight, player_speed):
        self.image = pygame.transform.scale(pygame.image.load(player_image), (player_width, player_hight))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.player_width = player_width
        self.player_hight = player_hight
        self.speed = player_speed
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Wall(pygame.sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Enemy(Image_sprite):
    direction = "left"

    def update(self):
        if self.rect.x <= 480:
            self.direction = "right"
        if self.rect.x >= 650:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
start_button = 'images/batton_start.png'
setting_button = 'images/batton_settings.png'
aftors_button = 'images/batton_aftor.png'
exit_button = 'images/batton_exit.png'
pause_button = 'images/batton_pause.png'


class Buttons():
    def __init__(self, image, x=0, y=0):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def bt_reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y) 
   
start_button = Buttons('images/batton_start.png', 100, 100)
setting_button = Buttons('images/batton_settings.png', 600, 100)
aftors_button = Buttons('images/batton_aftor.png', 100, 400)
exit_button = Buttons('images/batton_exit.png', 600, 400)
pause_button = Buttons('images/batton_pause.png', 725, 15)