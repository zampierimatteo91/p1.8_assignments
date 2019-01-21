import matplotlib.pyplot as mplot
import numpy as np
import sys


xval = np.linspace(-5, 5, num = 101)
yval = []

if sys.argv[1] == "1":
	for i in xval:
		yval.append(i)
	print(yval)
	mplot.plot(xval, yval)
	mplot.ylabel('f(x)')
	mplot.xlabel('x')
	mplot.title('y = x')
	mplot.show()

elif sys.argv[1] == "2":
	for i in xval:
		yval.append(i**2)
	print(yval)
	mplot.plot(xval, yval)
	mplot.ylabel('f(x)')
	mplot.xlabel('x')
	mplot.title('y = x**2')
	mplot.show()

elif sys.argv[1] == "3":
	for i in xval:
		yval.append(i**3)
	print(yval)
	mplot.plot(xval, yval)
	mplot.ylabel('f(x)')
	mplot.xlabel('x')
	mplot.title('y = x**3')
	mplot.show()
