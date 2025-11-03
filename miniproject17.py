import numpy as np
import matplotlib.pyplot as plt
x=np.random.rand(100,1)

y=2*x.flatten()+3+np.random.randn(100)*0.5
ones=np.ones((x.shape[0],1))

bias_term=np.hstack((x,ones))

beta=np.linalg.inv(x.T@x)@x.T@y
print("coefficients array is",beta)
prdictions=x@beta
print("predictions are",prdictions)
plt.scatter(x,y,label="original data")
plt.plot(x,prdictions,color='red',label="Regression line")
plt.xlabel(x)
plt.ylabel(y)
plt.legend()
plt.show()


