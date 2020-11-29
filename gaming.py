import pygame
import random
import math
pygame.init()
screen=pygame.display.set_mode((800,500))

pygame.display.set_caption("SPACE BATTLE !!!")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

bgimg=pygame.image.load("yo.jpg")
spimg=pygame.image.load("spobj.png")
bulimg=pygame.image.load("bullet.png")

objx=375
objy=400

alimg=[]
ex=[]
ey=[]
e_change_x=[]
e_change_y=[]
noe=6

global sc_val
sc_val=0
f = pygame.font.Font('freesansbold.ttf', 32)
g = pygame.font.Font('freesansbold.ttf', 128)




for i in range(noe):

    alimg.append(pygame.image.load("ufo.png"))
    ex.append(random.randint(0,735))
    ey.append(random.randint(30,250))
    e_change_x.append(0.35)
    e_change_y.append(50)

bx=0
by=400
b_state = "load"
b_x_change=0
b_y_change=1

changex=changey=0


def background():
    screen.blit(bgimg,(0,0))

def obj(x,y):
    screen.blit(spimg,(x,y))

def alien(p,q,j):
    screen.blit(alimg[j],(p,q))

def fire_b(x,y):
    global b_state
    b_state = "fire"
    screen.blit(bulimg,(x+16,y+10))

def collision_eb(a,b,c,d):
    dist=math.sqrt((math.pow(a-c,2))+(math.pow(b-d,2)))
    if dist <= 27:
        return True
    else:
        return False


def show_score():
    score = f.render("SCORE : "+str(sc_val),True,(255,255,255))
    screen.blit(score,(10,10))

def game_over():
    gv = g.render("GAME OVER !!!",True,(255,0,0))
    screen.blit(gv,(10,150))

    

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changex=-0.6
            if event.key == pygame.K_RIGHT:
                changex=0.6
            if event.key == pygame.K_UP:
                changey=-0.6
            if event.key == pygame.K_DOWN:
                changey=0.6

            if event.key == pygame.K_SPACE:
                if b_state == "load" :
                    bx=objx
                    by=objy
                    fire_b(bx,by)


        elif event.type == pygame.KEYUP:
            changex=changey=0

    background()


    objx+=changex
    objy+=changey

    
        
    if objx >= 736:
        objx=736
    if objx <= 0:
        objx=0
    if objy >= 436:
        objy=436    
    if objy <= 0:
        objy=0

    for i in range(noe):

        if ey[i]+64 >= objy :
            for j in range(noe):
                ey[j]=1000
                ex[j]=1000
            game_over()
            break

        if ex[i] >= 736:
            e_change_x[i]=-0.35
            ey[i]+=e_change_y[i]
        elif ex[i] <= 0:
            e_change_x[i]=0.35
            ey[i]+=e_change_y[i]

        ex[i]+=e_change_x[i]

        alien(ex[i],ey[i],i)

        c=collision_eb(ex[i],ey[i],bx,by)
        if c:
            sc_val=sc_val+1
            bx=objx
            by=objy
            b_state="load"
            ex[i]=random.randint(0,735)
            ey[i]=random.randint(30,250)
            




    if by <=0:
        b_state="load"

    if b_state == "fire":
        by-=b_y_change
        fire_b(bx,by)


    obj(objx,objy)
    show_score()

    pygame.display.update()
    

    

