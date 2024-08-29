import pyautogui as pag
import time
import random
import numpy as np

L_BLOCK = (227,91,2)
J_BLOCK = (33,65,198)
T_BLOCK = (175,41,138)
O_BLOCK = (227,159,2)
S_BLOCK = (89,177,1)
Z_BLOCK = (215,15,55)

BLOCKS=[J_BLOCK,L_BLOCK,O_BLOCK,T_BLOCK,S_BLOCK,Z_BLOCK]

def wait():
    time.sleep(1)

def getPosition():
    time.sleep(5)
    print(pag.position())

#take screenshot of score
#Point(x=626, y=875) top left
#Point(x=929, y=902) 

#rotate counter clock wise
def rotateCC(timez=1):
    for i in range(timez):
        pag.keyDown('z')
        pag.keyUp('z')


#rotate clockwise
def rotateCW(timez=1):
    for i in range(timez):
        pag.keyDown('up')
        pag.keyUp('up')


#soft drop
def softDrop(timez=1):
    for i in range(timez):
        pag.keyDown('down')
        pag.keyUp('down')


#hard drop
def hardDrop(timez=1):
    for i in range(timez):
        pag.keyDown('space')
        pag.keyUp('space')


#move right
def right(timez=1):
    for i in range(timez):
        pag.keyDown('right')
        pag.keyUp('right')



#move left
def left(timez=1):
    for i in range(timez):
        pag.keyDown('left')
        pag.keyUp('left')


#enter
def enter(timez=1):
    for i in range(timez):
        pag.keyDown('enter')
        pag.keyUp('enter')


#new game
#Point(x=913, y=667)   
def newGame():
    pag.FAILSAFE=True
    time.sleep(1)
    pag.moveTo(913,667)
    pag.click()

def checkDone():
    return (pag.pixelMatchesColor(915,650,(28,28,28)))


#take screenshot of score
#Point(x=626, y=875) top left
#Point(x=929, y=902) 
def screenshotScore():
    im = pag.screenshot(region=(626,875, 300, 28))
    im.save("score.png")

def screenshotLine():
    im = pag.screenshot(region=(626,903, 300, 28))
    im.save("Line.png")

def screenshotBlock():
    im = pag.screenshot(region=(626,931, 300, 28))
    im.save("Block.png")

def getBlock():
    tetromino= pag.pixel(869,208)
    for i in range(len(BLOCKS)):
        if (tetromino == BLOCKS[i]):
            output=[i]
            return np.array(output)
    output=[6]
    return np.array(output)

def Curr_Next():
    return np.array([getBlock(), getBlock()])



#[J_BLOCK, L_BLOCK, O_BLOCK, T_BLOCK, S_BLOCK, Z_BLOCK, L_BLOCK]




# if __name__ == "__main__":
#     main()