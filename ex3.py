from numpy import random
import numpy as np
import sys
import threading


def transposta(ini,end):
    global idx1
    numeros = idx1[ini:end]
    for idx in numeros:
        
        x = idx[0]
        y = idx[1]
        
        soma[y][x] = x1[x][y]
        


x= int(random.randint(1,5))
y= int(random.randint(1,5))
th = 0
elements = x*y
if x==y==1:
    x = int(random.randint(1,5))

n = int(x*y)
r = list(range(n))
if not len(r) == 1:
    r.remove(0)
if r[0] != 0:
    th = int(random.choice(r))
if th == 0:
    print("th = 0")
    sys.exit(1)



soma = np.zeros((y,x))
x1 = random.randint(100, size=(x, y))



idx = []
for i in range(x):
    for j in range(y):
        idx.append((i,j))


threads = []
ini = 0
tam = len(idx)/th
tam = int(tam)
end = tam
idx1= idx[:]

for i in range(th):
    if i+1==th:
    
        end=len(idx)
    
    t = threading.Thread(target=transposta, args=(ini,end))
    t.start()
    threads.append(t)
    ini = end
    end+=tam

for t in threads:
    t.join()


print(f"\nM: \n{x1}")
print(f"\nM.T: \n{soma}")