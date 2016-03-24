# Matrix Algebra

import numpy as np
from numpy import linalg 
A = np.matrix('1 2 3; 2 7 4')
B = np.matrix('1 -1; 0 1')
C = np.matrix('5 -1; 9 1; 6 0')
D = np.matrix('3 -2 -1; 1 2 3')
u = np.matrix('6 2 -3 5')
v = np.matrix('3 5 -1 4')
w = np.matrix('1;8;0;5')
alpha = 6

##Matrix Dimensions
A.shape
B.shape
C.shape
D.shape
u.shape
v.shape
w.shape

##Vector Operations
u + v
u - v
alpha * u
u * v
np.linalg.norm(u)

##Matrix Operations
#A + C ##is indeed not defined
A - np.matrix.transpose(C)
np.matrix.transpose(C) + 3*D
B * A
##B * np.matrix.transpose(A) #is indeed not defined
