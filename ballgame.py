from pygame import *
import random

ballpic = image.load('ball.png')
ballpic.set_colorkey((0,0,0))
backdrop = image.load('background.png')

done = False

numballs = 10
delay = 2
balls = []

for count in range(numballs):
    balls.append(dict)
    balls[count] = {'x': random.randint(0, 628), 'y': random.randint(0,448),
                    'xmove': random.randint(1, 4),
                    'ymove': random.randint(1, 4)
                    }

init()
screen = display.set_mode((660, 480))
display.set_caption('Ball game')

while done != True:
    screen.blit(backdrop, (0,0))
    event.set_grab(1)
    for count in range(numballs):
        screen.blit(ballpic, (balls[count]['x'], balls[count]['y']))
    display.update()
    for count in range(numballs):
        balls[count]['x'] = balls[count]['x'] + balls[count]['xmove']
        balls[count]['y'] = balls[count]['y'] + balls[count]['ymove']
    for count in range(numballs):
        if balls[count]['x'] > 628:
            balls[count]['xmove'] = random.randint(-3, -1)
        if balls[count]['x'] < -10:
            balls[count]['xmove'] = random.randint(1, 3)
        if balls[count]['y'] > 448:
            balls[count]['ymove'] = random.randint(-3, -1)
        if balls[count]['y'] < -10:
            balls[count]['ymove'] = random.randint(1, 3)
    for e in event.get():
        if e.type == KEYUP:
            if e.key == K_ESCAPE:
                done = True
                quit()
    if screen.get_at((mouse.get_pos())) == (255, 255, 255, 255):
        done = True
    
print('You lasted for', time.get_ticks()/1000, 'seconds!')
quit()


