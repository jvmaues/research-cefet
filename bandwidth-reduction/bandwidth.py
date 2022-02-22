import math

from numpy import arange
A = [[1,4], [0,2,4], [1,3], [2,4,5], [0,1,3], [3]]
f1 = [2, 3, 4, 1, 5, 6]

B = [[1], [0, 2, 3], [1], [1, 4], [3]]
f2 = [3, 1, 2, 5, 4]

def dif(p, q):
    return abs(p-q)
        
def measureBand(A, f):
    width = 0
    for v in range(len(A)):
        for adj in A[v]:
            temp = dif(f[v], f[adj])
            if temp > width:
                width = temp
            
    return width