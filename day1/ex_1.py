
import matplotlib.pyplot as mplot
import numpy as np
import sys
import math

xval = np.linspace(-3, 3, num = 101)
yval = []

if not sys.argv[1:]:
	print("usage: ex_1.py [function_number]\n\nFunction:\n\
		(1) -> f(x) = x\n\
		(2) -> f(x) = exp(x)\n\
		(3) -> f(x) = sqrt(|x|)\n")
	exit(1)

elif sys.argv[1] == "1":
	for i in xval:
		yval.append(i)
	
	mplot.plot(xval, yval)
	mplot.ylabel('f(x)')
	mplot.xlabel('x')
	mplot.title('y = x')
	mplot.show()

elif sys.argv[1] == "2":
	for i in xval:
		yval.append(math.exp(i))
	
	mplot.plot(xval, yval)
	mplot.ylabel('f(x)')
	mplot.xlabel('x')
	mplot.title('y = exp(x)')
	mplot.show()

elif sys.argv[1] == "3":
	for i in xval:
		yval.append(math.sqrt(abs(i)))
	
	mplot.plot(xval, yval)
	mplot.ylabel('f(x)')
	mplot.xlabel('x')
	mplot.title('y = sqrt(|x|)')
	mplot.show()
