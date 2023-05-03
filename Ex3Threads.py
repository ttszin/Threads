from numpy import random
import numpy as np
import sys

def transposta(i,j, l=None):
        if l:
            print(f"l na funcao: {l}")
            for idx in l:
                #print(f"idx: {idx}")
                x = idx[0]
                y = idx[1]
                soma[y][x] = x1[x][y]
        else:
            soma[j][i] = x1[i][j]
        

x= int(random.randint(1,5))
y= int(random.randint(1,5))
th = 0
if x==y==1:
    x = int(random.randint(1,5))

n = int(x*y)
r = list(range(n))
if not len(r) == 1:
    r.remove(0)
if r[0] != 0:
    th = random.choice(r)
if th == 0:
    sys.exit(1)


print(f'x:{x}    y: {y}     t: {th}')

soma = np.zeros((y,x))
x1 = random.randint(100, size=(x, y))
#x1 = np.zeros((x,y))
#x2 = random.randint(100, size=(x, y))

print(f"x1: shape: {x1.shape}")



resto = n%th

print(f"resto: {resto}")

idx= []
for i in range(x):
    for j in range(y):
        idx.append((i,j))
print(f'len(idx): {len(idx)}')
print(idx)
print(f'\nm = \n{x1}')
for t in range(th):
    
    if th !=1:
        id = idx.pop()
        x,y = id[0], id[1]
        transposta(x,y)

    if t+1 == th and len(idx)>1:
        print("penultima thread")
        transposta(0,0,idx)
print(f'transposta:\n{soma}')