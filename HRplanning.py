import numpy

# Forecasting number of available workers
D = numpy.array([[],[],[]])
M = numpy.array([[],[],[]])
b = numpy.array([[],[],[]])
a = M@numpy.linalg.inv(D)@b
print(a)

# Forecasting number of needed workers
X = numpy.array([[],[],[],[],[],[],[],[],[]])
Y = numpy.array([[],[],[],[],[],[],[],[],[]])
XTX = numpy.matmul(X.T,X)
print(XTX)
inverse = numpy.linalg.inv(XTX)
print(inverse)
XTY = numpy.matmul(X.T,Y)
print(XTY)
betas = numpy.matmul(inverse,XTY)
print(betas)