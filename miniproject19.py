import numpy as np
A=np.array([[1,2],
           [2,3]])
B=np.array([2,1])

x=np.linalg.solve(A,B)
print("solutions is:",x)