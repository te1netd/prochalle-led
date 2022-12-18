## ---- Imports ---- ##
import board
from piper_blockly import *
import time
## ---- Definitions ---- ##
GP0 = piperPin(board.GP0, "GP0")
GP1 = piperPin(board.GP1, "GP1")
GP2 = piperPin(board.GP2, "GP2")
GP3 = piperPin(board.GP3, "GP3")
GP4 = piperPin(board.GP4, "GP4")
GP6 = piperPin(board.GP6, "GP6")
GP7 = piperPin(board.GP7, "GP7")
GP8 = piperPin(board.GP8, "GP8")
GP15 = piperPin(board.GP15, "GP15")
## ---- Code ---- ##

while True:
  while GP15.checkPin(Pull.UP):
    pass

  for count in range(10):
    if count % 3 == 1:
      R = 0
      G = 1
      B = 1
    else:
      if count % 3 == 2:
        R = 1
        G = 0
        B = 1
      else:
        R = 1
        G = 1
        B = 0
    GP6.setPin(R)
    GP7.setPin(G)
    GP8.setPin(B)

    GP0.setPin(1)
    GP1.setPin(0)
    GP2.setPin(1)
    GP3.setPin(0)
    GP4.setPin(1)
    time.sleep(0.5)
    GP0.setPin(0)
    GP1.setPin(1)
    GP2.setPin(0)
    GP3.setPin(1)
    GP4.setPin(0)
    time.sleep(0.5)
    
  GP0.setPin(0)
  GP1.setPin(0)
  GP2.setPin(0)
  GP3.setPin(0)
  GP4.setPin(0)
  GP6.setPin(1)
  GP7.setPin(1)
  GP8.setPin(1)
    





