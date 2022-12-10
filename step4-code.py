##
## ライブラリを使うための命令
## 最初に書く
##
import board
from piper_blockly import *

##
## GPピンを変数に割り当てる
##
GP0 = piperPin(board.GP0, "GP0")
GP1 = piperPin(board.GP1, "GP1")
GP2 = piperPin(board.GP2, "GP2")
GP3 = piperPin(board.GP3, "GP3")
GP4 = piperPin(board.GP4, "GP4")

##
## LEDをひからせる
##
GP0.setPin(1)
GP1.setPin(1)
GP2.setPin(1)
GP3.setPin(1)
GP4.setPin(1)

##
## LEDを消す
##
##GP0.setPin(0)
##GP1.setPin(0)
##GP2.setPin(0)
##GP3.setPin(0)
##GP4.setPin(0)
