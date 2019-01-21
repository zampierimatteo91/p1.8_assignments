
import matplotlib.pyplot as mplot
import numpy as np
import sys

xval = np.linspace(-5, 5, num = 101)
yval = []

if not sys.argv[1:]:
	print("usage: ex_1.py [function_number]\n\nFunction:\n\
		(1) -> f(x) = x\n")
	exit(1)

elif sys.argv[1] == "1":
	for i in xval:
		yval.append(i)
	
	mplot.plot(xval, yval)
	mplot.ylabel('f(x)')
	mplot.xlabel('x')
	mplot.title('y = x')
	mplot.show()

