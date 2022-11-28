##---- JUNBI ----##
GP1 = piperPin(board.GP1, "GP1")
GP2 = piperPin(board.GP2, "GP2")
GP3 = piperPin(board.GP3, "GP3")
GP4 = piperPin(board.GP4, "GP4")

##---- LED ON -----##
GP1.setPin(1)
GP2.setPin(1)
GP3.setPin(1)
GP4.setPin(1)

## ---- LED OFF ----##
GP1.setPin(0)
GP2.setPin(0)
GP3.setPin(0)
GP4.setPin(0)


