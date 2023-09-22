import pygame
pygame.init()

screen=pygame.display.set_mode((900,600))
pygame.display.set_caption('GAME')
timer=pygame.time.Clock()

player=pygame.image.load('sprite1.png')
sky=pygame.image.load('sky.png')
font=pygame.font.Font('pixel.ttf',20)

player_x=400
player_y=450
y_change=0
jump=False
vel=5
m=1
v=5

run=True
while run:
    screen.blit(sky,(0,0))
    screen.blit(player,(player_x,player_y))

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x>=vel:
        player_x-=vel
    if keys[pygame.K_RIGHT] and player_x<800:
        player_x+=vel
    if keys[pygame.K_SPACE] and not jump:
        jump=True
    if jump:
        F=(1/2)*m*(v**2)
        player_y-=F
        v=v-1
        if v<0:
            m=-1
        if v==-6:
            jump=False
            v=5
            m=1

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.time.delay(50)
    pygame.display.flip()

pygame.quit()
