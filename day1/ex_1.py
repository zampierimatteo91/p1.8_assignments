
import matplotlib.pyplot as mplot
import numpy as np
import sys

def f(x):
	return(x)

xval = np.arange(-5.0, 5.1, 0.1)
yval = []

if sys.argv[1] == "1":
	yval = f(xval)
	print(yval)
	mplot.plot(xval, yval)
	mplot.ylabel('f(x)')
	mplot.xlabel('x')
	mplot.show()

