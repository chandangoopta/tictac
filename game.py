from numpy import matrix
from numpy import linalg

tic = matrix( [[0,0,0],[0,0,0],[0,0,0]])
print tic

move1=raw_input("first player, input row\n")
move2=raw_input("input column\n")
#print type(move1)
tic[int(move1),int(move2)]=1
print tic

