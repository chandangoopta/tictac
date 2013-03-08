from numpy import matrix
from numpy import linalg

tic = matrix( [[0,0,0],[0,0,0],[0,0,0]])
print tic

move1=raw_input("first player, input row\n")
move2=raw_input("input column\n")
tic[move1,move2]='x'
print tic

