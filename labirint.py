import pygame
import modules.image_class as m_cl
import os
import subprocess


def abs_path():
    path_object = os.path.abspath(__file__ + "/..")
    path_object = path_object.split("\\")
    path_object = "\\".join(path_object)
    return path_object 

work_directory = abs_path()
os.chdir(work_directory)


pygame.display.set_caption("Перша гра")
background = pygame.transform.scale(pygame.image.load("images/background.png"), (m_cl.win_width, m_cl.win_height))
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load('music/bg_music.mp3')
pygame.mixer.music.play()

win_music = pygame.mixer.Sound('music/win_music.mp3')
lose_music = pygame.mixer.Sound('music/lose_music.mp3')


monster = m_cl.Enemy('images/mounster.png', 460, 300, 50, 60, 3)
final = m_cl.Image_sprite('images/winner.png', 620, 410,  50, 80, 0)



pygame.font.init()
font = pygame.font.Font(None, 70)
win = font.render('YOU WIN! You ran away.', True, (0, 215, 255))
lose = font.render('YOU LOSE!', True, (255, 255, 0))
font2 = pygame.font.Font(None, 30)
pause = font2.render('ПАУЗА! Натиснить кнопку II для продовження', True, (0, 0, 0))




w1 = m_cl.Wall(179, 0, 0, 100, 20, 600, 10)
w2 = m_cl.Wall(179, 0, 0, 100, 480, 350, 10)
w3 = m_cl.Wall (179, 0, 0, 100, 20, 10, 340)
w4 = m_cl.Wall(179, 0, 0, 200, 130, 10, 350)
w5 = m_cl.Wall(179, 0, 0, 450, 130, 10, 360)
w6 = m_cl.Wall(179, 0, 0, 300, 20, 10, 350)
w7 = m_cl.Wall(179, 0, 0, 390, 120, 180, 10)
w8 = m_cl.Wall(179, 0, 0, 690, 20, 10, 390)
w9 = m_cl.Wall(179, 0, 0, 600, 410, 100, 10)


sprite_list = pygame.sprite.Group()
for i in range(9):
    sprite = [w1,w2,w3,w4,w5,w6,w7,w8,w9]
    sprite_list.add(sprite)
print(sprite_list)

image1_right = [pygame.transform.scale(pygame.image.load("images/ghost3.png"), (50, 60)), pygame.transform.scale(pygame.image.load("images/ghost3_1.png"), (50,60)), pygame.transform.scale(pygame.image.load("images/ghost3_2.png"), (50,60)), pygame.transform.scale(pygame.image.load("images/ghost3_3.png"), (50,60))]
image2_left = [pygame.transform.scale(pygame.image.load("images/ghost4.png"), (50,60)), pygame.transform.scale(pygame.image.load("images/ghost4_1.png"), (50,60)), pygame.transform.scale(pygame.image.load("images/ghost4_2.png"), (50,60)), pygame.transform.scale(pygame.image.load("images/ghost2_3.png"), (50,60))]
image4_down = [pygame.transform.scale(pygame.image.load("images/ghost.png"), (50,60)), pygame.transform.scale(pygame.image.load("images/ghost1_1.png"), (50,60)), pygame.transform.scale(pygame.image.load("images/ghost1_2.png"), (50,60)), pygame.transform.scale(pygame.image.load("images/ghost1_3.png"), (50,60))]
image3_up = [pygame.transform.scale(pygame.image.load("images/ghost2.png"), (50,60)), pygame.transform.scale(pygame.image.load("images/ghost2_1.png"), (50,60)), pygame.transform.scale(pygame.image.load("images/ghost2_2.png"), (50,60)), pygame.transform.scale(pygame.image.load("images/ghost2_3.png"), (50,60))]

sprite_images = image4_down



animation_speed = 0.15
animation_index = 0

sprite_rect = pygame.Rect(0, 0, 64, 64)
sprite_rect.center = (50, 50)



run = True
finish = False
clock = pygame.time.Clock()
FPS = 60

def collision():
    global finish
    for wall in sprite_list:
        if sprite_rect.colliderect(wall):
    
            finish = True
            m_cl.screen.blit(lose, (200, 200))
            lose_music.play()

        if sprite_rect.colliderect(monster):
            finish = True
            m_cl.screen.blit(lose, (200, 200))
            lose_music.play()


        if sprite_rect.colliderect(final):
            finish = True
            m_cl.screen.blit(win, (200, 200))
            win_music.play()

game_paused = False

while run:
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if m_cl.pause_button.collidepoint(x , y):
                game_paused = not game_paused
                


    if finish != True and game_paused == False:
        
        m_cl.screen.blit(background,(0, 0))
        monster.update()
        monster.reset()
        final.reset()
        m_cl.pause_button.bt_reset() 
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and sprite_rect.x > 5:
            sprite_images = image2_left 
            sprite_rect.x -= 5
            animation_index += 1
            if animation_index >= len(sprite_images):
                animation_index = 0
        elif keys[pygame.K_d] and sprite_rect.x <  800 - 80:
            sprite_images = image1_right
            sprite_rect.x += 5
            animation_index += 1
            if animation_index >= len(sprite_images):
                animation_index = 0
        elif keys[pygame.K_w] and sprite_rect.y > 5:
            sprite_images = image3_up 
            sprite_rect.y -= 5
            animation_index += 1
            if animation_index >= len(sprite_images):
                animation_index = 0
        elif keys[pygame.K_s] and sprite_rect.y  < 530 - 100:
            sprite_images = image4_down 
            sprite_rect.y += 5
            animation_index += 1
            if animation_index >= len(sprite_images):
                animation_index = 0
        elif keys[pygame.K_ESCAPE]:
                run = False
        
        m_cl.screen.blit(sprite_images[animation_index], sprite_rect)

        collision()
  
        pygame.display.flip()

        pygame.time.delay(10)

        pygame.display.flip()
        clock.tick(FPS)
    
    elif finish != True and game_paused == True:
        m_cl.screen.blit(pause, (200, 200))
        pygame.display.flip()
        clock.tick(10) 