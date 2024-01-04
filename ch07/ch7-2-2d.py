import numpy as np 

a = np.array([[1,2,3],[4,5,6]])
b = np.zeros_like(a)
print(b)
print("===========================")
c = np.ones_like(a)
print(c)
print("===========================")
d = np.eye(3)  
print(d)
print("---------------------------")
e = np.eye(3, k=1)
print(e)
print("===========================")    
f = np.random.rand(3)
print(f)
print("---------------------------")
g = np.random.rand(3,3)
print(g)   
