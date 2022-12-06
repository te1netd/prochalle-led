##
##
## LED0-4 wo sorezore tenmetsu
## LED5 wo zutto tenmetsu
##
##
## ---- Imports ---- ##
import board
from piper_blockly import *
import time
import math
## ---- Definitions ---- ##
def upRange(start, stop, step):
  while start <= stop:
    yield start
    start += abs(step)
    
    
GP0 = piperPin(board.GP0, "GP0")
GP1 = piperPin(board.GP1, "GP1")
GP2 = piperPin(board.GP2, "GP2")
GP3 = piperPin(board.GP3, "GP3")
GP4 = piperPin(board.GP4, "GP4")

GP5 = piperPin(board.GP5, "GP5")

rad = 0.1
phase = [0,3.14,0,3.14,0,3.14]
period = [0.8,1,1.2,1.4,1.6]

## ---- Code ---- ##

GP5.setPin(1)  ## tree top on

while True:
  rad = rad + 0.005    
  print (period[0] * rad + phase[0]) 
  GP0.setPin( math.cos(period[0] * rad + phase[0]) >0 )
  GP1.setPin( math.cos(period[1] * rad + phase[1]) >0 )
  GP2.setPin( math.cos(period[2] * rad + phase[2]) >0 )
  GP3.setPin( math.cos(period[3] * rad + phase[3]) >0 )
  GP4.setPin( math.cos(period[4] * rad + phase[4]) >0 )




GP5.setPin(0)  ## tree top off




