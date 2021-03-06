import numpy as np

x=np.array([[3,6],[4,7],[2,6],[4,8]])
y=[9,11,8,12]

np.random.seed(2)

m,n=np.shape(x)
theta=np.random.rand(n)

print "Initial value of weights" 
print theta

xTrans = x.transpose()
for i in range(0, 100000):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        gradient = np.dot(xTrans, loss) / m
        theta = theta - 0.0005 * gradient

print "Final value of weights"
print theta
print "Addition of 34 and 6 is equal to"
print np.dot(np.array([[34,6]]),theta)
