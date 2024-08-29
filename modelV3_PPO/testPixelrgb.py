import pyautogui as pag
import time
import random
import numpy as np
import cv2
im=pag.screenshot()
im.save('canvas.png')
rgb=cv2.imread('canvas.png')

board=test=np.array([[0]*10]*19)
y=145
for i in range(19):
    y += 32
    x=465
    for j in range(10):
        space= pag.pixel(x,y)
        if (((rgb[465][245] == np.array([0,0,0])).all()) == False):
            board[i][j]=1
        x += 32
print(board)