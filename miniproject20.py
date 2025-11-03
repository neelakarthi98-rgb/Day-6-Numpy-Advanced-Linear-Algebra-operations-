import numpy as np
x=np.array([[2,1,3],
           [3,4,5],
           [4,6,1]])
ope=(x-x.mean(axis=0))/x.std(axis=0)
print("The result is",ope)
mean=ope.mean(axis=0)
std=np.std(ope,axis=0)
print("mean value is",mean)
print("standarlized value is",std)