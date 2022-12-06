## ---- Imports ---- ##
import time
import board
from digitalio import Pull
from piper_blockly import *

## ---- Definitions ---- ##
GP15 = piperPin(board.GP15, "GP15")
GP0 = piperPin(board.GP0, "GP0")

## ---- Code ---- ##
while True:
  if not GP15.checkPin(Pull.UP):
    GP0.setPin(1)
  else:
    GP0.setPin(0)
  time.sleep(0.1)



