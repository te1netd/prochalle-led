## ---- Imports ---- ##
import board
from piper_blockly import *
import time
import math
import analogio


# Describe function
def Degree2Color(degree, phase):
  tempD = (degree - phase) % 360
#DEBUG  print(tempD)
  if tempD < 60:
    color = (tempD / 60) * 65535
  elif tempD < 180:
    color = 65535
  elif tempD < 240:
    color = ((240 - tempD) / 60) * 65535
  else:
    color = 0
  return color


## ---- Definitions ---- ##
def upRange(start, stop, step):
  while start <= stop:
    yield start
    start += abs(step)
    
R = pwmio.PWMOut(board.GP6, frequency=100)
G = pwmio.PWMOut(board.GP7, frequency=100)
B = pwmio.PWMOut(board.GP8, frequency=100)

rad=0

## ---- Code ---- ##


while rad < 3.14 * 2 * 20 :
  rad = rad + 0.0002    
#DEBUG  print (period[0] * rad + phase[0]) 

  degree= rad / 3.1415 * 180
  R.duty_cycle = int(Degree2Color(degree, 0))
  G.duty_cycle = int(Degree2Color(degree, 120))
  B.duty_cycle = int(Degree2Color(degree, 240))
 


R.duty_cycle = 65535  ## R off
G.duty_cycle = 65535  ## G off
B.duty_cycle = 65535  ## B off 








