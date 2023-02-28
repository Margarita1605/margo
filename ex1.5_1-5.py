import numpy as np 
a=np.array([[2,8],[1,6]])
b=np.array([[3,2,7],[4,1,8],[6,3,7]])
g=np.array([[4,3,2,7],[6,1,1,-2],[7,5,8,1],[9,5,-3,-5]])

d=a.transpose() 
z=b.transpose() 
i=g.transpose() 
print(' транспонированную',d)
print(z)
print(i)

t = np.linalg.inv(a)
y = np.linalg.inv(b)
o= np.linalg.inv(g)
print('обратная',t)
print(y)
print(o)

a1 = np.linalg.det(a)
a2 = np.linalg.det(b)
a3 = np.linalg.det(g)
print('определитель',a1)
print('определитель',a2)
print('определитель', round(a3,2) )

b1=np.linalg.norm(b, ord=1)
print('норма 3 на 3',b1)

b2=np.linalg.norm(g, ord=1)
print('норма 4 на 4',b2)


