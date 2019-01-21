
import matplotlib.pyplot as mplot
import numpy as np
import sys

def f(x):
	return(x)

xval = np.arange(-5.0, 5.1, 0.1)
yval = []

yval = f(xval)
print(yval)

mplot.plot(xval, )
mplot.ylabel('f(x)')
mplot.xlabel('x')
mplot.show()

