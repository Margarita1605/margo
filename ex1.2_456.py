import numpy as np 
a = np.array([[1.2, 2.4, 3.6], [3.5, 6.7, 1.5], [8.4, 3.1, 9.2]]) 

d=a.shape
print(a)
print(d)

g=a.max(axis = 1)
j=a.max(axis = 0)
print('макс в каждой строке = ',g)
print('макс в каждой столб = ',j)

k=a.min(axis = 1)
w=a.min(axis = 0)
print('мин в каждой строке = ',k)
print('мин в каждой столб = ',w)

t=a.sum(axis = 1)
u=a.sum(axis = 0)
print('сум в каждой строке = ',t)
print('сум в каждой столб = ',u)
