import pygame

from sys import exit

width=800
height=600
fps=30

color_rose = (255, 0, 71)

SPEED = 200.0


def create_actors():
    #images
    global jungle
    jungle=pygame.image.load("C:\\Users\\passi\\OneDrive\\Bibliothèque\\Programmation\\Projets python\Battle\\assets\\images\\jungle.png")
    jungle = jungle.convert()

    global jungle_rect
    jungle_rect = jungle.get_rect()
    jungle_rect.bottom = height

    #ship
    global ship
    ship = pygame.image.load ("C:\\Users\\passi\\OneDrive\\Bibliothèque\\Programmation\\Projets python\\Battle\\assets\\images\\ship.png")
    ship = ship.convert_alpha()

    global ship_rect
    ship_rect = ship.get_rect()
    ship_rect.center = (width/2,height/2)

    #eagle
    global eagle
    eagle = pygame.image.load ("C:\\Users\\passi\\OneDrive\\Bibliothèque\\Programmation\\Projets python\\Battle\\assets\\images\\eagle.png")
    eagle = eagle.convert_alpha()

    global eagle_rect
    eagle_rect = eagle.get_rect()
    eagle_rect.center = (width/2,0)   

    #font
    global mfont
    mfont = pygame.font.Font("C:\\Users\\passi\\OneDrive\\Bibliothèque\\Programmation\\Projets python\\Battle\\assets\\fonts\\antonio-Bold.ttf",30)

    #son
    global son
    son = pygame.mixer.Sound("C:\\Users\\passi\\OneDrive\\Bibliothèque\\Programmation\\Projets python\\Battle\\assets\\sounds\\assets_sounds_laser.wav")
    son.set_volume(0.1)

    #music
    pygame.mixer.music.load("C:\\Users\\passi\\OneDrive\\Bibliothèque\\Programmation\\Projets python\\Battle\\assets\\musics\\pump.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

def action_event(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            print("down")
            son.play()
 

    if event.type== pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            print("up")
            son.play()

def jungle_update(delta):
    jungle_rect.y += int(SPEED* delta)

    if jungle_rect.y > 0:
        jungle_rect.bottom = height
        

def action_update(delta):
    #ship_update(delta)
    jungle_update(delta)

    eagle_update(delta)

def eagle_update(delta):
    eagle_rect.y+=int(2*SPEED* delta)

    if eagle_rect.top > height:
        eagle_rect.top = 0

def action_collide():
    if ship_rect.colliderect(eagle_rect):
        print("collide")

    else:
        print("none")
    
def ship_update(delta):
    ship_rect.y -= int(SPEED* delta) 

    if ship_rect.left > width:
        ship_rect.left = 0

    if ship_rect.top > width:
        ship_rect.top = 0    

    if ship_rect.bottom <0:
        ship_rect.top = height

def action_render(ecran):
    ecran.fill((0, 0, 0))
    ecran.blit(jungle,jungle_rect)

    #ship
    ecran.blit(ship,ship_rect)

    #texte
    label = mfont.render("Points=0", 1, color_rose)
    ecran.blit(label,(10,10))

    #the flip
    pygame.display.flip()
    
    
def main():
    pygame.init()

    running=True
    screen=pygame.display.set_mode((width,height))

    pygame.display.set_caption("battle")

    clock=pygame.time.Clock()


    create_actors()

    while running==True:

        delta_ms=clock.tick(fps)

        delta_s=delta_ms/1000

        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                running=False
                
            if evt.type== pygame.KEYDOWN:
                if evt.key == pygame.K_ESCAPE:
                    running=False



            action_event(evt)

        action_update(delta_s)

        action_collide()

        action_render(screen)
    pygame.mixer.music.stop()  
    pygame.quit()
    exit()

    return 0
if __name__ == "__main__":
    main()

    