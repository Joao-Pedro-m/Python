import time
import os,tty,termios,sys
os.system("clear")
a1 = "░░"
a = [
["  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
["  ","웃",a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,"  "],
["  ",a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,"  "],
["  ",a1,a1,a1,a1,a1,"  ",a1,a1,a1,a1,a1,a1,"  "],
["  ",a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,"  "],
["  ",a1,a1,a1,a1,a1,"  ",a1,a1,a1,a1,a1,a1,"  "],
["  ",a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,"  "],
["  ",a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,"  "],
["  ",a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,"  "],
["  ",a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,"  "],
["  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
["\n\n","\n\n","\n\n","\n\n"],
]

class player:
  def __init__(self,posX,posY):
    self.posX = posX
    self.posY = posY

def atualizarFps():
 time.sleep(0.1)
 os.system("clear")
 for x in a:
   print(" "*20,*x, sep = "")
 if readkey != "":
   movimento()

def movimento():
  if readkey() == UP:
    if a[jogador.posY-1][jogador.posX] == "░░":
      a[jogador.posY][jogador.posX] = "░░" 
      a[jogador.posY-1][jogador.posX] = "웃"
      jogador.posY = jogador.posY-1
  elif readkey() == DOWN:
    if a[jogador.posY+1][jogador.posX] == "░░":
      a[jogador.posY][jogador.posX] = "░░" 
      a[jogador.posY+1][jogador.posX] = "웃"
      jogador.posY = jogador.posY+1

  elif readkey() == LEFT:
    if a[jogador.posY][jogador.posX-1] == "░░":
      a[jogador.posY][jogador.posX] = "░░" 
      a[jogador.posY][jogador.posX-1] = "웃"
      jogador.posX = jogador.posX-1
  elif readkey() == RIGHT:
    if a[jogador.posY][jogador.posX+1] == "░░":
      a[jogador.posY][jogador.posX] = "░░" 
      a[jogador.posY][jogador.posX+1] = "웃"
      jogador.posX = jogador.posX+1

  atualizarFps()



def readchar():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

def readkey():
	c1 = readchar()
	if ord(c1) != 0x1b:
		return c1
	c2 = readchar()
	if ord(c2) != 0x5b:
		return c1 + c2
	c3 = readchar()
	if ord(c3) != 0x33:
		return c1 + c2 + c3
	c4 = readchar()
	return c1 + c2 + c3 + c4

UP = '\x1b\x5b\x41'
DOWN = '\x1b\x5b\x42'
LEFT = '\x1b\x5b\x44'
RIGHT = '\x1b\x5b\x43'

jogador = player(1,1)


atualizarFps()
