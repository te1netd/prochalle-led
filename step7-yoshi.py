##
##
## LED0-4 wo sorezore tenmetsu
## LED5 wo zutto tenmetsu
## FULL COLOR LED GP6,7,8
##
## MUSIC GP10
##

## ---- Imports ---- ##
import board
from piper_blockly import *
import time
import math
import analogio
import pwmio


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
    
GP0 = piperPin(board.GP0, "GP0")
GP1 = piperPin(board.GP1, "GP1")
GP2 = piperPin(board.GP2, "GP2")
GP3 = piperPin(board.GP3, "GP3")
GP4 = piperPin(board.GP4, "GP4")
GP5 = piperPin(board.GP5, "GP5")
GP15 = piperPin(board.GP15, "GP15")

R = pwmio.PWMOut(board.GP6, frequency=100)
G = pwmio.PWMOut(board.GP7, frequency=100)
B = pwmio.PWMOut(board.GP8, frequency=100)

GP9 = pwmio.PWMOut(board.GP10,  frequency=65535,  duty_cycle=32768, variable_frequency=True)

score = [65535,880,880,880,0,880,880,880,0,880, 1046, 699,784,880,0,0,0,932,932,932,932,932,880,880,880,880,784,784,698,784,1046,0,65535]

rad = 0.1
phase = [   0,  3.14,   0, 3.14,   0]
period = [0.8,      1, 1.2,  1.4, 1.6]
score_i = 0
i = 65535

## ---- Code ---- ##

GP5.setPin(1)  ## tree top on

while rad < 3.14 * 2 * 28 :
  rad = rad + 0.002    
#DEBUG  print (period[0] * rad + phase[0]) 
  GP0.setPin( math.cos(period[0] * rad + phase[0]) >0 )
  GP1.setPin( math.cos(period[1] * rad + phase[1]) >0 )
  GP2.setPin( math.cos(period[2] * rad + phase[2]) >0 )
  GP3.setPin( math.cos(period[3] * rad + phase[3]) >0 )
  GP4.setPin( math.cos(period[4] * rad + phase[4]) >0 )

  degree= rad / 3.1415 * 180
  R.duty_cycle = int(Degree2Color(degree, 0))
  G.duty_cycle = int(Degree2Color(degree, 120))
  B.duty_cycle = int(Degree2Color(degree, 240))
 # time.sleep(0.05)  
 
# music
  if i == 65535:
    if GP15.checkPin(Pull.UP):
      pass
    else:
      i = 0
  else:   
    score_i = score_i + 1
    if score_i >= 125:
      i = i + 1
      score_i = 0
      if i >= len(score):
        i = 65535
      else:
        if score[i] == 0:
          if score[i-1] == 0:
            if score[i-2] == 0:
              if score[i-3] == 0:
                GP9.frequency = score[i-4]
              else:
                GP9.frequency = score[i-3]
            else:
              GP9.frequency = score[i-2]
          else:
            GP9.frequency = score[i-1]
        else:           
          GP9.frequency = score[i]
    if score_i == 120:
      if i < len(score)-1:
        if score[i+1] == 0:
          pass
        else:
          GP9.frequency = 65535

  

GP0.setPin(0)  ## LED off
GP1.setPin(0)  ## LED off
GP2.setPin(0)  ## LED off
GP3.setPin(0)  ## LED off
GP4.setPin(0)  ## LED off
GP5.setPin(0)  ## tree top off
R.duty_cycle = 65535  ## R off
G.duty_cycle = 65535  ## G off
B.duty_cycle = 65535  ## B off 







