## ---- Imports ---- ##
import board
from piper_blockly import *
import time

## ---- Definitions ---- ##
GP6 = piperPin(board.GP6, "GP6")
GP7 = piperPin(board.GP7, "GP7")
GP8 = piperPin(board.GP8, "GP8")

## ---- Code ---- ##
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
  time.sleep(1)

GP6.setPin(1)
GP7.setPin(1)
GP8.setPin(1)

