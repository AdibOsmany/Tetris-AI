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
#Point(x=913, y=670)   
def newGame():
    pag.FAILSAFE=True
    pag.moveTo(913,670)
    pag.click()

def checkDone():
    return (pag.pixelMatchesColor(915,650,(28,28,28)))


#take screenshot of score
#Point(x=626, y=875) top left
#Point(x=929, y=902) 
def screenshotScore():
    im = pag.screenshot('score.png',region=(626,875, 300, 28))


def screenshotLine():
    im = pag.screenshot('Line.png',region=(626,903, 300, 28))

def screenshotBlock():
    return pag.screenshot(region=(626,931, 300, 28))
    im = pag.screenshot('Block.png',region=(626,931, 300, 28))
    

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

CANVAS=[[(465, 177), (497, 177), (529, 177), (561, 177), (593, 177), (625, 177), (657, 177), (689, 177), (721, 177), (753, 177)], [(465, 209), (497, 209), (529, 209), (561, 209), (593, 209), (625, 209), (657, 209), (689, 209), (721, 209), (753, 209)], [(465, 241), (497, 241), (529, 241), (561, 241), (593, 241), (625, 241), (657, 241), (689, 241), (721, 241), (753, 241)], [(465, 273), (497, 273), (529, 273), (561, 273), (593, 273), (625, 273), (657, 273), (689, 273), (721, 273), (753, 273)], [(465, 305), (497, 305), (529, 305), (561, 305), (593, 305), (625, 305), (657, 305), (689, 305), (721, 305), (753, 305)], [(465, 337), (497, 337), (529, 337), (561, 337), (593, 337), (625, 337), (657, 337), (689, 337), (721, 337), (753, 337)], [(465, 369), (497, 369), (529, 369), (561, 369), (593, 369), (625, 369), (657, 369), (689, 369), (721, 369), (753, 369)], [(465, 401), (497, 401), (529, 401), (561, 401), (593, 401), (625, 401), (657, 401), (689, 401), (721, 401), (753, 401)], [(465, 433), (497, 433), (529, 433), (561, 433), (593, 433), (625, 433), (657, 433), (689, 433), (721, 433), (753, 433)], [(465, 465), (497, 465), (529, 465), (561, 465), (593, 465), (625, 465), (657, 465), (689, 465), (721, 465), (753, 465)], [(465, 497), (497, 497), (529, 497), (561, 497), (593, 497), (625, 497), (657, 497), (689, 497), (721, 497), (753, 497)], [(465, 529), (497, 529), (529, 529), (561, 529), (593, 529), (625, 529), (657, 529), (689, 529), (721, 529), (753, 529)], [(465, 561), (497, 561), (529, 561), (561, 561), (593, 561), (625, 561), (657, 561), (689, 561), (721, 561), (753, 561)], [(465, 593), (497, 593), (529, 593), (561, 593), (593, 593), (625, 593), (657, 593), (689, 593), (721, 593), (753, 593)], [(465, 625), (497, 625), (529, 625), (561, 625), (593, 625), (625, 625), (657, 625), (689, 625), (721, 625), (753, 625)], [(465, 657), (497, 657), (529, 657), (561, 657), (593, 657), (625, 657), (657, 657), (689, 657), (721, 657), (753, 657)], [(465, 689), (497, 689), (529, 689), (561, 689), (593, 689), (625, 689), (657, 689), (689, 689), (721, 689), (753, 689)], [(465, 721), (497, 721), (529, 721), (561, 721), (593, 721), (625, 721), (657, 721), (689, 721), (721, 721), (753, 721)], [(465, 753), (497, 753), (529, 753), (561, 753), (593, 753), (625, 753), (657, 753), (689, 753), (721, 753), (753, 753)], [(465, 785), (497, 785), (529, 785), (561, 785), (593, 785), (625, 785), (657, 785), (689, 785), (721, 785), (753, 785)]]

def boardState():
    board=np.array([[0]*10]*19)
    for i in range(19):
        for j in range(10):
            space= pag.pixel(CANVAS[i][j][0],CANVAS[i][j][1])
            if ( space != (0,0,0)):
                board[i][j]=1
    return board

def isEmpty(rgb):
    if rgb == (0,0,0):
        return 0
    return 1

def testB(line):
    return [isEmpty(pag.pixel(x,y)) for x,y in line]

# for line in CANVAS:
#     print(testB(line)) 

# x=465
# y=145
time.sleep(2)
pag.moveTo(869,208)

# if __name__ == "__main__":
#     main()