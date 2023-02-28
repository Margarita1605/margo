import numpy as np 
a = np.array([[4, 2], [9, 1]]) 
b = np.array([[5, 3], [2, 5]]) 
f=np.vstack((a, b)) 
print(f)

g=f[:-1,0]
print(g)

y=g.sum() # Нахождение суммы элементов массива
o=g.min() # Нахождения минимума массива 
x=g.max() 
print('сум=',y,'мин=',o,'макс=',x)

d=np.hstack((a, b))
print(d)

h=d[0, :-1]
print(h)

q=h.sum() # Нахождение суммы элементов массива
w=h.min() # Нахождения минимума массива 
r=h.max() 
print('сум=',q,'мин=',w,'макс=',r)

