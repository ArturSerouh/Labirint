import pygame
import modules.image_class as m_cl
import subprocess


pygame.init()

WIDTH = 1000
HEIGHT = 800
pygame.mixer.init()
pygame.mixer.music.load('music/menu_music.mp3')
pygame.mixer.music.play()


screen = pygame.display.set_mode((WIDTH, HEIGHT))


screen.fill((100, 92, 152))

clock = pygame.time.Clock()

FPS = 60

game = True


def run_game():
    global game
    while game:
        m_cl.start_button.bt_reset() 
        m_cl.setting_button.bt_reset()
        m_cl.aftors_button.bt_reset() 
        m_cl.exit_button.bt_reset()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if m_cl.start_button.collidepoint(x, y):
                    process = subprocess.Popen(['python', 'labirint.py'])
                    pygame.mixer.music.pause()
                    process.wait()
                    pygame.mixer.music.play()
                    
                if m_cl.exit_button.collidepoint(x, y):
                    game = False      


        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    run_game()

