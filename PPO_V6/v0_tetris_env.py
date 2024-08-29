import gymnasium as gym
from gymnasium.spaces import Discrete, Box, Dict
from gymnasium.envs.registration import register
from gymnasium.utils.env_checker import check_env
import numpy as np
import random
import time
import easyocr
import pyautogui as pag
from PIL import Image
from collections import OrderedDict


def readImg(img):
    reader=easyocr.Reader(['en'], gpu=False, verbose=False)
    result=reader.readtext(img)
    if len(result)==0:
        return 0
    elif (not result[0][1].isdigit()):
        return 0
    output=result[0][1]
    return int(output)
    
#get the score 
def getScore():
    pag.screenshot('score.png',region=(626,875, 300, 28))
    return readImg('score.png')
    
#of lines
def getLine():
    pag.screenshot('line.png',region=(626,903, 300, 28))
    return readImg('line.png')

#of Blocks
def getBlocks():
    pag.screenshot('blocks.png',region=(626,931, 300, 28))
    return readImg('blocks.png')

L_BLOCK = (227,91,2)
J_BLOCK = (33,65,198)
T_BLOCK = (175,41,138)
O_BLOCK = (227,159,2)
S_BLOCK = (89,177,1)
Z_BLOCK = (215,15,55)

BLOCKS=[J_BLOCK,L_BLOCK,O_BLOCK,T_BLOCK,S_BLOCK,Z_BLOCK]

#rotate counter clock wise
def rotateCC():
    pag.keyDown('z')
    pag.keyUp('z')


#rotate clockwise
def rotateCW():
    pag.keyDown('up')
    pag.keyUp('up')


#soft drop
def softDrop():
    pag.keyDown('down')
    pag.keyUp('down')


#hard drop
def hardDrop():
    pag.keyDown('space')
    pag.keyUp('space')


#move right
def right():
    pag.keyDown('right')
    pag.keyUp('right')



#move left
def left():
    pag.keyDown('left')
    pag.keyUp('left')


#new game
#Point(x=913, y=670)   
def newGame():
    pag.FAILSAFE=True
    pag.moveTo(913,670)
    pag.click()


def checkDone():
    return (not pag.pixelMatchesColor(915,650,(0,0,0)))


def getTetromino(piece = 1):
    tetromino= pag.pixel(869,108+(piece*100))
    if tetromino in BLOCKS:
        return BLOCKS.index(tetromino) + 1
    return 7

    # No Piece [J_BLOCK, L_BLOCK, O_BLOCK, T_BLOCK, S_BLOCK, Z_BLOCK, I_BLOCK]
    #   0         1        2        3        4        5        6        7   


#hold key
def hold():
    pag.keyDown('c')
    pag.keyUp('c')

CANVAS=[(465, 145), (497, 145), (529, 145), (561, 145), (593, 145), (625, 145), (657, 145), (689, 145), (721, 145), (753, 145), (465, 177), (497, 177), (529, 177), (561, 177), (593, 177), (625, 177), (657, 177), (689, 177), (721, 177), (753, 177), (465, 209), (497, 209), (529, 209), (561, 209), (593, 209), (625, 209), (657, 209), (689, 209), (721, 209), (753, 209), (465, 241), (497, 241), (529, 241), (561, 241), (593, 241), (625, 241), (657, 241), (689, 241), (721, 241), (753, 241), (465, 273), (497, 273), (529, 273), (561, 273), (593, 273), (625, 273), (657, 273), (689, 273), (721, 273), (753, 273), (465, 305), (497, 305), (529, 305), (561, 305), (593, 305), (625, 305), (657, 305), (689, 305), (721, 305), (753, 305), (465, 337), (497, 337), (529, 337), (561, 337), (593, 337), (625, 337), (657, 337), (689, 337), (721, 337), (753, 337), (465, 369), (497, 369), (529, 369), (561, 369), (593, 369), (625, 369), (657, 369), (689, 369), (721, 369), (753, 369), (465, 401), (497, 401), (529, 401), (561, 401), (593, 401), (625, 401), (657, 401), (689, 401), (721, 401), (753, 401), (465, 433), (497, 433), (529, 433), (561, 433), (593, 433), (625, 433), (657, 433), (689, 433), (721, 433), (753, 433), (465, 465), (497, 465), (529, 465), (561, 465), (593, 465), (625, 465), (657, 465), (689, 465), (721, 465), (753, 465), (465, 497), (497, 497), (529, 497), (561, 497), (593, 497), (625, 497), (657, 497), (689, 497), (721, 497), (753, 497), (465, 529), (497, 529), (529, 529), (561, 529), (593, 529), (625, 529), (657, 529), (689, 529), (721, 529), (753, 529), (465, 561), (497, 561), (529, 561), (561, 561), (593, 561), (625, 561), (657, 561), (689, 561), (721, 561), (753, 561), (465, 593), (497, 593), (529, 593), (561, 593), (593, 593), (625, 593), (657, 593), (689, 593), (721, 593), (753, 593), (465, 625), (497, 625), (529, 625), (561, 625), (593, 625), (625, 625), (657, 625), (689, 625), (721, 625), (753, 625), (465, 657), (497, 657), (529, 657), (561, 657), (593, 657), (625, 657), (657, 657), (689, 657), (721, 657), (753, 657), (465, 689), (497, 689), (529, 689), (561, 689), (593, 689), (625, 689), (657, 689), (689, 689), (721, 689), (753, 689), (465, 721), (497, 721), (529, 721), (561, 721), (593, 721), (625, 721), (657, 721), (689, 721), (721, 721), (753, 721), (465, 753), (497, 753), (529, 753), (561, 753), (593, 753), (625, 753), (657, 753), (689, 753), (721, 753), (753, 753)]

def pixel_rgb(img, x, y):
	r, g, b = img.getpixel((x, y))
	return (r, g, b)

def boardState():
    img = pag.screenshot().convert('RGB')
    return np.reshape([0 if pixel_rgb(img, i[0], i[1])==(0,0,0) else 1 for i in CANVAS],(20,10))

register(
    id='Tetris-AI-v0',
    entry_point= 'v0_tetris_env:tetrisEnv',
)

class tetrisEnv(gym.Env):

    global ACTIONS
    #           0        1        2       3    4    5      6
    ACTIONS=[rotateCC,rotateCW,softDrop,right,left,hold,hardDrop]

    # No Piece [J_BLOCK, L_BLOCK, O_BLOCK, T_BLOCK, S_BLOCK, Z_BLOCK, I_BLOCK]
    #   0         1        2        3        4        5        6        7   
    metadata={"render_modes":[None], 'render_fps': 1 }
    
    def __init__(self):
        self.action_space = Discrete(7)
        self.observation_space = Dict({'Current': Discrete(8), 'Next':Discrete(8), 'Hold':Discrete(8), 'Board':Box(0,1, shape=(20,10), dtype= int)})
        self.state=OrderedDict(sorted({'Current': 0, 'Next': 0, 'Hold': 0, 'Board': np.reshape([[0]*10]*20, (20,10))}.items()))
        self.empty=True
        self.held=False
        self.nextPiece2=0

    def step(self, action):

        reward=1

        #apply actions
        ACTIONS[action]()
        if action==5:
            if self.empty:
                self.state['Hold']=self.state['Current']
                self.state['Current']=self.state['Next']
                self.state['Next']=getTetromino()
                self.nextPiece2=getTetromino(piece=2)
                self.empty=False
                self.held=True

            elif self.held==False:
                temp=self.state['Current']
                self.state['Current']=self.state['Hold']
                self.state['Hold']=temp
                self.held=True
        
        #update board
        self.state['Board']=boardState()

        #update current and next piece
        next=getTetromino()
        next2=getTetromino(piece=2)
        if ((self.state['Next'] != next) or (self.nextPiece2 != next2)): #checks if piece changed
            self.state['Current']=self.state['Next']
            self.state['Next']=next
            self.nextPiece2=next2
            self.held=False
            reward+=5
        

        #check if done
        done=checkDone()
        if done:
            reward+= (getLine()*50)+5

        #set placeholder
        info={}

        #return stuff
        return self.state, reward, done, info

        
    def render(self):
        pass

    def reset(self):
        newGame()
        self.state= {'Current': getTetromino(), 'Hold': 0}
        self.empty=True
        self.held=False
        time.sleep(2.5)
        self.state['Board']=boardState()
        self.state['Next']= getTetromino()
        self.nextPiece2=getTetromino(piece=2)
        self.state=OrderedDict(sorted(self.state.items()))
        return self.state