from numpy import matrix
from numpy import linalg

tic = matrix( [[0,0,0],[0,0,0],[0,0,0]])
print tic

def input(move1,move2):
   	#move1=raw_input("first player, input row\n")
	#move2=raw_input("input column\n")
	#print type(move1)
	tic[int(move1),int(move2)]=1
	print tic

#conditions
pl1=raw_input("input your move position\n")
pl1=int(pl1)

if pl1==1:
	move1=0
	move2=0
	input(move1,move2)
else:
	move1=0
	move2=1
	input(move1,move2)
