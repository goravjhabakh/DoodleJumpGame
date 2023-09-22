import pygame
import random
pygame.init()

player=pygame.transform.scale(pygame.image.load('sprite1.png'),(50,50))
sky=pygame.image.load('sky.png')

fps=60
font = pygame.font.Font('pixel.ttf',36)
timer=pygame.time.Clock()

platforms=[[350,550,200,15],[500,450,200,15],[350,350,200,15],
           [200,250,200,15],[350,150,200,15],[500,50,200,15]]
jump=False
y_change=0
x_change=0
collided=[]

screen=pygame.display.set_mode((900,600))
pygame.display.set_caption('GAME')

player_x=400
player_y=450
speed=5
score=0
highscore=0
gameover=False

def update_player(y):
    global jump
    global y_change
    jumph=12
    gravity=0.5
    if jump:
        y_change= -jumph
        jump=False
    y+=y_change
    y_change+=gravity
    return y

def check_collision(blcks,jmp):
    global player_x
    global player_y
    global y_change
    global collided
    global score
    for i in range(len(blcks)):
        if blcks[i].colliderect([player_x+10,player_y+50,40,5]) and jmp==False and y_change>0:
            if blcks[i] not in collided:
                collided.append(blcks[i])
                print(collided)
                score+=1
            jmp=True
    return jmp

def reset():
    global gameover
    gameover=False
    global score
    score=0
    global collided
    collided=[]
    global player_x
    player_x=400
    global player_y
    player_y=450
    platforms=[[350,550,200,15],[500,450,200,15],[350,350,200,15],[200,250,200,15],[350,150,200,15],[500,50,200,15]]
    
run=True
while run:
    timer.tick(fps)
    screen.fill((0,0,0))
    screen.blit(sky,(0,0))
    screen.blit(player,(player_x,player_y))
    score_text=font.render('Score: '+str(score),True,(0,0,0))
    screen.blit(score_text,(650,10))
    
    blocks=[]

    for i in range(len(platforms)):
        block=pygame.draw.rect(screen,(0,0,0),platforms[i],0,5)
        blocks.append(block)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            '''if event.type==pygame.K_r and gameover:
                gameover=False
                score=0
                player_x=400
                player_y=450
                platforms=[[350,550,200,15],[500,450,200,15],[350,350,200,15],[200,250,200,15],[350,150,200,15],[500,50,200,15]]'''
            if event.key==pygame.K_LEFT:
                x_change = -speed
            if event.key==pygame.K_RIGHT:
                x_change = speed
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                x_change = 0
            if event.key==pygame.K_RIGHT:
                x_change = 0
            '''if event.key==pygame.K_r:
                gameover=False
                score=0
                player_x=400
                player_y=450
                platforms=[[350,550,200,15],[500,450,200,15],[350,350,200,15],[200,250,200,15],[350,150,200,15],[500,50,200,15]]'''
        
    player_x+=x_change
    jump=check_collision(blocks,jump)

    if player_x<=-20:
        player_x=-20
    if player_x>=820:
        player_x=820

    if x_change>0:
        player=pygame.transform.scale(pygame.image.load('sprite1.png'),(50,50))
    elif x_change<0:
        player=pygame.transform.flip(pygame.transform.scale(pygame.image.load('sprite1.png'),(50,50)),1,0)

    if player_y>-80 and player_y<550:
        player_y=update_player(player_y)
    else:
        gameover=True
        y_change=0
        x_change=0

    if gameover:
        if player_y<50:
            over=font.render('WIN!',True,(255,128,0))
            screen.blit(over,(350,200))
        else:
            reset()

    pygame.display.flip()
pygame.quit()
    
