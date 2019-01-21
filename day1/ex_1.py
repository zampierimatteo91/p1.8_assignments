
import matplotlib.pyplot as mplot
import numpy as np
import sys
import math

xval = np.linspace(-5, 5, num = 101)
yval = []

if sys.argv[1] == "1":
	for i in xval:
		yval.append(i)
	
	mplot.plot(xval, yval)
	mplot.ylabel('f(x)')
	mplot.xlabel('x')
	mplot.title('y = x')
	mplot.show()

elif sys.argv[1] == "2":
	for i in xval:
		yval.append(math.sin(i))

	mplot.plot(xval, yval)
	mplot.ylabel('f(x)')
	mplot.xlabel('x')
	mplot.title('y = sin(x)')
	mplot.show()

elif sys.argv[1] == "3":
	for i in xval:
		yval.append(math.cos(i))

	mplot.plot(xval, yval)
	mplot.ylabel('f(x)')
	mplot.xlabel('x')
	mplot.title('y = cos(x)')
	mplot.show()

elif sys.argv[1] == "4":
	for i in xval:
		yval.append(math.tan(i))

	mplot.plot(xval, yval)
	mplot.ylabel('f(x)')
	mplot.xlabel('x')
	mplot.title('y = tan(x)')
	mplot.show()
