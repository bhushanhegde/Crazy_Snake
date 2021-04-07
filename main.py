import pygame
import random
from time import sleep
import os
import subprocess

pygame.init()

HIGHT=601
WIDTH=601

window=pygame.display.set_mode((HIGHT,WIDTH))
pygame.display.set_caption("CRAZY SNAKE")

cell_length=HIGHT//20
#print(cell_length)

speed=[7]
#initial snake body

body=[]
head=[cell_length*2,cell_length]
body.append(head)
body.append([cell_length*1,cell_length])
body.append([0,cell_length])

#type of play
border=False

food_pos=[0,cell_length]

def draw_grid():
    
    for x in range(0,WIDTH,cell_length):
        pygame.draw.line(window,(255,255,255),(x,cell_length),(x,WIDTH))


    for y in range(0,HIGHT,cell_length):
        pygame.draw.line(window,(255,255,255),(0,y),(WIDTH,y))

def rand_food():
    global food_pos
    randx=random.randrange(0,WIDTH-1,cell_length)
    randy=random.randrange(cell_length,HIGHT-1,cell_length)
    food_pos=[randx,randy]

def food():
    while food_pos in body:
        rand_food()
        
    pygame.draw.rect(window,(255,0,0),(food_pos[0]+1,food_pos[1]+1,cell_length-1,cell_length-1))


def snake(orient=None):
    global food_pos
    heads=False
    #if player selects border type
    if border:
        #right border check
        if body[0][0]>=WIDTH:
            exit()
        
        #left border check
        if body[0][0]<0:
            exit()

        #top border check
        if body[0][1]<cell_length:
            exit()
        
        #bottom border check
        if body[0][1]>=HIGHT:
            exit()
    else:
        #right border check
        if body[0][0]>=WIDTH-1:
            body[0][0]=0
        
        #left border check
        if body[0][0]<0:
            body[0][0]=WIDTH-1

        #top border check
        if body[0][1]<cell_length:
            body[0][1]=HIGHT-1
        
        #bottom border check
        if body[0][1]>=HIGHT:
            body[0][1]=cell_length
            
    for s in body:
        #check for snake bite
        if s==body[0]:
            if heads:
                exit()
            heads=True
        pygame.draw.rect(window,(0,255,0),(s[0]+1,s[1]+1,cell_length-1,cell_length-1))
    snake_head(orient)

    #if snake head touches the food then increase the size of snake by one
    #print(body[0],food_pos)
    if body[0]==food_pos:
        add_tail()
        food()
    
def add_tail():
    #identify the direction of movement of snake

    #right side movement
    if body[-1][1]==body[-2][1] and body[-1][0]<body[-2][0]:
        body.append([body[-1][0]-cell_length,body[-1][1]])
    
    #left side movement
    elif body[-1][1]==body[-2][1] and body[-1][0]>body[-2][0]:
        body.append([body[-1][0]+cell_length,body[-1][1]])

    #downward movement
    elif body[-1][0]==body[-2][0] and body[-1][1]<body[-2][1]:
        body.append([body[-1][0],body[-1][1]-cell_length])
    else:
        body.append([body[-1][0],body[-1][1]+cell_length])
    
def snake_head(orient):
    if orient==None or orient=='R':
        pygame.draw.circle(window,(0,0,255),(body[0][0]+cell_length-(cell_length//3),body[0][1]+cell_length-(cell_length/1.5)),(cell_length/8))
        pygame.draw.circle(window,(0,0,255),(body[0][0]+cell_length-(cell_length//3),body[0][1]+(cell_length/1.25)),(cell_length/8))
    elif orient=='L':
        pygame.draw.circle(window,(0,0,255),(body[0][0]+(cell_length//3),body[0][1]+cell_length-(cell_length/1.5)),(cell_length/8))
        pygame.draw.circle(window,(0,0,255),(body[0][0]+(cell_length//3),body[0][1]+(cell_length//1.25)),(cell_length/8))
    elif orient=='U':
        pygame.draw.circle(window,(0,0,255),(body[0][0]+(cell_length//4),body[0][1]+(cell_length//4)),(cell_length/8))
        pygame.draw.circle(window,(0,0,255),(body[0][0]+int(0.75*cell_length),body[0][1]+(cell_length//4)),(cell_length/8))
    elif orient=='D':
        pygame.draw.circle(window,(0,0,255),(body[0][0]+(cell_length//4),body[0][1]+int(0.75*cell_length)),(cell_length/8))
        pygame.draw.circle(window,(0,0,255),(body[0][0]+int(0.75*cell_length),body[0][1]+int(0.75*cell_length)),(cell_length/8))


def start():
    start=False
    while not start:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if event.type==pygame.KEYDOWN:
                start=True
    #move towards right
    right()
    
def right():
    pressed=False
    while not pressed:
        move_right()
        pygame.display.update()
        sleep(1/speed[0])
        for key in pygame.event.get():
            if key.type==pygame.QUIT:
                exit()
            if key.type==pygame.KEYDOWN:
                if key.key==pygame.K_s:
                    speed[0]+=1
                if key.key==pygame.K_b:
                    if speed[0]>1:
                        speed[0]-=1
                if key.key==pygame.K_DOWN or key.key==pygame.K_2:
                    pressed=True
                    down()
                elif key.key==pygame.K_UP or key.key==pygame.K_8:
                    pressed=True
                    up()
                elif key.key==pygame.K_RIGHT or key.key==pygame.K_6:
                    pass
                elif key.key==pygame.K_LEFT or key.key==pygame.K_4:
                    pass


def left():
    pressed=False
    while not pressed:
        move_left()
        pygame.display.update()
        sleep(1/speed[0])

        for key in pygame.event.get():
            if key.type==pygame.QUIT:
                exit()
            if key.type==pygame.KEYDOWN:
                if key.key==pygame.K_s:
                    speed[0]+=1
                if key.key==pygame.K_b:
                    if speed[0]>1:
                        speed[0]-=1
                if key.key==pygame.K_DOWN or key.key==pygame.K_2:
                    pressed=True
                    down()
                elif key.key==pygame.K_UP or key.key==pygame.K_8:
                    pressed=True
                    up()
                elif key.key==pygame.K_RIGHT or key.key==pygame.K_6:
                    pass
                elif key.key==pygame.K_LEFT or key.key==pygame.K_4:
                    pass


def down():
    pressed=False
    while not pressed:
        move_down()
        pygame.display.update()
        sleep(1/speed[0])
        for key in pygame.event.get():
            if key.type==pygame.QUIT:
                exit()
            if key.type==pygame.KEYDOWN:
                if key.key==pygame.K_s:
                    speed[0]+=1
                if key.key==pygame.K_b:
                    if speed[0]>1:
                        speed[0]-=1
                if key.key==pygame.K_DOWN or key.key==pygame.K_2:
                    pass
                elif key.key==pygame.K_UP or key.key==pygame.K_8:
                    pass
                elif key.key==pygame.K_RIGHT or key.key==pygame.K_6:
                    pressed=True
                    right()
                elif key.key==pygame.K_LEFT or key.key==pygame.K_4:
                    pressed=True
                    left()

def up():
    pressed=False
    while not pressed:
        move_up()
        pygame.display.update()
        sleep(1/speed[0])
        for key in pygame.event.get():
            if key.type==pygame.QUIT:
                exit()
            if key.type==pygame.KEYDOWN:
                if key.key==pygame.K_s:
                    speed[0]+=1
                if key.key==pygame.K_b:
                    if speed[0]>1:
                        speed[0]-=1
                if key.key==pygame.K_DOWN or key.key==pygame.K_2:
                    pass
                elif key.key==pygame.K_UP or key.key==pygame.K_8:
                    pass
                elif key.key==pygame.K_RIGHT or key.key==pygame.K_6:
                    pressed=True
                    right()
                elif key.key==pygame.K_LEFT or key.key==pygame.K_4:
                    pressed=True
                    left()

                

def move_down():
    print("D")
    #clear the previous snake
    for s in body:
        pygame.draw.rect(window,(0,0,0),(s[0]+1,s[1]+1,cell_length-1,cell_length-1))
    
    
    #head of the snake shoud be down
    #body[0][1]+=cell_length
    body.pop()
    #the remaining should follow the successor
    body.insert(0,[body[0][0],body[0][1]+cell_length])
    
    snake('D')

def move_up():
    print("U")
    #clear the previous snake
    for s in body:
        pygame.draw.rect(window,(0,0,0),(s[0]+1,s[1]+1,cell_length-1,cell_length-1))
    body.pop()

    body.insert(0,[body[0][0],body[0][1]-cell_length])
    
    snake('U')

def move_left():
    print("L")
    for s in body:
        pygame.draw.rect(window,(0,0,0),(s[0]+1,s[1]+1,cell_length-1,cell_length-1))
    body.pop()
    body.insert(0,[body[0][0]-cell_length,body[0][1]])
    
    snake('L')


    
def move_right():
    print("R")
    for s in body:
        pygame.draw.rect(window,(0,0,0),(s[0]+1,s[1]+1,cell_length-1,cell_length-1))
    body.pop()
    body.insert(0,[body[0][0]+cell_length,body[0][1]])
    
    snake('R')


def main():
    draw_grid()
    pygame.display.update()
    food()
    pygame.display.update()
    snake()
    pygame.display.update()
    start()
    pygame.display.update()
    
    exit=False
    while not exit:
        #pygame.time(50)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True


main()
